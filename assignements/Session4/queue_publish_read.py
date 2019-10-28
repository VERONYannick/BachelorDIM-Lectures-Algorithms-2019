import argparse
import simple_queue_publish as qp
import simple_queue_read as qr
import time

parser = argparse.ArgumentParser()
parser.add_argument("-read",action="store_true")
parser.add_argument("-concurrency",action="store_true")
parser.add_argument("-msg")

args = parser.parse_args()


if not args.read:
    nb_msg = int(input("number of message to send : "))
else:
    nb_reader = int(input("number of readers : "))
    if nb_reader>1:
        slow_reader = input("Make reader 1 slow ? (y/n) : ")
        if slow_reader=='y':
            slow_reader=True
        else:
            slow_reader=False

if args.read:
    qr.read(args.concurrency,nb_reader,slow_reader)
else:
    if args.msg:
        msg=args.msg
    else:
        msg="default msg"
    qp.publish(msg,args.concurrency,nb_msg)
