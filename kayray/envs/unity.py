# from mlagents.envs import UnityEnvironment
import os
import gym
from gym import spaces
from gym_unity.envs import UnityEnv
from kayray.utils import glogger, describe
from collections import OrderedDict

from ray.rllib.env.multi_agent_env import MultiAgentEnv


PATH = os.path.dirname(os.path.abspath(__file__))


class UnityRayEnv(gym.Env):
    def __init__(self, env_config, env_name, no_graphics=True, multiagent=False, use_visual=False):
        glogger.info(f'Starting env: {env_name} | worker_id: {env_config.worker_index}')
        env_name = f'{PATH}/build/{env_name}'
        self._env = UnityEnv(environment_filename=env_name, worker_id=env_config.worker_index, no_graphics=no_graphics, multiagent=multiagent) 
        self.observation_space = self._env.observation_space
        self.action_space = self._env.action_space
        glogger.info(describe(self._env))
        glogger.info(describe(self))
        
    def reset(self):
        return self._env.reset()
    
    def step(self, actions):
        obs, rewards, dones, infos = self._env.step(actions)
        return obs, rewards, dones, infos

class MultiAgentsUnityRayEnv(MultiAgentEnv):
    def __init__(self, env_config, env_name, no_graphics=True, multiagent=True, use_visual=False):
        glogger.info(f'Starting env: {env_name} | worker_id: {env_config.worker_index}')
        env_name = f'{PATH}/build/{env_name}'
        self._env = UnityEnv(environment_filename=env_name, worker_id=env_config.worker_index, no_graphics=no_graphics, multiagent=multiagent)
        self.agents = self._env._n_agents
        self.dones = set()
        self.observation_space = self._env.observation_space
        self.action_space = self._env.action_space
        self.resetted = False
        glogger.info(describe(self._env))
        glogger.info(describe(self))
        
    def reset(self):
        self.resetted = True
        self.dones = set()
        last_obs = self._env.reset()
        return {i: obs for i, obs in enumerate(last_obs)}
        
    def step(self, action_dict):
        actions = list(action_dict.values())
        # glogger.fatal(actions)
        obs, rew, done, info = {}, {}, {}, {}
        obs_list, rew_list, done_list, info_list = self._env.step(actions)
        for i in range(self.agents):
            obs[i], rew[i], done[i], info[i] = obs_list[i], rew_list[i], done_list[i], info_list
            if done[i]:
                self.dones.add(i)
        done["__all__"] = len(self.dones) == self.agents
        
        # glogger.fatal(obs, rew, done, info)
        return obs, rew, done, info
        
    
    
def make_unity_env(env_config, env_name, worker_id=0,  no_graphics=True):
    multiagent = env_name[-2:] == '20'
    if multiagent:
        return MultiAgentsUnityRayEnv(env_config, env_name)
    return UnityRayEnv(env_config, env_name)