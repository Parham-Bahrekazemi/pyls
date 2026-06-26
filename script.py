
import argparse

from pathlib import Path

import datetime

parser = argparse.ArgumentParser(prog='ls' , description='Lists files a directory' , epilog='Thanks for using %(prog)s')

general = parser.add_argument_group('General options')

general.add_argument('path')

detailed = parser.add_argument_group('Detailed options')

detailed.add_argument('-l' , '--long' , action='store_true' , help='Lists files in long format')


args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print('Directory dose not exist') 
    raise SystemExit(1)


def build_output(entry , long = False):
    if long:
        size_in_mb = entry.stat().st_size / (1024 * 1024)
        time = datetime.datetime.fromtimestamp(entry.stat().st_mtime).strftime('%H:%M')
        return f'{size_in_mb:.2f} MB {time} {entry.name}'
    return entry.name

for entry in target_dir.iterdir():
    print(build_output(entry , long=args.long))
