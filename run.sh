#!/bin/sh
# args: env_type | train_mode | experiment_name
python train.py -f experiments/$1/$2/$3.yaml 2>&1 | tee  experiments/output/$2/$3.txt