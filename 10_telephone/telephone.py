#! /usr/bin/env python3

import argparse
import os
import random

import string

def get_args():
    parser = argparse.ArgumentParser(
            prog='telephone.py',
            description='Telephone')

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-s', '--seed',
            metavar='seed',
            help='Random seed (default:None)',
            default=None,
            type=int)

    parser.add_argument('-m', '--mutations',
            metavar='mutations',
            help='Percent mutations (default: 0.1)',
            default=0.1,
            type=float)

    args = parser.parse_args()

    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    args.text = open(args.text).read().strip() if os.path.isfile(args.text) else args.text

    return args

def main():
    args = get_args()

    random.seed(args.seed)

    nmut = round(len(args.text) * args.mutations)

    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    new_text = args.text

    for i in random.sample(range(len(args.text)), nmut):
        new_char = random.choice(alpha.replace(new_text[i], ''))
        new_text = new_text[:i] + new_char + new_text[i+1:]

    print(f'You said: "{args.text}"')
    print(f'I heard : "{new_text}"')



if __name__ == '__main__':
    main()
