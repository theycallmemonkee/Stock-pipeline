import requests

def extract_data(symbol: str):
    API_KEY = "61afbf6c2d204a9e8078a47da54ee66b"

    url = "https://api.twelvedata.com/time_series"

    params = {
        "symbol": symbol,
        "interval": "1day",
        "outputsize": 30,
        "apikey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data