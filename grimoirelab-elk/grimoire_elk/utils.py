from .raw.git import GitOcean
from .enriched.git import GitEnrich
import pkg_resources

ENTRY_POINT_NAME = "grimoire_elk"
def get_connectors():
    connectors = {"git": [GitOcean, GitEnrich]}
    for entry_point in pkg_resources.iter_entry_points(ENTRY_POINT_NAME):
        connectors.update(entry_point.load()())
    return connectors
