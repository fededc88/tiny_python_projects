#! /usr/bin/env python3

import argparse

def read_args():
    parser = argparse.ArgumentParser(
            prog='gashlycrumb',
            description='Read a file, find the first letter of each line, build \
            a data structure that associates the letter to the line',
            epilog='This is the end of the help')

    parser.add_argument('letter', nargs='+', help='Letter(s)')
    parser.add_argument('-f', '--file',
            metavar='FILE',
            type=argparse.FileType('rt'),
            default='gashlycrumb.txt',
            help='Input file (default: gashlycrumb.txt)')
            

    return parser.parse_args()

def main():
    
    args = read_args()

    data = dict()

    # build a data structure that associate the letter to the line of text
    for line in args.file:
        #print(line)
        data[line[0].lower()] = line

    # print the lines
    for letter in args.letter:
        if letter.lower() in data:
            print(data[letter.lower()], end = '')
        else:
            print(f'I do not know "{letter}".')

if __name__ == '__main__':
    main()

