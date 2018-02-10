from setuptools import setup

setup(name='libs',
      version='0.1',
      description='Live coding experiment',
      url='https://github.com/ngmatos/LiveCodingPython',
      author='Nuno Barros',
      author_email='nunobarros_@hotmail.com',
      packages=['libs'],
      install_requires=[
          'watchdog',
      ],
      zip_safe=False)