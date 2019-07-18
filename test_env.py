#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import time
import yaml
import json
import argparse

import ray
from ray.tests.cluster_utils import Cluster
# from ray.tune.config_parser import make_parser
# from ray.tune.result import DEFAULT_RESULTS_DIR
from ray.tune.trial import resources_to_json
from ray.tune.registry import register_env
from ray.tune.tune import _make_scheduler, run_experiments

from kayray import DEFAULT_RESULTS_DIR
from kayray.envs import make_env
from kayray.utils import set_global_seeds, make_parser, DotDict, glogger


env = make_env(DotDict({'env_type': 'unity', 'worker_index': 1}), 'mac/Reacher')
