import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Create databse connection
def get_db_connection():
    try:
        connection = psycopg2.connect(
        host='localhost',
        database='rates',
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )

    except Exception as error:
        print(error)

    return connection
       

# Get location codes
def get_location_codes(location):
    try:
        connection = get_db_connection()
        cur = connection.cursor()
        params = (location,)
        cur.execute(f'''
        SELECT ports.code
        FROM ports
        JOIN regions
        ON regions.slug = ports.parent_slug
        WHERE regions.parent_slug = '{location}' OR ports.code = '{location}' OR ports.parent_slug = '{location}';
        ''', params)
    
        code = cur.fetchone()

    except Exception as error:
        print(error)

    return code

# Calculate average prices
def calculate_average_prices(orig_code, dest_code, date_from, date_to):
    try:
        connection = get_db_connection()
        cur = connection.cursor(cursor_factory=RealDictCursor)

        params = (orig_code, dest_code, date_from, date_to,)

        # Execute raw query
        cur.execute(f'''
            SELECT prices.day,
            
            CASE
                WHEN COUNT(prices.price) >= 3 THEN ROUND(AVG(prices.price), 0)
                WHEN COUNT(prices.price) < 3 THEN NULL
            END AS average_price

            FROM

            (SELECT *
            FROM regions
            INNER JOIN ports
            ON regions.parent_slug = ports.parent_slug) AS result

            FULL OUTER JOIN prices
            ON prices.orig_code = result.code
            WHERE prices.orig_code = (%s) AND prices.dest_code = (%s) AND day BETWEEN (%s) AND (%s)
            GROUP BY prices.day;
            ''', params)

        results = cur.fetchall()

        # Format the result in given format of API
        for result in results:
            result['day'] = str(result['day'])
            result['average_price'] = int(result['average_price']) if result['average_price'] is not None else None
        
        # Close cursor and connection after execution
        cur.close()
        connection.close()

    except Exception as error:
        print(error)
    
    return results