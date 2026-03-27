import unittest
from weather import get_weather
from stylist import suggest_outfit

class TestStylistBot(unittest.TestCase):
    def test_suggest_outfit_cold(self):
        weather = 'cold'
        outfit = suggest_outfit(weather)
        self.assertEqual(outfit['top'], 'Sweater')
        self.assertEqual(outfit['bottom'], 'Jeans')
        self.assertEqual(outfit['shoes'], 'Boots')
        self.assertEqual(outfit['jacket'], 'Puffer Jacket')

    def test_suggest_outfit_warm(self):
        weather = 'warm'
        outfit = suggest_outfit(weather)
        self.assertEqual(outfit['top'], 'T-shirt')
        self.assertEqual(outfit['bottom'], 'Chinos')
        self.assertEqual(outfit['shoes'], 'Sneakers')
        self.assertEqual(outfit['jacket'], 'Light Jacket')

    def test_suggest_outfit_hot(self):
        weather = 'hot'
        outfit = suggest_outfit(weather)
        self.assertEqual(outfit['top'], 'Tank Top')
        self.assertEqual(outfit['bottom'], 'Shorts')
        self.assertEqual(outfit['shoes'], 'Sandals')
        self.assertEqual(outfit['jacket'], 'No Jacket')

    def test_suggest_outfit_rainy(self):
        weather = 'rainy'
        outfit = suggest_outfit(weather)
        self.assertEqual(outfit['top'], 'Long Sleeve Shirt')
        self.assertEqual(outfit['bottom'], 'Jeans')
        self.assertEqual(outfit['shoes'], 'Waterproof Boots')
        self.assertEqual(outfit['jacket'], 'Raincoat')

if __name__ == '__main__':
    unittest.main()
