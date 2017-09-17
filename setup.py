#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
import drumutation

def readme():
    with open("README.md") as f:
        return f.read()

setup(name="drumutation",
      version=drumutation.__version__,
      description="Create LilyPond sheet music for drum permutations.",
      long_description=readme(),
      classifiers=[],
      keywords=[],
      url="https://github.com/donutfarian/drumutation",
      author="Kris Andersen",
      author_email="kris.andersen@gmail.com",
      license="MIT",
      packages=["drumutation"],
      app=["bin/drumutation"],
      data_files=[],
      scripts=["bin/drumutation"],
      setup_requires=[],
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
