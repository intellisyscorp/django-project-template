import pprint
from datetime import datetime

from django.db import connection


def debug_middleware(get_response):
    def middleware(request):
        print("[{}] {} {} | {}".format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            request.method,
            request.get_full_path(),
            getattr(request, 'user_id', None),
        ))

        print('>>> Request Headers')
        try:
            pprint.pprint(dict(request.headers), indent=4)
        except Exception as e:
            print('\t' + str(e))

        print(f'>>> # of Queries START: {len(connection.queries)}')

        response = get_response(request)

        print(f'>>> # of Queries FINISH: {len(connection.queries)}')

        print('>>> Response Data')
        try:
            pprint.pprint(dict(response.data), indent=4)
        except Exception as e:
            print('\t' + str(e))

        return response
    return middleware
