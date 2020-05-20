# Connectors for EnrichOcean
from .enriched.gitlab import GitLabEnrich
# Connectors for Ocean
from .raw.gitlab import GitLabOcean


def get_connectors():
    return {"gitlab": [GitLabOcean, GitLabEnrich]}

