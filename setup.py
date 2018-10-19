# -*- coding: utf-8 -*-
import re
from setuptools import setup

REQUIRES = [
    'boto3'
]


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname, "r") as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


def readme():
    try:
        with open('Readme.md') as f:
            return f.read()
    except IOError:
        return ''

__version__ = find_version("aws_ssh_config/__init__.py")

setup(
    name="aws_ssh_config",
    version=__version__,
    description="aws_ssh_config generates ssh config file content from given AWS account",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Dmitriy Lyalyuev",
    author_email="dmitriy@lyalyuev.info",
    url="https://github.com/DmitriyLyalyuev/aws_ssh_config",
    packages=["aws_ssh_config"],
    install_requires=REQUIRES,
    license="MIT",
    scripts=['aws_ssh_config/aws_ssh_config'],
    keywords="ssh aws devops sysadmin-tool script",
    classifiers=[
        "Environment :: MacOS X",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
)
