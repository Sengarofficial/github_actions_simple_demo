from main import backwards_string, get_mode
import unittest
import os 



class TestMain(unittest.TestCase):

    def test_backwards_string(self):
        random_string = "This string needs to be tested"
        random_reversed_string = "detset eb ot sdeen gnirts siht"
        self.assertEqual(random_reversed_string, backwards_string(random_string))



    def test_get_env(self):
        self.assertEqual(os.environ.get("MODE"), get_mode())




if __name__ == "__main__":
    unittest.main()
    