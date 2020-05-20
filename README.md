# python-plugins-test

Dynamically discover and load plugins.

## Describiton

There are three packages: [`core`](./core), [`plugin-gitee`](./plugin-gitee) and [`plugin-gitlab`](./plugin-gitlab), which are distributed separately.

-   `core` implements the core logic and includes some default backends(e.g. `git` and `github`)
-   `plugin-gitee` provides extra feature of `gitee` backend
-   `plugin-gitlab` provides extra feature of `gitlab` backend

### plugins

[`plugin-gitee`](./plugin-gitee/setup.py) and [`plugin-gitlab`](./plugin-gitlab/setup.py) register themselves for discovery by adding the `entry_points` argument to `setup()` in `setup.py`.

```python
setup(name="plugin_gitee",
      description="This is plugin_gitee",
      packages=["plugin_gitee", "plugin_gitee.raw", "plugin_gitee.enriched"],
      entry_points={"plugin": "gitee = plugin_gitee"},
      )
```

```python
setup(name="plugin_gitlab",
      description="This is plugin_gitlab",
      packages=["plugin_gitlab", "plugin_gitlab.raw",
                "plugin_gitlab.enriched"],
      entry_points={"plugin": "gitlab = plugin_gitlab"},
      )
```

### core

[`core`](./core/core/utils) can automatically discover the registered entry points by using `pkg_resources.iter_entry_points()` and dynamically load modules of plugins by using ` __import__()` and `getattr()` method.

In this case, `plugin-gitee` exports the `gitee connectors` by `get_connectors()` in [`utils.py`](./plugin-gitee/plugin_gitee/utils.py):

```python
# Connectors for EnrichOcean
from .enriched.gitee import GiteeEnrich
# Connectors for Ocean
from .raw.gitee import GiteeOcean

def get_connectors():
    return {"gitee": [GiteeOcean, GiteeEnrich]}
```

And [`plugin-gitlab`](./plugin-gitlab/plugin_gitlab/utils.py) does the same thing.

While `core` will import all of the `connectors` provided by plugins in [`utils.py`](./core/core/utils.py):

```python
PLUGIN_PREFIX = "plugin"
def get_connectors():
    connectors = {"git": [GitOcean, GitEnrich]}
    for plugin in pkg_resources.iter_entry_points(PLUGIN_PREFIX):
        backend = plugin.name
        module_name = PLUGIN_PREFIX + "_" + backend + ".utils"
        module = __import__(module_name, fromlist=["get_connectors"])
        connectors.update(getattr(module, "get_connectors")())
    return connectors
```

Finally, you can get all of the `connectors`:

```python
from core.utils import get_connectors
connectors = get_connectors()
```

The result looks like:

    {
      "git": [GitOcean, GitEnrich],
      "gitee": [GiteeOcean, GiteeEnrich],
      "gitlab": [GitlabOcean, GitlabEnrich]
      ...
    }

## How to run

```bash
git clone git@github.com:heming6666/python-plugins-test.git
cd python-plugins-test
sudo bash run.sh
```

## Note
**The entry points should be well defined in advance if using package metadata to do the automatic plugin discovery.**

## Reference

-   <https://packaging.python.org/guides/creating-and-discovering-plugins/#using-package-metadata>
-   <https://www.geeksforgeeks.org/how-to-dynamically-load-modules-or-classes-in-python/>
-   <https://stackoverflow.com/questions/2724260/why-does-pythons-import-require-fromlist>
