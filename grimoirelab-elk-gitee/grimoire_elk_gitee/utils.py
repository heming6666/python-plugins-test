from .raw.gitee import GiteeOcean
from .enriched.gitee import GiteeEnrich


def get_connectors():

    return {"gitee": [GiteeOcean, GiteeEnrich]}
