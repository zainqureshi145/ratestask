from flask import Flask, request, jsonify
from db_util import get_db_connection, get_location_codes, calculate_average_prices

# init app
app = Flask(__name__)

# Define Endpoints
@app.route('/rates', methods=['GET'])
def get_rates():
    date_from = request.args.get('date_from', None)
    date_to = request.args.get('date_to', None)
    origin = request.args.get('origin', None)
    destination = request.args.get('destination', None)

# Get Location Codes
    orig_code = get_location_codes(origin)
    dest_code = get_location_codes(destination)
# Get Average Prices
    results = calculate_average_prices(orig_code, dest_code, date_from, date_to)
# Return Json Data
    return jsonify(results)


# run server
if __name__ == '__main__':
    app.run(debug=True)