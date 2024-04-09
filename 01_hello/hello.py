#!/usr/bin/env python3
# Purpose: Say Hello

import argparse

parser = argparse.ArgumentParser(prog='Hello World', 
                                 description='Say hello to my litle frient',
                                 epilog='Text at the bottom of the help')

parser.add_argument('-n', '--name', metavar='name',default='World', help='Name to greet')

args = parser.parse_args()

print('Hello, ' + args.name + '!')

