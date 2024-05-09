#! /usr/bin/env python3

import argparse
import random

adj = """bankrupt base caterwauling corrupt cullionly detestable dishonest false
filthsome filthy foolish foul gross heedless indistinguishable infected insatiate
irksome lascivious lecherous loathsome lubbery old peevish rsacaly rotten
ruinous scurilous scurvy slanderous sodden-witted thin-faced toad-spotted
unmannered vile wall-eyed""".strip().split()

assert len(adj) == 36

nouns = """Judas Satan ape ass barbermonger beggar blsck boy braggart butt
carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool gull harpy
jack jolthead knave liar lunatic maw milsop minion ratcatcher recreant togue
scold slave swine traitor varlet villain worm""".strip().split()

assert len(nouns) == 39

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

    for i in range(args.number):
        #print('You {} {}!'.format(', '.join(random.choices(adj, k = args.adjectives)), random.choice(nouns))) 
        print('You ' + ', '.join(random.sample(adj, k = args.adjectives)) + ' ' + random.choice(nouns) + '!') 

if __name__ == '__main__':
    main()
