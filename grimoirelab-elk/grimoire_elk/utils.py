from .raw.git import GitOcean
from .raw.gitee import GiteeOcean
from .enriched.git import GitEnrich
from .enriched.gitee import GiteeEnrich


def get_connectors():

    return {"git": [GitOcean, GitEnrich], "gitee": [GiteeOcean, GiteeEnrich]}
