import sys

def default():
    print('Hello world')
    if sys.argv[1] == 'cat':
        print('Meow!')
    elif sys.argv[1] == 'dog':
        print('Woof!')
    elif sys.argv[1] == 'Cow':
        print('Moo!')

def main():
    print('This is main')
    default()

if __name__ == '__main__':
    main()
    print('Program Ended')