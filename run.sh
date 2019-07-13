#!/bin/sh

python train.py -f experiments/$1.yaml 2>&1 | tee  experiments/output/$1.txt