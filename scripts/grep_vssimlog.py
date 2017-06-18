#!/usr/bin/python

import os
import sys

ttype = sys.argv[1]
tmode = sys.argv[2]
tnum = sys.argv[3]

logs = [None]*4

prefix = ttype + "-" + tmode + "-" + tnum
dirname = "vssimlogs/" + prefix + "/"

for i in range(0,4):
  f = open(dirname + prefix + "-vssd" + str(i+1) + ".csv", "r")
  logs[i] = f.readlines()

r = [0]*4
br = [0]*4
gc = [0]*4
bgc = [0]*4
sgc = [0]*4
bsgc = [0]*4

num = len(logs[0])
firstline = logs[0][0]
fw = firstline.split(',')
idx_r = fw.index("#r")
idx_br = fw.index("#br")
idx_gc = fw.index("#gc")

for i in range(1, num):
  gcs = 0
  bgcs = 0
  for j in range(0, 4):
    log = logs[j]
    line = log[i]
    w = line.split(',')
    br[j] += int(w[idx_br])
    r[j] += int(w[idx_r])
    gc[j] += int(w[idx_gc])
    if int(w[idx_gc])!=0:
      gcs += 1
    if int(w[idx_br]) != 0 and int(w[idx_gc])!=0 :
      bgcs += 1
      bgc[j] += int(w[idx_gc])
  if gcs > 0:
    sgc[gcs-1] += 1
  if bgcs > 0:
    bsgc[bgcs-1] += 1

out = ""
pbr = 0.0
for j in range(0, 4):
  out += "Blocked Reads in VSSD{:d}: {:.02f}%\n".format(j+1, 100*float(br[j])/float(r[j]))
  pbr += 100*float(br[j])/float(r[j])
out += "Average: {:.02f}%\n\n".format(pbr/4)

#for j in range(0, 4):
#  out += "GC in VSSD{:d}: {:d}\n".format(j+1, gc[j])

for j in range(0, 4):
  out += "Blocking GC in VSSD{:d}: {:d}\n".format(j+1, bgc[j])
out += "\n"

#for j in range(0, 4):
#  out += "{:d}-GC: {:.02f}%\n".format(j+1, 100*float(sgc[j])/float(num-1))

for j in range(0, 4):
  out += "{:d}-Blocking-GC: {:.02f}%\n".format(j+1, 100*float(bsgc[j])/float(num-1))

print out
