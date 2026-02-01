import requests

def get_all_crypto_rates():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'ngn',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'sparkline': 'false'
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return []