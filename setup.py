from setuptools import setup, find_packages

setup(
	name='KayRay',
	packages=[package for package in find_packages() if package.startswith('kayray')],
 	install_requires=[
		'ray', 'mlagents', 'gym_unity', 'gym', 'roboschool', 
		'pandas', 'pydash', 'psutil', 'setproctitle', 'lz4',
  		'torch', 'opencv-python', 'requests'
	 ],
	description='Kayray experiments',
	author='Amr Kayid',
	url='https://github.com/AmrMKayid/kayray',
	author_email='amrkayid2027@gmail.com',
	version='0.0.1'
)
