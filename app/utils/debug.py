import functools

from django.db import connection

__all__ = [
    'debug_db_queries_here',
    'debug_db_queries_decorator',
]


def debug_db_queries_here(marker: str = 'HERE'):
    print(f'> # of Queries {marker}: {len(connection.queries)}')


def debug_db_queries_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'> # of Queries BEFORE {func}: {len(connection.queries)}')

        response = func(*args, **kwargs)

        print(f'> # of Queries AFTER {func}: {len(connection.queries)}')
        return response
    return wrapper
