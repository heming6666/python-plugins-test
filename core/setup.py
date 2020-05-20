from setuptools import setup

setup(name="core",
      description="This is core",
      version="0.1.0",
      packages=['core', 'core.raw', 'core.enriched'],
      setup_requires=['wheel']
      )
