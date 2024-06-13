#! /usr/bin/env python3

import argparse
import os
import random 


def get_args():
    parser = argparse.ArgumentParser(
            prog='ransom.py',
            description='Ransom Note')

    parser.add_argument('text',
            metavar='text',
            help='Input text or file',
            type=str)
    parser.add_argument('-s', '--seed',
            metavar='int',
            help='Random seed (default: None)',
            type=int,
            default=None)

    args = parser.parse_args()

    args.text = open(args.text).read().strip() if os.path.isfile(args.text) else args.text  

    return args

def choose(char):
    
    return char.upper() if random.choice([False, True]) else char.lower()

def main():
    args = get_args()

    random.seed(args.seed)

    new_text = []
    for letter in args.text:
        new_text.append(choose(letter))

    print(''.join(new_text))

if __name__ == '__main__':
    main()


