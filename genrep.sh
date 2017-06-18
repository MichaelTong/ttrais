#!/bin/bash


echo "Please enter Trace Type: (e.g. tpcc)"
read ttype
echo "Please enter Running Mode: (e.g. gct, def)"
read tmode
echo "Please enter Seq NO. of this run:"
read tnum

./scripts/grep_vssimlog.py $ttype $tmode $tnum

./scripts/grep_kernellog.py $ttype-$tmode-$tnum

echo "Please enter dirname: (e.g. tpcc-1130)"
read dirname

./scripts/grep_percentile.py $ttype $tmode $tnum $dirname
