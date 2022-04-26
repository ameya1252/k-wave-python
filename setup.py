#!/usr/bin/env python

from distutils.core import setup

setup(name='k-Wave-python',
      version='0.1',
      description='Acoustics toolbox for time domain acoustic '
                  'and ultrasound simulations in complex and tissue-realistic media.',
      author='Farid Yagubbayli',
      author_email='farid.yagubbayli@tum.de',
      maintainer='Walter Simson',
      maintainer_email='walter.simson@tum.de',
      url='http://www.k-wave.org/',
      packages=['kwave', 'kwave.utils','kwave.reconstruction', 'kwave.kWaveSimulation_helper'],
      )
