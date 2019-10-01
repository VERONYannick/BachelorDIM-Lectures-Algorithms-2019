import argparse
import os
import simple_queue_publish as qp
import simple_queue_read as qr

parser = argparse.ArgumentParser()
parser.add_argument("-read",action="store_true")
parser.add_argument("-msg")
args = parser.parse_args()
print(args)

if args.read:
    qr.read()
else:
    if args.msg:
        qp.publish(args.msg)
    else:
        qp.publish("default msg")
