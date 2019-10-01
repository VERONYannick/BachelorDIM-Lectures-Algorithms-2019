import argparse
import simple_queue_publish as qp
import simple_queue_read as qr

parser = argparse.ArgumentParser()
parser.add_argument("-read",action="store_true")
parser.add_argument("-concurrency",action="store_true")
parser.add_argument("-msg")


args = parser.parse_args()


if not args.read:
    print("number of message to send ?")
    nb_msg = int(input())
else:
    print("number of readers ?")
    nb_reader = int(input()) 

if args.read:
    qr.read(args.concurrency,nb_reader)
else:
    if args.msg:
        msg=args.msg
    else:
        msg="default msg"
    qp.publish(msg,args.concurrency,nb_msg)
