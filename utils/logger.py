import sys
import logging


class Logger:
    def __init__(self, log_file_path: str):

        self.formatter = logging.Formatter("%(asctime)s — %(name)s - %(name)s — %(levelname)s — %(message)s")
        self.log_file = log_file_path
        self.log_level = logging.DEBUG

    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def get_file_handler(self):

        file_handler = logging.FileHandler(filename=self.log_file)
        file_handler.setFormatter(self.formatter)
        return file_handler

    def get_logger(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(self.log_level)
        logger.addHandler(self.get_console_handler())
        logger.addHandler(self.get_file_handler())
        logger.propagate = True
        return logger

