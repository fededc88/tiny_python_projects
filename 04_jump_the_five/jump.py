#! /usr/bin/env python3

import argparse

def get_args():

    parser = argparse.ArgumentParser(
            prog='jumpy',
            description='The program decode a phone number',
            epilog='This is an epilog')

    parser.add_argument('str', 
            help='Text to decode',
            type=str)

    return parser.parse_args()

def main():
    # Read program input arguments
    args = get_args()

    text = args.str
    
    jumper ={
            '1':'9',
            '2':'8',
            '3':'7',
            '4':'6',
            '5':'0',
            '6':'4',
            '7':'3',
            '8':'2',
            '9':'1',
            '0':'5'}

    for char in text:
        print(jumper.get(char, char), end='')

    print()

if __name__ == '__main__':
    main()


