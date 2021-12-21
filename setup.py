from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='random-giphy-bot',
    version='1.0',
    description='Discord bot that gives a random GIF from GIPHY, based on a single word.',
    license='LGPL 2.1',
    long_description=long_description,
    author='Nathan Guerrero',
    author_email='naguerr2@uci.edu',
    url='https://github.com/AnarchoBooleanism/random-giphy-bot',
    packages=['random-giphy-bot'],
    install_requires=[],
    scripts=[
            
            ]
)