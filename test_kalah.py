import unittest
from kalha import Kalha

class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Kalha(6, 4)

    def tearDown(self):
        pass

    def test_status(self):
        self.assertEqual(self.game.status(),(4,4,4,4,4,4,0,4,4,4,4,4,4,0))

if __name__ == '__main__':
    unittest.main()
