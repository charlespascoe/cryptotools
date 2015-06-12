import argparse
import sys
import cli.cipher

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers()

cli.cipher.create_parsers(subparsers)

analysis_parser = subparsers.add_parser('analysis', help='Various analysis tools').add_subparsers(help='Wut?')

result = parser.parse_args()

if 'func' not in result:
    parser.print_help()
    sys.exit(0)

result.func(sys.stdin, result, sys.stdout)

sys.stdin.close()
sys.stdout.close()
sys.stderr.write('\n')
sys.stderr.close()
