from setuptools import setup

setup(name="grimoire-elk-gitee",
      description="This is grimoire-elk-gitee",
      version="0.1.0",
      packages=['grimoire_elk', 'grimoire_elk.enriched', 'grimoire_elk.raw'],
      namespace_packages=['grimoire_elk',
                          'grimoire_elk.enriched',
                          'grimoire_elk.raw'],
      setup_requires=['wheel'],
      zip_safe=False
      )
