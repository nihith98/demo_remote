import sys

def default():
    print('Hi')
    if sys.argv[1] == 'cat':
        print('Meow!')
    elif sys.argv[1] == 'dog':
        print('Woof!')
    elif sys.argv[1] == 'Cow':
        print('Moo!')

def main():
    default()

if __name__ == '__main__':
    main()
    print('End')