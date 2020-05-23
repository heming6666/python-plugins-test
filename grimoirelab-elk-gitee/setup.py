from setuptools import setup

setup(name="plugin_gitee",
      description="This is plugin_gitee",
      version="0.1.0",
      packages=["plugin_gitee", "plugin_gitee.raw", "plugin_gitee.enriched"],
      entry_points={"plugin": "gitee = plugin_gitee"},
      setup_requires=['wheel']
      )
