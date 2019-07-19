# from mlagents.envs import UnityEnvironment
import os
import platform
import gym
from gym import spaces
from gym_unity.envs import UnityEnv
from kayray.utils import glogger, describe
from collections import OrderedDict

from ray.rllib.env.multi_agent_env import MultiAgentEnv


PATH = os.path.dirname(os.path.abspath(__file__))


class UnityRayEnv(gym.Env):
    def __init__(self, env_config, env_name='Reacher', no_graphics=True, multiagent=False, use_visual=False):
        # print(env_config)
        glogger.info(f'Starting env: {env_name} | worker_id: {env_config.worker_index}')
        env_name = f'{PATH}/build/{env_name}'
        self.env = UnityEnv(environment_filename=env_name, worker_id=env_config.worker_index, no_graphics=no_graphics, multiagent=multiagent) 
        self.observation_space = self.env.observation_space
        self.action_space = self.env.action_space
        glogger.info(describe(self.env))
        glogger.info(describe(self))
        
    def reset(self):
        return self.env.reset()
    
    def step(self, actions):
        obs, rewards, dones, infos = self.env.step(actions)
        return obs, rewards, dones, infos
    
    def close(self):
        self.env.close()

class MultiAgentsUnityRayEnv(UnityRayEnv, MultiAgentEnv):
    def __init__(self, env_config, env_name='Reacher20', no_graphics=True, multiagent=True, use_visual=False):
        UnityRayEnv.__init__(self, env_config=env_config, env_name=env_name, no_graphics=no_graphics, multiagent=multiagent, use_visual=use_visual)
        # glogger.info(f'Starting env: {env_name} | worker_id: {env_config.worker_index}')
        # env_name = f'{PATH}/build/{env_name}'
        # self.env = UnityEnv(environment_filename=env_name, worker_id=env_config.worker_index, no_graphics=no_graphics, multiagent=multiagent)
        self.agents = self.env._n_agents
        self.dones = set()
        self.observation_space = self.env.observation_space
        self.action_space = self.env.action_space
        self.resetted = False
        glogger.info(describe(self))
        
    def reset(self):
        self.resetted = True
        self.dones = set()
        last_obs = self.env.reset()
        return {i: obs for i, obs in enumerate(last_obs)}
        
    def step(self, action_dict):
        actions = list(action_dict.values())
        # glogger.fatal(actions)
        obs, rew, done, info = {}, {}, {}, {}
        obs_list, rew_list, done_list, info_list = self.env.step(actions)
        for i in range(self.agents):
            obs[i], rew[i], done[i], info[i] = obs_list[i], rew_list[i], done_list[i], info_list
            if done[i]:
                self.dones.add(i)
        done["__all__"] = len(self.dones) == self.agents
        
        # glogger.fatal(obs, rew, done, info)
        return obs, rew, done, info
        
    
    
def make_unity_env(env_config, env_name, no_graphics=True):
    multiagent = env_name[-2:] == '20'
    env_name = f'mac/{env_name}' if platform.system().lower() == 'darwin' else f'linux/{env_name}'
    if multiagent:
        return MultiAgentsUnityRayEnv(env_config, env_name, no_graphics=no_graphics)
    return UnityRayEnv(env_config, env_name, no_graphics=no_graphics)