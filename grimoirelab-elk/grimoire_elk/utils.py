from .raw.git import GitOcean
from .enriched.git import GitEnrich

def get_connectors():

    return {"git": [GitOcean, GitEnrich]}
