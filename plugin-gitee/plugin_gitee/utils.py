# Connectors for EnrichOcean
from .enriched.gitee import GiteeEnrich
# Connectors for Ocean
from .raw.gitee import GiteeOcean


def get_connectors():
    return {"gitee": [GiteeOcean, GiteeEnrich]}

