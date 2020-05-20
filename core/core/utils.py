from .raw.git import GitOcean
from .enriched.git import GitEnrich
import pkg_resources

PLUGIN_PREFIX = "plugin"


def get_connectors():
    connectors = {"git": [GitOcean, GitEnrich]}
    for plugin in pkg_resources.iter_entry_points(PLUGIN_PREFIX):
        backend = plugin.name
        module_name = PLUGIN_PREFIX + "_" + backend + ".utils"
        module = __import__(module_name, fromlist=["get_connectors"])
        connectors.update(getattr(module, "get_connectors")())
    return connectors
