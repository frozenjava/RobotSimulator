#
# setup.py
# Josh Artuso
# Setup file to install the jbot module
#

from distutils.core import setup

setup(name='jBot',
      version='1.3',
      description='Educational robot simulator',
      author='Josh Artus',
      url='https://github.com/frozenjava/RobotSimulator',
      packages=['jbot'],
      package_dir={'jbot': 'jbot'},
      package_data={'jbot': ['images/*.png']}
      )
