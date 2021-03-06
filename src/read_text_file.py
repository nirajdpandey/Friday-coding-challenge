__Author__ = 'Niraj Dev Pandey'
__Date__ = '23 December 2020'
__Purpose__ = 'This file will read text data and extract lines out of it'

# import dependencies
import yaml
import logging
import glob

# initialize logging
logging.basicConfig(filename='../logging.log',
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


class DataReader:
    def __init__(self, input_path):
        """
        Function read_text_file will accept one argument as text file path
        :param input_path: directory path to the text file
        :return: list of Lines of the provided text file
        """

        self.input_path = input_path
        self.content = []

    def reader(self):
        """
        reader function will use the path provided in init function
        and extract the data out of those files. You don't need to
        provide specific file path. Just the folder path will work.
        The glob package will automatically find all the text files from
        that provided folder path.
        :return: list of Lines of the provided text file
        """

        logger.info("loading text file to read")
        files = glob.glob(self.input_path + '*txt')  # Loading all the text file given folder
        print("Loaded file count is : ", len(files))
        for file in files:
            print("Loaded files are: ", file)
            # the [:] index is helpful in case you have just one input text file
            # this helps the loop not to throw any error
            with open(file[:], 'r', encoding='utf8') as f:
                self.content.append(f.readlines())  # append the lines to empty list
            logger.info("Loaded text file successfully!")
            logger.info("process finished!")
        return self.content  # Return all the extracted content in a python list
