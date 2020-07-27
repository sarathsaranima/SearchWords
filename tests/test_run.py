import logging
import sys
import unittest

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


class LoremTestCase(unittest.TestCase):
    """
    A class to test the test cases of keyword search in lorem ipsum text
    """

    def test_match_keyword(self):
        """
        Test case for testing match keyword
        """
        sys.path.insert(0, "../")
        import search_word
        import input
        input_obj = input.ReadValidate("unit_text_file.txt")
        check_text = input_obj.read_input_text_file()
        word_obj = search_word.SearchWord("lorem", check_text)
        word_obj.match_keyword()
        logging.debug("unit test match_count: {}".format(word_obj.match_count))
        self.assertEqual(word_obj.match_count, 10)

    def test_write_to_csv(self):
        """
        Test case for testing writing to csv file
        """
        sys.path.insert(0, "../")
        import search_word
        word_obj = search_word.SearchWord('lorem', 'loremipsum')
        word_obj.match_keyword()
        word_obj.write_to_csv("expected_key_count.csv")
        with open('key_count.csv', 'r') as actual, open('expected_key_count.csv', 'r') as expected:
            file_actual = actual.readlines()
            file_expected = expected.readlines()
            logging.debug("file_actual : {}".format(file_actual))
            logging.debug("file_expected : {}".format(file_expected))
        self.assertListEqual(file_actual, file_expected)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
