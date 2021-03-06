#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyjn",
    version="0.0.1",
    author="Arghadeep Chaudhury",
    author_email="arghadeep.chaudhury@gmail.com",
    description="Python Lib for api call on Indian Covid 19 dataset near real time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepstartup/INDICovid19",
    packages=find_packages(),
    install_requires=['flatten_json'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)