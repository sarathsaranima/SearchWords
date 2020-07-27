import logging

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


class SearchWord(object):
    """
    Class that contains methods to search a keyword in a search text.
    """
    search_text = ''
    key_word = ''
    match_count = 0

    def __init__(self, key, search):
        self.key_word = key
        self.search_text = search

    def match_keyword(self):
        """
        A method to get the count of matches of keyword in a text
        :return: match_count : number of items matched
        """
        index = 0
        while True:
            index = self.search_text.find(self.key_word, index)
            if index == -1:
                return self.match_count if self.match_count == 0 else self.match_count - 1
            self.match_count += 1
            index += 1

    def write_to_csv(self, output_csv):
        """
        A method to write matches to CSV
        :param output_csv: output csv file
        :return: None
        """
        with open(output_csv, "w") as csv_file:
            for _ in range(self.match_count):
                csv_file.write(self.key_word)
                csv_file.write('\n')
        logging.debug("Successfully generated output file {}".format(output_csv))
        csv_file.close()







