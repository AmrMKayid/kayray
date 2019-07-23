import pandas as pd

exp = pd.read_csv('~/kayray_results/local/gym-reacher-ppo-baseline/PPO_RoboschoolReacher-v1_0_2019-07-21_01-13-38_fjl4r_c/progress.csv')
print(exp.head())
print(exp.tail())

# exp.plot(total_time_s, episode_reward_mean)
exp.plot(x='time_total_s', y='episode_reward_mean', style='o')
# print(list(exp))
import matplotlib.pyplot as plt
plt.plot(exp['time_total_s'], exp['episode_reward_mean'])
plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd

# # gca stands for 'get current axis'
# ax = plt.gca()

# exp.plot(kind='line',x='time_total_s',y='episode_reward_mean',ax=ax)
# # df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)

# plt.show()