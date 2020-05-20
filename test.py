from core.utils import get_connectors

print("====git=====")
git = get_connectors()["git"][0]()
print(git)
git_enrich = get_connectors()["git"][1]()
print(git_enrich)
print("====gitee=====")
gitee = get_connectors()["gitee"][0]()
print(gitee)
gitee_enrich = get_connectors()["gitee"][1]()
print(gitee_enrich)
print("====gitlab=====")
gitlab = get_connectors()["gitlab"][0]()
print(gitlab)
gitlab_enrich = get_connectors()["gitlab"][1]()
print(gitlab_enrich)

