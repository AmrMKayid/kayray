# from mlagents.envs import UnityEnvironment
import os
import gym
from gym import spaces
from gym_unity.envs import UnityEnv
from kayray.utils import glogger, describe
from collections import OrderedDict

COUNTER = 0
PATH = os.path.dirname(os.path.abspath(__file__))

class UnityRayEnv(gym.Env):
    def __init__(self, env_config, env_name, no_graphics=True, multiagent=True, use_visual=False):
        glogger.info(f'Starting env: {env_name} | worker_id: {env_config.worker_index}')
        glogger.fatal(f'worker_index: {env_config.worker_index} | vector_index: {env_config.vector_index}')
        env_name = f'{PATH}/build/{env_name}'
        multiagent = env_name[-2:] == '20'
        self._env = UnityEnv(environment_filename=env_name, worker_id=env_config.worker_index, no_graphics=no_graphics, multiagent=multiagent) #, use_visual=True)
        self.action_space = self._env.action_space # spaces.Dict({f'action_{i}': self._env.action_space for i in range(self._env._n_agents)}) #self._env.action_space
        self.observation_space = spaces.Dict({f'obs_{i}': self._env.observation_space for i in range(self._env._n_agents)})
        glogger.info(describe(self._env))
        glogger.info(describe(self))
    def reset(self):
        return self._env.reset()
    def step(self, actions):
        if isinstance(actions, OrderedDict):
            actions = list(actions.values())
        # glogger.fatal(f'Actions: {actions}')
        obs, rewards, dones, infos = self._env.step(actions)
        # glogger.fatal(obs, rewards, dones, infos)
        obs = spaces.Dict({f'obs_{i}': o for i, o in enumerate(obs)})
        return obs, rewards, dones, infos

def make_unity_env(env_config, env_name, worker_id=0,  no_graphics=True):
	return UnityRayEnv(env_config, env_name)

# def make_unity_env(env_config, env_name, worker_id=0,  no_graphics=True):
# 	# return UnityRayEnv(env_config, env_name)
# 	glogger.info(f'Starting env: {env_name} | worker_id: {env_config.worker_index}')
# 	glogger.fatal(f'worker_index: {env_config.worker_index} | vector_index: {env_config.vector_index}')
# 	env_name = f'{PATH}/build/{env_name}'
# 	multiagent = env_name[-2:] == '20'
# 	env = UnityEnv(environment_filename=env_name, worker_id=env_config.worker_index, no_graphics=no_graphics, multiagent=multiagent) #, 
# 	glogger.info(env)
# 	return env