import unittest
import strmquiz.quiz_builder as quiz_builder

class MyTestCase(unittest.TestCase):
    def __init__(self):
        configfile = ""
        outformat = ""
        self.tester = quiz_builder.QuizBuilder(outformat, config_file=configfile)

        new_test = tester.get_test(test_id)

    def test_base(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
