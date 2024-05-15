import unittest
import strm_test.test_builder as test_builder

class MyTestCase(unittest.TestCase):
    def __init__(self):
        configfile = ""
        outformat = ""
        self.tester = test_builder.test_builder(outformat, config_file=configfile)

        new_test = tester.get_test(test_id)

    def test_base(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
