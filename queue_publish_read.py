import argparse
parser = argparse.ArgumentParser()
parser.add_argument("read",action="store_true")
args = parser.parse_args()
print(args.read)