import binascii
from bitcoin import privkey_to_pubkey, pubkey_to_address

class PrivateKeyResult:
    def __init__(self, private_key, btc_address, balance=None):
        self.private_key = private_key
        self.btc_address = btc_address
        self.balance = balance
        self.wif = self.get_wif()
        self.private_key_hex = self.get_hex()

    def get_wif(self):
        """Convert private key to Wallet Import Format (WIF)"""
        return binascii.hexlify(self.private_key).decode('utf-8')

    def get_hex(self):
        """Convert private key to hexadecimal format"""
        return self.private_key.hex()

    def get_public_key(self):
        """Derive public key from private key"""
        return privkey_to_pubkey(self.private_key)

    def get_address(self):
        """Derive Bitcoin address from public key"""
        return pubkey_to_address(self.get_public_key())

    def to_dict(self):
        """Convert object to dictionary for serialization"""
        return {
            'private_key_hex': self.private_key_hex,
            'wif': self.wif,
            'btc_address': self.btc_address,
            'balance': self.balance
        }