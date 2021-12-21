from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='random-giphy-bot',
    version='0.1.0dev',
    description='Discord bot that gives a random GIF from GIPHY, based on a single word.',
    license='LGPL 2.1',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Nathan Guerrero',
    author_email='naguerr2@uci.edu',
    url='https://github.com/AnarchoBooleanism/random-giphy-bot',
    packages=find_packages(),
    install_requires=['discord.py', 'python-dotenv'],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'random_giphy_bot = random_giphy_bot.app:run'
        ]
    },
    data_files={
        '': ['.env', '.env*']
    }
)

# Note: If adding tests or other directories that shouldn't be added as packages, replace find_packages() with find_packages(exclude=('tests*', etc etc))