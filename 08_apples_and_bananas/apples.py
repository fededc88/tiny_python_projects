#! /usr/bin/env python3

import argparse
import os

vowels=['a', 'e', 'i', 'o', 'u']

def get_args():
    parser = argparse.ArgumentParser(
            prog='apples.py',
            description='Apples and Bannanas')

    parser.add_argument('text',
            metavar='text',
            help='Input text or file')
    parser.add_argument('-v', '--vowel',
            metavar='vowel',
            choices= vowels,
            default='a',
            help='The vowel to substitute (default: a)')

    return parser.parse_args()

def replace_text(text, new_vowel):

        for vowel in vowels:
            text = text.replace(vowel, new_vowel)  

        for vowel in vowels:
            text = text.replace(vowel.upper(), new_vowel.upper())  

        return text

def main():


    args = get_args()

    new_vowel = args.vowel
    text = args.text

    text = open(text).read().rstrip() if os.path.isfile(text) else text
    
    print(replace_text(text, new_vowel))


if __name__ == '__main__':
    main()

