from .raw.git import GitOcean
from .enriched.git import GitEnrich
import pkg_resources

def get_connectors():
    connectors = {"git": [GitOcean, GitEnrich]}
    for entry_point in pkg_resources.iter_entry_points('grimoire_elk'):
        connectors.update(entry_point.load()())
    return connectors
