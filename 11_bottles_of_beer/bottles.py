#! /usr/bin/env python3 

import argparse

def get_args():
    parser = argparse.ArgumentParser(
            prog='bottles.py',
            description='Bottles of beer song')

    parser.add_argument('-n', '--num',
            metavar='number',
            help='How many bottles (default: 10)',
            default=10,
            type=int)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args

def verse(bottles):

    next_bottle = bottles -1 if bottles > 1 else 0

    s1 = '' if bottles == 1 else 's'
    s2 = 'No more'  if bottles == 1 else f'{next_bottle}'
    s3 = '' if next_bottle == 1 else 's'
    s4 = '\n' if next_bottle >  0 else ''

    return '\n'.join([
        f'{bottles} bottle{s1} of beer on the wall,',
        f'{bottles} bottle{s1} of beer,',
        'Take one down, pass it around,',
        f'{s2} bottle{s3} of beer on the wall!{s4}'])

def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,',
        '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'])
    

    last_verse = verse(2)
    assert last_verse == '\n'.join([
        '2 bottles of beer on the wall,',
        '2 bottles of beer,',
        'Take one down, pass it around,',
        '1 bottle of beer on the wall!'])

def main():

    args = get_args()

    print('\n'.join(map(verse, range(args.num, 0, -1))))

if __name__ == '__main__':
    main()
