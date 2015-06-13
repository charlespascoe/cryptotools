import argparse
import sys
import cli.cipher
import cli.analysis

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers()

cli.cipher.create_parsers(subparsers)
cli.analysis.create_parsers(subparsers)

result = parser.parse_args()

if 'func' not in result:
    parser.print_help()
    sys.exit(0)

result.func(result, sys.stdin, sys.stderr, sys.stdout)

sys.stdin.close()
sys.stdout.close()
sys.stderr.write('\n')
sys.stderr.close()
