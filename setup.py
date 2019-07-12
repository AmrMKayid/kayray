from setuptools import setup, find_packages

setup(
	name='sonic_on_ray',
	packages=[package for package in find_packages() if package.startswith('kayray')],
	description='Kayray experiments',
	author='Amr Kayid',
	url='https://github.com/AmrMKayid/kayray',
	author_email='amrkayid2027@gmail.com',
	version='0.0.1'
)