import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Arrange
    expected_abc = ('ABC',120.48,121.2,120.84)
    expected_def = ('DEF',117.87,121.68,119.775)
    # Act and assert
    self.assertEqual(getDataPoint(quotes[0]),expected_abc)
    self.assertEqual(getDataPoint(quotes[1]),expected_def)
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Arrange
    expected_abc = ('ABC', 120.48, 121.2, 120.84)
    expected_def = ('DEF', 117.87, 121.68, 119.775)
    # Act and assert
    self.assertEqual(getDataPoint(quotes[0]), expected_abc)
    self.assertEqual(getDataPoint(quotes[1]), expected_def)


  """ ------------ Add more unit tests ------------ """

if __name__ == '__main__':
    unittest.main()
