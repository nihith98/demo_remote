import sys

def default():
    print('Hi')
    if sys.argv[1] == 'cat':
        print('Meow')
    elif sys.argv[1] == 'dog':
        print('Woof')

def main():
    default()

if __name__ == '__main__':
    main()