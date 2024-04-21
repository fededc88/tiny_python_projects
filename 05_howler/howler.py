#! /usr/bin/env python3

import argparse
import os

import sys

def get_args():
    parser = argparse.ArgumentParser(
            prog='Howler.py',
            description='Howler (upper-cases input)')

    parser.add_argument('text', type=str, help='Inpyt string or file')
    parser.add_argument('-o', '--outfile',
            metavar='str', 
            dest='outfile',
            help='Output filename (default: ',
            default = '')

    return parser.parse_args()


def main():
    
    args = get_args()

    text = args.text
    of_path = args.outfile


    if os.path.isfile(text):
        #print('is file', text)
        in_file = open(text)
        out_text = in_file.read().upper()
        in_file.close()
    else:
       out_text = text.upper()

    if of_path != '':
        out_file = open(of_path, 'wt')
    else:
        out_file = sys.stdout

    print(out_text, file = out_file)

    if out_file != sys.stdout:
        out_file.close()



if __name__ == '__main__':
    main()
    



