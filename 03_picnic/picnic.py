#!/usr/bin/env python3
"""
Author : fededc88 <fededc88@localhost>
Date   : 2024-04-19
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Item(s) to bring',
                        type=str,
                        nargs='+')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items (default:False)',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.str
    flag_sort = args.sorted

    if flag_sort:
        str_arg.sort()

    str_length = len(str_arg)

    if str_length == 1:
        str_out = str_arg[0]

    elif str_length == 2:
        str_out = ' and '.join(str_arg)

    elif str_length > 2:
        str_out = ', '.join(str_arg[0:-1])
        str_out = str_out +', and '+ str_arg[-1]


    print('You are bringing {}.'.format(str_out))

# --------------------------------------------------
if __name__ == '__main__':
    main()
