import argparse
import sys
import cli.cipher
import cli.analysis

parser = argparse.ArgumentParser()

input_group = parser.add_mutually_exclusive_group()

input_group.add_argument('-i', dest='input', help='Text input')
input_group.add_argument('-f', dest='filename', help='File input')

subparsers = parser.add_subparsers()

cli.cipher.create_parsers(subparsers)
cli.analysis.create_parsers(subparsers)

result = parser.parse_args()


if 'func' not in result:
    parser.print_help()
    sys.exit(0)

src = ''

if result.filename is not None:
    with open(result.filename) as f:
        src = f.read()
elif result.input is not None:
    src = result.input
else:
    src = sys.stdin.read()

result.func(result, src, sys.stderr, sys.stdout)

sys.stdin.close()
sys.stdout.close()
sys.stderr.write('\n')
sys.stderr.close()
