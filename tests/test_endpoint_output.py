from unittest import result
from requests import get

# Check the status code with valid parameters

def test_region_1():
    result = get(
        "http://localhost:5000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
    )

    assert result.status_code == 200
    assert result.json() == [
    {
        "average_price": 882,
        "day": "2016-01-01"
    },
    {
        "average_price": 882,
        "day": "2016-01-02"
    },
    {
        "average_price": 882,
        "day": "2016-01-05"
    },
    {
        "average_price": 882,
        "day": "2016-01-06"
    },
    {
        "average_price": 882,
        "day": "2016-01-07"
    },
    {
        "average_price": 832,
        "day": "2016-01-08"
    },
    {
        "average_price": 832,
        "day": "2016-01-09"
    },
    {
        "average_price": 832,
        "day": "2016-01-10"
    }
]

def test_region_2():
    result = get(
        "http://localhost:5000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=china_main&destination=uk_main"
    )

    assert result.status_code == 200
    assert result.json() == [
    {
        "average_price": 1104,
        "day": "2016-01-01"
    },
    {
        "average_price": 1104,
        "day": "2016-01-02"
    },
    {
        "average_price": 1103,
        "day": "2016-01-05"
    },
    {
        "average_price": 1103,
        "day": "2016-01-06"
    },
    {
        "average_price": 1103,
        "day": "2016-01-07"
    },
    {
        "average_price": 1103,
        "day": "2016-01-08"
    },
    {
        "average_price": 1103,
        "day": "2016-01-09"
    },
    {
        "average_price": 1103,
        "day": "2016-01-10"
    }
]