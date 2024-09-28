rom flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from models import PrivateKeyResult
from serializers import deserialize_json
from btc_utils import is_valid_address, recover_private_key, get_address_balance

app = Flask(__name__)
api = Api(app)

# Error handling
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request: Invalid input.'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Private key not found or invalid address.'}), 404)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal Server Error: Something went wrong.'}), 500)

class PrivateKeyAPI(Resource):
    def post(self):
        try:
            # Validate and deserialize input
            json_data = request.get_json(force=True)
            btc_address = deserialize_json(json_data).get('btc_address')
            
            if not btc_address or not is_valid_address(btc_address):
                return bad_request(None)

            # Simulated fuzzing and key recovery process (replace with actual implementation)
            private_key = recover_private_key(btc_address)

            if private_key:
                balance = get_address_balance(btc_address)
                result = PrivateKeyResult(private_key, btc_address, balance)
                return jsonify(result.to_dict()), 200
            else:
                return not_found(None)

        except Exception as e:
            app.logger.error(f"Internal Error: {e}")
            return internal_error(e)

# Endpoint to check the health of the API
class HealthCheck(Resource):
    def get(self):
        return jsonify({'status': 'OK'}), 200

api.add_resource(PrivateKeyAPI, '/find_private_key')
api.add_resource(HealthCheck, '/health')

if __name__ == '__main__':
    app.run(debug=True)