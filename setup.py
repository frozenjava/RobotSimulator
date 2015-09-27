#
# setup.py
# Josh Artuso
# Setup file to install the jbot module
#

from distutils.core import setup

setup(name='jBot',
      version='1.2',
      description='Educational robot simulator',
      author='Josh Artuso',
      url='https://github.com/frozenjava/RobotSimulator',
      packages=['jbot'],
      package_dir={'jbot': 'jbot'},
      package_data={'jbot': ['images/*.png']}
      )
