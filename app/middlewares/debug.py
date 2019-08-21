import logging
import pprint
import traceback

from django.db import connection


def debug_middleware(get_response):
    def middleware(request):
        # Skip debugging for swagger page
        if 'swagger' in request.get_full_path():
            return get_response(request)

        logging.info('%s %s | %s', request.method, request.get_full_path(), getattr(request, 'user_id', None))

        print('• Request Headers:')
        try:
            pprint.pprint(dict(request.headers or {}), indent=8)
        except:
            traceback.print_exc()

        print('• DB Queries:')
        print(f'\t# of Queries START: {len(connection.queries)}')

        response = get_response(request)

        print(f'\t# of Queries FINISH: {len(connection.queries)}')

        print('• List of %d DB Queries:' % len(connection.queries))
        pprint.pprint(connection.queries)

        print('• Response Data:')
        try:
            pprint.pprint(dict(response.data or {}), indent=8)
        except:
            traceback.print_exc()

        return response
    return middleware
