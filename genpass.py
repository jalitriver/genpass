'''Simple Python3 program used to generate suitable passwords.'''

import argparse
import random
import sys

# The character set from which passwords are generated.
_charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def genpassword(nchars):
    '''Return a password of length nchars where each character is randomly
    generated.'''

    return "".join([random.choice(_charset) for x in range(nchars)])

def genpasswords(nwords, nchars):
    '''Return a list holding nwords passwords where each password has
    nchars randomly generated characters.'''

    return [genpassword(nchars) for x in range(nwords)]

def main():
    '''Main entry point into this module when it is invoked as a program.'''

    # Parse command-line arguments.
    parser = argparse.ArgumentParser(description='Generate Passwords')
    parser.add_argument(
        dest='nchars',
        type=int,
        nargs='?',
        default=16,
        help='number of characters in each password')
    parser.add_argument(
        dest='nwords',
        type=int,
        nargs='?',
        default=1,
        help='number of passwords to generate')
    args = parser.parse_args()

    # Check for errors in the command-line arguments.
    if args.nchars < 16:
        raise(Exception('Refusing to generate weak passwords.'))
    if args.nwords < 1:
        raise(Exception('At least one password must be generated.'))

    # Generate the passwords.
    for password in genpasswords(args.nwords, args.nchars):
        print(password)

# Only invoke main() automatically if this Python module is loaded as
# a program (instead of as a library).
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        sys.stderr.write('*** Error: %s\n' % (e,))
