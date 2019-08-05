

def tx_management(get_response):
    GLOBAL_TX_HEADER_NAME = "X-Global-Tx"
    LOCAL_TX_HEADER_NAME = "X-Local-Tx"

    def middleware(request):
        global_tx = request.headers.get(GLOBAL_TX_HEADER_NAME)
        local_tx = request.headers.get(LOCAL_TX_HEADER_NAME)

        response = get_response(request)

        if global_tx:
            response[GLOBAL_TX_HEADER_NAME] = global_tx
        if local_tx:
            response[LOCAL_TX_HEADER_NAME] = int(local_tx) + 1

        return response

    return middleware
