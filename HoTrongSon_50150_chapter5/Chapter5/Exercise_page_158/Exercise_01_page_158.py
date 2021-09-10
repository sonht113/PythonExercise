"""
Author: Ho Trong Son
Date: 18/08/2021
Program: Exercise_01_page_158.py
Problem:
    1.  Give three examples of real-world objects that behave like a dictionary.
Solution:
    Result:
        Date: 2020-02-18
        Close price: 200.0

        Date: 2020-02-19
        Close price: 201.0

        Date: 2020-02-20
        Close price: 202.0

"""

price_history = [
    {"ticker": "AAPL", "close price": 200.00, "daily high": 180.0, "daily low": 147.0, "volume": 2000000, "date": "2020-02-18"},
    {"ticker": "AAPL", "close price": 201.00, "daily high": 178.0, "daily low": 146.0, "volume": 2000000, "date": "2020-02-19"},
    {"ticker": "AAPL", "close price": 202.00, "daily high": 179.0, "daily low": 149.0, "volume": 2000000, "date": "2020-02-20"}]

for dict in price_history:
    print("Date: %s" % dict['date'])
    print("Close price: %s" % dict['close price'], '\n')

