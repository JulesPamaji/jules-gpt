import hashlib
from ecdsa import SigningKey, VerifyingKey
from ecdsa.util import sigdecode_der
from bitcoin import privkey_to_pubkey, pubkey_to_address, address_to_hash160

def is_valid_address(address):
    try:
        # Check if the address can be converted to a hash160
        hash160 = address_to_hash160(address)
        return True
    except Exception as e:
        return False

def get_address_from_key(private_key):
    public_key = privkey_to_pubkey(private_key)
    return pubkey_to_address(public_key)

def validate_address(address):
    return is_valid_address(address)

def get_balance(address, blockchain_api):
    # Fetch balance from blockchain API
    response = blockchain_api.get_balance(address)
    return response['balance']

def sign_message(message, private_key):
    signing_key = SigningKey.from_string(private_key, curve=SigningKey.from_string.SECP256k1)
    signature = signing_key.sign_deterministic(message.encode(), sigencode=sigencode_der)
    return signature

def verify_signature(message, signature, public_key):
    verifying_key = VerifyingKey.from_string(public_key, curve=VerifyingKey.from_string.SECP256k1)
    return verifying_key.verify(signature, message.encode())

def get_public_key_from_private(private_key):
    return privkey_to_pubkey(private_key)

def get_hash160_from_address(address):
    return address_to_hash160(address)

def get_address_from_hash160(hash160):
    return pubkey_to_address(hash160)

def get_address_from_pubkey(public_key):
    return pubkey_to_address(public_key)

def hash_message(message):
    return hashlib.sha256(message.encode()).hexdigest()