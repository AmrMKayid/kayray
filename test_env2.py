from kayray import DEFAULT_RESULTS_DIR
from kayray.envs import make_env, make_unity_env
from kayray.utils import set_global_seeds, make_parser, DotDict, glogger

env = make_unity_env(DotDict({'worker_index': 0}), 'Reacher20')
env.reset()
obs, rew, dones, info = env.step(env.action_space.sample())


