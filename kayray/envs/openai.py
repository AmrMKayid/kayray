import gym
import roboschool
from kayray.utils import glogger, describe

def make_env(env_name):
	import gym
	import roboschool
	env = gym.make(env_name)
	# env._max_episode_steps = 300
	glogger.info(describe(env))
	return env