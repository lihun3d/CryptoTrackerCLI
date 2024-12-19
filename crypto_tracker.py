import requests

def get_crypto_price(crypto_symbol):
    """
    Function to fetch the current price of a cryptocurrency using a free API.
    :param crypto_symbol: Symbol of the cryptocurrency (e.g., BTC, ETH)
    :return: Price of the cryptocurrency in USD
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get(crypto_symbol.lower(), {}).get("usd", "Price not available")
    else:
        return "Failed to fetch price. Please try again later."

def main():
    print("Welcome to CryptoTrackerCLI!")
    print("Type the symbol of a cryptocurrency to check its price (e.g., BTC, ETH).")
    print("Type 'exit' to quit the program.")
    
    while True:
        crypto_symbol = input("Enter cryptocurrency symbol: ").strip().lower()
        if crypto_symbol == "exit":
            print("Goodbye!")
            break
        price = get_crypto_price(crypto_symbol)
        print(f"The current price of {crypto_symbol.upper()} is: ${price}")

if __name__ == "__main__":
    main()
