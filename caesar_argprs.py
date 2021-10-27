import argparse
from caesar import caesar


parser = argparse.ArgumentParser(description='Сдвиг по алфавиту')
parser.add_argument('text', type=str,
                    help='Строка для зашифровки')
parser.add_argument('-sh', '--shift', dest='shift', default=0, type=int,
                    help='Сдвиг по алфавиту')
args = parser.parse_args()

print(f'Результат: {caesar(args.text, args.shift)}')