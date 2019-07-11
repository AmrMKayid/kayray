# from mlagents.envs import UnityEnvironment
from gym_unity.envs import UnityEnv
from kayray.utils import glogger, describe

def make_unity_env(env_name):
	env_name = f'build/{env_name}'  # Name of the Unity environment binary to launch
	env = UnityEnv(env_name, worker_id=0, use_visual=True)
	# env = UnityEnvironment(file_name=env_name, worker_id=0)
	glogger.info(describe(env))