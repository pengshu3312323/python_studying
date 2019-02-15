#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import getopt

from grpc_tools import protoc


def gencode(protoc_file):
    protoc.main(
        '-I./',
        '--python_out=.',
        '--grpc_python_out=.',
        './{}'.format(protoc_file)
    )


if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], 'hf:', ['help', 'file:'])
    protoc_file = ''
    for opt, val in opts:
        if opt in ('-h', '--help'):
            print('-f $PROTCO_FILE or --file $PROTOC_FILE')
        if opt in ('-f', '--file'):
            protoc_file = val

    if not protoc_file:
        print('-f $PROTCO_FILE or --file $PROTOC_FILE')
    else:
        gencode(protoc_file)
