#!/usr/bin/env python
from __future__ import print_function

import sys
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('qif_file', help='QIF file to clean up')
    # TODO: parser.add_argument('-i', '--inplace', help='Modify the file in place')
    # TODO: parser.add_argument('-o', '--output', help='Optional file to write to, else stdout')
    return parser.parse_args()


def clean_line(line):
    """

    :param str line:
    :return:
    :rtype str
    """
    if not line.startswith('P') or ',' not in line:
        return line.strip()

    try:
        s1 = line.split(',')[2].strip()
        return 'P' + (s1.split(',')[0] if ',' in s1 else s1)
    except IndexError:
        print('ERROR on "' + line + '"', file=sys.stderr)
        raise Exception('Not expected format: {}'.format(line))


def main():
    args = parse_args()

    with open(args.qif_file, 'r') as qiffile:
        for line in qiffile:
            print(clean_line(line))


def old():
    filepath_to_clean = sys.argv[1]

    qiffile = open(filepath_to_clean)

    for line in qiffile:
        cleaned_line = ''
        if line.startswith('P'):

            try:
                if line.startswith('PDD PAYMENT RECEIVED'):
                    cleaned_line = line.split(',')[0].strip()
                elif line.startswith('PPURCHASE'):
                    s1 = line.split(',')[2].strip()
                    cleaned_line = s1.split(',')[0] if ',' in s1 else s1
            except IndexError:
                print('ERROR on "' + line.strip() + '"', file=sys.stderr)
                raise Exception('Not expected format: PPURCHASE - DOMESTIC, PLYMOUTH, SUBWAY, GBP 10.99')
            print('P' + cleaned_line)
        else:
            print(line.strip())
