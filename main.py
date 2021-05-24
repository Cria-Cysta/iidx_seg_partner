import spiceapi

def spice_connect(host, port, password):
    detail=spiceapi.Connection(
        host=host,
        port=port,
        password=password
        )
    return detail

def ticker_get(detail):
    ticker=spiceapi.iidx_ticker_get(detail)
    convtext=str(ticker[0])
    return convtext

