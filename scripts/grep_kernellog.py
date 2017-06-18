#!/usr/bin/python

import os
import sys

#ttype = sys.argv[1]
#tmode = sys.argv[2]
#tnum = sys.argv[3]
prefix = sys.argv[1]

#prefix = ttype + "-" + tmode + "-" + tnum
dirname = "kernellogs/" + prefix + "/"
kernellog = dirname + "kern.cnt.log"

f = open(kernellog, "r")
lines = f.readlines()

total = (float)(lines[0].split(" ")[1])

normal = (float)(lines[1].split(" ")[1])
blocked = (float)(lines[1].split(" ")[3])
retry = (float)(lines[1].split(" ")[5])
eio = (float)(lines[1].split(" ")[7])

recon = (int)(lines[4].split(" ")[1])

totaldio = (float)(lines[2].split(" ")[5])
blockdio = (float)(lines[2].split(" ")[2][:-1])

gc0 = (float)(lines[14].split(" ")[1])
gc1 = (float)(lines[15].split(" ")[1])
gc2 = (float)(lines[16].split(" ")[1])
gc3 = (float)(lines[17].split(" ")[1])
gc4 = (float)(lines[18].split(" ")[1])


if "def" in prefix:
  print "GC-BLOCK: {:.02f}% ({}/{}) \\\\\n".format(blocked/total*100, (int)(blocked), (int)(total))
  print "BLOCK-DIO: {:.02f}% ({}/{}) \\\\".format(blockdio/totaldio*100, (int)(blockdio), (int)(totaldio))
elif "nogc" not in prefix:
  print "GC-EIO: {:.02f}% ({}/{}) \\\\".format(eio/total*100, (int)(eio), (int)(total))
  print "RETRY: {:.02f}% ({}/{}) \\\\".format(retry/total*100, (int)(retry), (int)(total))
  print "RECONSTRUCT: {:.02f}% ({}/{}) \\\\\n".format(recon/total*100, (int)(recon), (int)(total))
  
  print "DIO_INGC_0: {:.02f}% ({}/{}) \\\\".format(gc0/totaldio*100, (int)(gc0), (int)(totaldio))
  print "DIO_INGC_1: {:.02f}% ({}/{}) \\\\".format(gc1/totaldio*100, (int)(gc1), (int)(totaldio))
  print "DIO_INGC_2: {:.02f}% ({}/{}) \\\\".format(gc2/totaldio*100, (int)(gc2), (int)(totaldio))
  print "DIO_INGC_3: {:.02f}% ({}/{}) \\\\".format(gc3/totaldio*100, (int)(gc3), (int)(totaldio))
  print "DIO_INGC_4: {:.02f}% ({}/{}) \\\\".format(gc4/totaldio*100, (int)(gc4), (int)(totaldio))
