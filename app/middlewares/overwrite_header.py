

def overwrite_header(get_response):
    def middleware(request):
        if 'X-Gateway-Name' in request.headers and request.headers['X-Gateway-Name'] == 'fitzme-gateway':
            request.META['HTTP_X_FORWARDED_PROTO'] = 'https'

        response = get_response(request)

        return response
    return middleware
