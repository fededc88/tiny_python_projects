#! /usr/bin/env python3

import argparse
import random

def get_args():
    
    parser = argparse.ArgumentParser(
            prog='abuse.py',
            description='Heap abuse')

    parser.add_argument('-a', '--adjectives',
            metavar='adjectives',
            help='Number of adjectives (default: 2)',
            default=2,
            type=int)

    parser.add_argument('-n', '--number',
            metavar='insults',
            help='Number of insults (default: 3)',
            default=3,
            type=int)

    parser.add_argument('-s', '--seed',
            metavar='seed',
            help='Random seed (default: None)',
            default=None,
            type=int)

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args

def main():
    args = get_args()

    random.seed(args.seed)

    print(random.randint(0,1000))


if __name__ == '__main__':
    main()
