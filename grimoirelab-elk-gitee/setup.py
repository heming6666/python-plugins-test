from setuptools import setup

setup(name="grimoire-elk-gitee",
      description="This is grimoire-elk-gitee",
      version="0.1.0",
      packages=['grimoire_elk_gitee', 'grimoire_elk_gitee.enriched', 'grimoire_elk_gitee.raw'],
      entry_points={"grimoire_elk": "gitee = grimoire_elk_gitee.utils:get_connectors"},
      setup_requires=['wheel'],
      zip_safe=False
      )
