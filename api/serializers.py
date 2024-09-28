import json
from models import PrivateKeyResult

def serialize_private_key_result(private_key_result):
    """Serialize PrivateKeyResult object to JSON"""
    return json.dumps(private_key_result.to_dict(), indent=4)

def deserialize_json(json_data):
    """Deserialize JSON data to a PrivateKeyResult object"""
    data = json.loads(json_data)
    return PrivateKeyResult(**data)

def convert_hex_to_private_key(hex_key):
    """Convert hexadecimal private key to bytes"""
    return bytes.fromhex(hex_key)

def convert_wif_to_private_key(wif_key):
    """Convert WIF private key to bytes"""
    # Remove WIF prefix and suffix, and convert back to bytes
    wif_prefix = "5H"  # Example WIF prefix
    wif_suffix = "cUe"  # Example WIF suffix
    if wif_key.startswith(wif_prefix) and wif_key.endswith(wif_suffix):
        key_without_prefix = wif_key[len(wif_prefix):-len(wif_suffix)]
        return bytes.fromhex(key_without_prefix)
    return None

# Dynamic usage:
# Assuming private_key_result is a dynamically generated PrivateKeyResult object
serialized_result = serialize_private_key_result(private_key_result)

# Deserialize the JSON and access the private key in hex and WIF formats
deserialized_result = deserialize_json(serialized_result)
hex_key = deserialized_result.private_key_hex
wif_key = deserialized_result.wif

# Dynamic usage:
# Assuming private_key_result is a dynamically generated PrivateKeyResult object
serialized_result = serialize_private_key_result(private_key_result)

# Deserialize the JSON and access the private key in hex and WIF formats
deserialized_result = deserialize_json(serialized_result)
hex_key = deserialized_result.private_key_hex
wif_key = deserialized_result.wif

# Perform further processing or operations

# Validate the WIF private key
if convert_wif_to_private_key(wif_key) is None:
    print("Invalid WIF private key format.")
else:
    print("WIF private key is valid.")

# Get the Bitcoin address from the private key
address = get_address_from_private_key(wif_key)

# Fetch the balance for the Bitcoin address
balance = get_balance_for_address(address)

# Display the results
print(f"Private Key (Hex): {hex_key}")
print(f"Private Key (WIF): {wif_key}")
print(f"Bitcoin Address: {address}")
print(f"Balance: {balance} BTC")