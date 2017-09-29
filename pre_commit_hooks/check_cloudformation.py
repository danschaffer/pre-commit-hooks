from __future__ import print_function

import argparse
import re
import sys

try:
    from yaml.cyaml import CSafeLoader as Loader
except ImportError:  # pragma: no cover (no libyaml-dev / pypy)
    Loader = yaml.SafeLoader


def check_cloudformation(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Yaml filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        contents = open(filename).read()
        if re.search('Fn::Join') or re.search('!Join'):
            print("Found usage of Join, please use !Sub instead.")
            retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(check_yaml())
