################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request
import unittest

QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    if price_b == 0:
        return
    return price_a / price_b


# Unit tests
class TestClient(unittest.TestCase):
    def testGetDataPoint(self):
        # Dummy quote data
        quote = {
            'stock': 'ABC',
            'top_bid': {'price': '147.53'},
            'top_ask': {'price': '145.92'}
        }
        expected_data_point = ('ABC', 147.53, 145.92, 146.725)
        self.assertEqual(getDataPoint(quote), expected_data_point)

    def testGetRatio(self):
        price_a = 12
        price_b = 6
        expected_ratio = 2.0
        self.assertEqual(getRatio(price_a, price_b), expected_ratio)

        # Test when price_b is zero
        price_a = 12
        price_b = 0
        self.assertIsNone(getRatio(price_a, price_b))

        # Test when price_a is zero
        price_a = 0
        price_b = 6
        expected_ratio = 0.0
        self.assertEqual(getRatio(price_a, price_b), expected_ratio)


# Main
if __name__ == "__main__":
    unittest.main()

    """ ----------- Update to get the ratio --------------- """
    prices = {}
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
        print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
