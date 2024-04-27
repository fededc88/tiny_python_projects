#! /usr/bin/env python3
import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(
            prog='wc',
            description='Emulate wc (word count)')

    parser.add_argument('file',
            metavar='FILE',
            type=argparse.FileType('rt'),
            default=[sys.stdin],
            help='Input file(s)',
            nargs='*')

    return parser.parse_args()

def main():

    args = get_args()

    files = args.file

    #print(type(files))

    total_lines = 0
    total_words = 0
    total_bytes = 0

    for fh in files:
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in fh:
            num_lines += 1

            #words = line.split()
            for word in line.split():
                num_words +=1

            num_bytes += len(line)
        total_lines +=num_lines
        total_words +=num_words
        total_bytes +=num_bytes
            
        print('{:8}{:8}{:8} {}'.format(num_lines, num_words, num_bytes, fh.name ))

    if len(files) > 1:
        print('{:8}{:8}{:8} {}'.format(total_lines, total_words, total_bytes, 'total'))

if __name__ == '__main__':
    main()
