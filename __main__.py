#! /usr/bin/python3

import argparse
import spaceshipnamegenerator as sng

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'N', nargs='?', default=1, metavar='N', type=int,
        help="The number of ship names to generate"
    )
    parser.add_argument(
        "-p", "--prefix", nargs='?', default="",
        help="prefix the ship names"
    )
    args = parser.parse_args()
    names_str = sng.gen_num(args.N, args.prefix)
    if (names_str[-1] == "\n"): names_str=names_str[:-1]
    print(names_str)
