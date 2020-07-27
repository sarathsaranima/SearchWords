import os
import logging

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


class ReadValidate(object):
    """
    A class to maintain read and validation methods for input
    """
    input_text_file = ''
    key_word = ''
    search_text = ''

    def __init__(self, input_file):
        self.input_text_file = input_file

    def read_input_text_file(self):
        """
        A method to read and validate the input text file path
        :return: string containing the text to be searched.
        """
        try:
            assert os.path.exists(self.input_text_file)
            fr = open(self.input_text_file, 'r')
            text = fr.read()
            fr.close()
            logging.debug("Text :" + text)
            self.search_text = text.lower()
            return self.search_text
        except AssertionError:
            raise AssertionError("No file in this path : " + str(self.input_text_file))

    def validate_text(self):
        """
        Validate the number of lines in a text
        :return: boolean
        """
        logging.debug("No of lines in the text: " + str(self.search_text.count("\n")+1))
        if self.search_text.count("\n") == 199:
            logging.info("Input Successfully Validated..")
            return True
        else:
            raise ValueError('Invalid Input: Input text not of 200 lines')

    def get_the_keyword(self):
        """
        Get the keyword from user
        :return: string with search keyword
        """
        search_key = str(input("Enter the keyword to search in text:"))
        self.key_word = search_key.lower()
        return self.key_word
