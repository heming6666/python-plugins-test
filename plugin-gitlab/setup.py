from setuptools import setup

setup(name="plugin_gitlab",
      description="This is plugin_gitlab",
      version="0.1.0",
      packages=["plugin_gitlab", "plugin_gitlab.raw",
                "plugin_gitlab.enriched"],
      entry_points={"plugin": "gitlab = plugin_gitlab"},
      setup_requires=['wheel']
      )
