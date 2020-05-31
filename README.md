# python-plugins-test

Dynamically discover and load plugins.

## Describtion

There are two packages: [`grimoirelab-elk`](./grimoirelab-elk) and [`grimoirelab-elk-gitee`](./grimoirelab-elk-gitee), which are distributed separately.

-   `grimoirelab-elk` implements the core logic and includes some default backends(e.g. `git` and `github`)
-   `grimoirelab-elk-gitee` provides extra feature of `gitee` backend

### plugins

[`grimoirelab-elk-gitee`](./grimoirelab-elk-gitee/setup.py) registers itself for discovery by adding the `entry_points` argument to `setup()` in `setup.py`.

```python
setup(name="grimoire-elk-gitee",
      description="This is grimoire-elk-gitee",
      packages=['grimoire_elk_gitee', 'grimoire_elk_gitee.enriched', 'grimoire_elk_gitee.raw'],
      entry_points={"grimoire_elk": "gitee = grimoire_elk_gitee.utils:get_connectors"},
      )
```

On the other hand, it exports the `connectors` by `get_connectors()` in [`utils.py`](./grimoirelab-elk-gitee/grimoire_elk_gitee/utils.py):

```python
# Connectors for EnrichOcean
from .enriched.gitee import GiteeEnrich
# Connectors for Ocean
from .raw.gitee import GiteeOcean

def get_connectors():
    return {"gitee": [GiteeOcean, GiteeEnrich]}
```

### core

`grimoirelab-elk` can automatically discover the registered entry points by using `pkg_resources.iter_entry_points()` and load all of the `connectors` provided by plugins in [`utils.py`](./grimoirelab-elk/grimoire_elk/utils.py):

```python
def get_connectors():
    connectors = {"git": [GitOcean, GitEnrich]}
    for entry_point in pkg_resources.iter_entry_points('grimoire_elk'):
        connectors.update(entry_point.load()())
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
      ...
    }

## How to run

```bash
git clone git@github.com:heming6666/python-plugins-test.git
cd python-plugins-test
sudo bash run.sh
```


## Reference
-   <https://amir.rachum.com/blog/2017/07/28/python-entry-points/>
-   <https://packaging.python.org/guides/creating-and-discovering-plugins/#using-package-metadata>
-   <https://www.geeksforgeeks.org/how-to-dynamically-load-modules-or-classes-in-python/>
-   <https://stackoverflow.com/questions/2724260/why-does-pythons-import-require-fromlist>
