from logging import Logger
import sys


logger = Logger()
test = 'Test'

if __name__ == '__main__':
    Logger.info(test)
    logger.info(sys[0])