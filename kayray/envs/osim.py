import numpy as np
from osim.env import L2M2019Env
from kayray.utils import glogger, describe

class OsimRLRayEnv():
    def __init__(self, env_config=None, visualize=False):
        self.env = L2M2019Env(visualize=visualize)
        self.observation_space = self.env.observation_space
        self.action_space = self.env.action_space
        glogger.info(describe(self.env))
        glogger.info(describe(self))
    
    def iterdict(self, d, l):
        for k, v in d.items():        
            if isinstance(v, dict):
                self.iterdict(v, l)
            else:            
                l.append(v)
        return l

    def new_obs(self, l):
        for i in range(len(l)):
            a = l[i]
            if isinstance(l[i], np.ndarray):
                l[i] = l[i].flatten()
            else:
                l[i] = np.array(l[i])
        l = np.hstack(l)
        return l

    def reset(self):
        new_obs = []
        observation = self.env.reset()
        if not isinstance(observation, list):
            observation = self.new_obs(self.iterdict(observation, new_obs))
        return observation


    def step(self, actions):
        new_obs = []
        observation, reward, done, info = self.env.step(actions)
        if not isinstance(observation, list):
            observation = self.new_obs(self.iterdict(observation, new_obs))
        
        return observation, reward, done, info


def make_osim_env(env_config, visualize=False):
    env = OsimRLRayEnv(env_config, visualize)
    return env