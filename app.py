from flask import Flask, request, jsonify
from db_util import get_location_codes, calculate_average_prices
from dateutil.parser import parse
from werkzeug.exceptions import NotFound
from flask import abort

# Init app
app = Flask(__name__)

# Define endpoints
@app.route('/rates', methods=['GET'])
def get_rates():
    print("Hello World")
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    origin = request.args.get('origin')
    destination = request.args.get('destination')

    orig_code = get_location_codes(origin)
    dest_code = get_location_codes(destination)
# Get average prices
# Valid date formats YYYY-MM-DD, YY-MM-DD, MM-DD-YYYY, MM-DD-YY, DD-MM-YYYY, DD-MM-YY
    results = calculate_average_prices(orig_code, dest_code, parse(date_from), parse(date_to))
# Return json data
    return jsonify(results)


# Run server
if __name__ == '__main__':
    app.run(debug=True)