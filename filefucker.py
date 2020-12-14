import argparse
import sys
import os
import random
import string

parser = argparse.ArgumentParser(description="Secure delete a file")

parser.add_argument("-f", "--file", type=str, help="File Name", required=True)
parser.add_argument("-n", "--num", type=str, help="How Many")

args = parser.parse_args()
filename = getattr(args, "file")
number = getattr(args, "num")


if number == None:
    number = 40

def randomdatagen(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

print("""
--------------------------------------
File/Dir : {}
Number   : {}
--------------------------------------
""".format(filename, number))
for count in range(number):
    with open(filename, "rb") as f:
        datatodelete = f.read()
    datalen = len(datatodelete)
    gendata = randomdatagen(datalen)
    with open(filename, "wb") as f:
        f.write(gendata.encode())

os.remove(filename)
print("Done", len(gendata))
    
