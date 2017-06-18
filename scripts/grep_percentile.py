#!/usr/bin/python

import os
import sys

ttype = sys.argv[1]
tmode = sys.argv[2]
tnum = sys.argv[3]
dirname = sys.argv[4]

dirpath = "rtk/raw/" + dirname + "/"

prefix = ttype + "-" + tmode + "-" + tnum

tmplogs = open(dirpath + prefix + "-rd.tmp", "r")

lines = tmplogs.readlines()
num = len(lines)

p90 = (int)(num*0.9) 
p95 = (int)(num*0.95)
p999 = (int)(num*0.999)

summ = 0.0
for i in range(0, num):
  summ += (float)(lines[i])/1000.0

out = "\t90th\t95th\t99.9th\tmax\tavg\n\t{:.02f}\t{:.02f}\t{:.02f}\t{:.02f}\t{:.02f}\n".format((float)(lines[p90])/1000.0, (float)(lines[p95])/1000.0, (float)(lines[p999])/1000.0, (float)(lines[-1])/1000.0, summ/num)
print out
