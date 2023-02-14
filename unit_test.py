import unittest
import temperature


class TestAboveFreezing(unittest.TestCase):
    """temperature.above_freezing 테스트한다."""

    def test_above_freezing_above(self):
        expected = True
        actual = temperature.above_freezing(5.2)
        self.assertEqual(expected, actual, "The temperature is above freezing.")

    def test_above_freezing_above(self):
        expected = False
        actual = temperature.above_freezing(-2)
        self.assertEqual(expected, actual, "The terperature is below freezing.")

    def test_above_freezing_above(self):
        expected = False
        actual = temperature.above_freezing(0)
        self.assertEqual(expected, actual, "The temperature is at the freezing mark.")


if __name__ == "__main__":

    unittest.main()
