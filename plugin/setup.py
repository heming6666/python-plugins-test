from setuptools import setup

setup(name="plugin",
      description="This is plugin",
      version="0.1.0",
      packages=['plugin', 'plugin.raw', 'plugin.enriched'],
      setup_requires=['wheel']
)