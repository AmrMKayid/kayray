__all__ = ['openai', 'unity']

from .openai import *
from .unity import *

def make_env(env_config, env_name, no_graphics=True):
    # print(env_config)
    if env_config['env_type'] == 'openai':
        return make_openai_env(env_config, env_name)
    elif env_config['env_type'] == 'unity':
        return make_unity_env(env_config, env_name, no_graphics=no_graphics)
    else:
        raise NotImplementedError