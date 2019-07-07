#!/usr/bin/env python
from __future__ import print_function

import argparse
import re
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('qif_file', help='QIF file to clean up')
    # TODO: parser.add_argument('-i', '--inplace', help='Modify the file in place')
    # TODO: parser.add_argument('-o', '--output', help='Optional file to write to, else stdout')
    return parser.parse_args()


line_pattern = re.compile(r', \d+\.\d+$')


def clean_line(line):
    """
    :param str line: The line to clean
    :return: The cleaned line, ready for output
    :rtype str
    """
    if not line.startswith('P') or ',' not in line:
        return line.strip()

    try:
        if line_pattern.search(line):  # One source requires a different approach to another
            # TODO: Examples of what matches would be helpful when coming back to this code...
            cleaned_line = line.strip().rsplit(',', 1)[0]
            if cleaned_line.startswith('PCASH WITHDRAWAL') or cleaned_line.startswith('PCARD PAYMENT'):
                cleaned_line = cleaned_line.rsplit(',', 2)[0]
            return cleaned_line
        else:
            comma_count = line.count(',')
            if comma_count == 1:  # 'PDD PAYMENT RECEIVED  D/DEBIT, GBP -12.34'
                s1 = line.split(',')[0].strip()
                s1 = s1[1:]  # remove leading P, it's added back on the return statement
            else:
                s1 = line.split(',')[2].strip()
            return 'P' + (s1.split(',')[0] if ',' in s1 else s1)
    except IndexError:
        print('ERROR on "' + line + '"', file=sys.stderr)
        raise Exception('Not expected format: "{}"'.format(line))


def main():
    args = parse_args()

    with open(args.qif_file, 'r') as qiffile:
        for line in qiffile:
            print(clean_line(line))
