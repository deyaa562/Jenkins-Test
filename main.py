from logging import Logger
import sys


logger = Logger('logger')
test = 'Test'
test = sys.argv[1]

if __name__ == '__main__':
    print(test)
    print(f'logger: {sys.argv[1]}')
    print(f'logger: {(int(sys.argv[2]) + 1)}')
    print(f'logger: {(int(sys.argv[3]) + 4)}')
    print(sys.argv[1])
