from logging import Logger
import sys


logger = Logger('logger')
test = 'Test'

if __name__ == '__main__':
    logger.info(test)
    logger.info(f'logger: {sys.argv[1]}')
