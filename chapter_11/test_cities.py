import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_coutry(self):
        ans = city_country('goiânia', 'brazil')
        self.assertEqual(ans, 'Goiânia, Brazil')

    def test_city_country_population(self):
        ans = city_country('goiânia', 'brazil', 7_206_589)
        self.assertEqual(ans, 'Goiânia, Brazil - population 7206589')

if __name__ == '__main__':
    unittest.main()