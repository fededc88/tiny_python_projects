#! /usr/bin/env python3

import argparse
import os

import sys

def get_args():
    """ Get command-line arguments"""

    parser = argparse.ArgumentParser(
            prog='Howler.py',
            description='Howler (upper-cases input)')

    parser.add_argument('text',
            metavar='text',
            type=str,
            help='Inpyt string or file')

    parser.add_argument('-o', '--outfile',
            metavar='str', 
            dest='outfile',
            help='Output filename (default: ',
            default = '')

    return parser.parse_args()


def main():
    """ program entry point """
    
    args = get_args()

    text = args.text
    of_path = args.outfile

    out_text = open(text).read().rstrip() if os.path.isfile(text) else text

    out_file = open(of_path, 'wt') if of_path else sys.stdout

    print(out_text.upper(), file = out_file)

if __name__ == '__main__':
    main()
    



