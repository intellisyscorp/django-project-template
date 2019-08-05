

def user_management(get_response):
    USER_HEADER_NAME = "X-User-ID"

    def middleware(request):
        user_id = request.headers.get(USER_HEADER_NAME)

        if user_id:
            request.user_id = user_id

        response = get_response(request)
        return response

    return middleware
