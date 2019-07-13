# from mlagents.envs import UnityEnvironment
import os
from gym_unity.envs import UnityEnv
from kayray.utils import glogger, describe

COUNTER = 0
PATH = os.path.dirname(os.path.abspath(__file__))

def make_unity_env(env_name, worker_id=0,  no_graphics=True):
	glogger.info(f'Starting env: {env_name}')
	env_name = f'{PATH}/build/{env_name}'  # Name of the Unity environment binary to launch
	multiagent = env_name[-2:] == '20'
	# TODO: worker_id & nums_workers
	env = UnityEnv(environment_filename=env_name, worker_id=worker_id, no_graphics=no_graphics, multiagent=multiagent) #, use_visual=True)
	# env = UnityEnvironment(file_name=env_name, worker_id=0)
	glogger.info(describe(env))
	return env