from .raw.git import GitOcean
from .enriched.git import GitEnrich
import sys
import pkg_resources

PLUGIN = "plugin_"


def get_connectors():
    connectors = {"git": [GitOcean, GitEnrich]}
    for plugin in pkg_resources.iter_entry_points('plugin'):
        backend = plugin.name.lower()

        raw_module_name = PLUGIN + backend + '.raw.' + backend
        raw_module = __import__(raw_module_name, fromlist=["raw." + backend])
        raw_cls = getattr(raw_module, plugin.name + "Ocean")

        enriched_module_name = PLUGIN + backend + '.enriched.' + backend
        enriched_module = __import__(enriched_module_name, fromlist=[
                                     "enriched." + backend])
        enriched_cls = getattr(enriched_module, plugin.name + "Enrich")

        connectors[backend] = [raw_cls, enriched_cls]
    return connectors
