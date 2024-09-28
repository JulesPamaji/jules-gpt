import requests
from requests.exceptions import RequestException

class BlockchainAPI:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def get_balance(self, address):
        endpoint = f"{self.base_url}/address/{address}/balance"
        response = self.make_request(endpoint)
        return response['balance']

    def get_transaction_history(self, address):
        endpoint = f"{self.base_url}/address/{address}/transactions"
        response = self.make_request(endpoint)
        return response['transactions']

    def make_request(self, endpoint):
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error fetching data: {e}")
            return None

# Example usage:
api_url = "https://blockchain-api.example.com/v1/"
headers = {'API-Key': 'your-api-key'}
blockchain = BlockchainAPI(api_url, headers)

address = "1BTCAddressExample"
balance = blockchain.get_balance(address)
print(f"Balance for {address}: {balance} BTC")

# Fetch transaction history
tx_history = blockchain.get_transaction_history(address)
print("Transaction History:")
for tx in tx_history:
    print(tx)