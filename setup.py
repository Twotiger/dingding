# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dingding",
    version="0.4",
    author="Twotiger",
    author_email="dgl0518@gmail.com",
    description="ding ding robot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Twotiger/dingding",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
