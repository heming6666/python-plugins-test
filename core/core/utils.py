from .raw.git import GitOcean
from .enriched.git import GitEnrich
import sys
import pkg_resources

PLUGIN = "plugin_"


def get_connectors():
    connectors = {"git": [GitOcean, GitEnrich]}
    for plugin in pkg_resources.iter_entry_points('plugin'):
        backend = plugin.name
        module_name = PLUGIN + backend + ".utils"
        module = __import__(module_name, fromlist=["get_connectors"])
        connectors.update(getattr(module, "get_connectors")())
    return connectors
