from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

import ray
from ray.tune import run_experiments, register_env
from ray.rllib.models import ModelCatalog

from kayray import DEFAULT_RESULTS_DIR
from kayray.envs import make_env, make_unity_env
from kayray.utils import set_global_seeds, make_parser, DotDict, glogger

env = make_unity_env(DotDict({'worker_index': 1}), 'linux/Reacher', no_graphics=False)
obs = env.reset()
print(obs)
# rews = []
for i in range(1000):
    # actions = {}
    # for a in range(env.agents):
    #     actions.update({f'Action_{a}': env.action_space.sample()})
    # glogger.info(actions)
    obs, rew, dones, info = env.step( env.action_space.sample())
    # rews.append(rew)
# glogger.info(rews)



# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--num-iters", type=int, default=100)
#     parser.add_argument("--num-workers", type=int, default=0)
#     args = parser.parse_args()

#     ray.init()

#     env_name = 'mac/Reacher'
#     register_env("unityml", lambda env_config: make_unity_env(env_config=env_config, env_name=env_name))

#     run_experiments({
#         "ppo_sc2": {
#             "run": "PPO",
#             "env": "unityml",
#             "stop": {
#                 "training_iteration": args.num_iters,
#             },
#             "config": {
#                 "num_workers": args.num_workers,
#                 "observation_filter": "NoFilter",  # breaks the action mask
#                 "vf_share_layers": True,  # don't create a separate value model
#             },
#         },
#      })
