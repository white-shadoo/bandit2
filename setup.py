#!/usr/bin/env python
try:
    import pbr
except ImportError:
    import subprocess
    subprocess.check_call(["pip", "install", "pbr"])
    import pbr

from setuptools import setup

setup(setup_requires=["pbr"], pbr=True)
