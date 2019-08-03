__all__ = ['openai', 'unity', 'osim']

from .openai import *
from .unity import *
from .osim import *

def make_env(env_config, env_name, no_graphics=True):
    # print(env_config)
    if env_config['env_type'] == 'openai':
        return make_openai_env(env_config, env_name)
    elif env_config['env_type'] == 'unity':
        return make_unity_env(env_config, env_name, no_graphics=no_graphics)
    elif env_config['env_type'] == 'osim':
		return make_osim_env(env_config, visualize=False)
    else:
        raise NotImplementedError