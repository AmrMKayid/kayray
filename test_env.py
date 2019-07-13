from kayray.envs.unity import make_unity_env

env1 = make_unity_env('Reacher20', worker_id=0, no_graphics=False)
env2 = make_unity_env('Reacher20', worker_id=1, no_graphics=False)

env1.reset()
env2.reset()
while True:
	actions1 = [env1.action_space.sample() for _ in range(20)]
	actions2 = [env2.action_space.sample() for _ in range(20)]
	s1, r1, t1, i1 = env1.step(actions1)
	s2, r2, t2, i2 = env2.step(actions2)
	# print(s, r, t, i)