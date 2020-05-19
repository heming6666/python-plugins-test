# python-plugins-test
本仓库用于测试 Python 插件的自动发现与加载。

关联 issue: https://github.com/X-lab2017/grimoirelab-elk/issues/3

## 功能
- `plugin` 模拟核心包
- `plugin-gitee` 模拟 gitee 插件包
- `plugin-gitlab` 模拟 gitlab 插件包

目前实现效果为：三个包独立打包发布，在`plugin` 核心包运行时可自动发现、加载插件包的相关类。

## 运行

```bash
git clone git@github.com:heming6666/python-plugins-test.git
cd python-plugins-test

sudo bash run.sh
```

或者可参考 [run.sh](https://github.com/heming6666/python-plugins-test/blob/master/run.sh) 脚本内容手动运行。


运行结果：
```
====git=====
Hello world from GitOcean
<plugin.raw.git.GitOcean object at 0x7f64226cbb70>
Hello world from GitEnrich
<plugin.enriched.git.GitEnrich object at 0x7f64226cb8d0>
====gitee=====
Hello world from GiteeOcean
<plugin_gitee.raw.gitee.GiteeOcean object at 0x7f64226cbe10>
Hello world from GiteeEnrich
<plugin_gitee.enriched.gitee.GiteeEnrich object at 0x7f64226cb898>
====gitlab=====
Hello world from GitlabOcean
<plugin_gitlab.raw.gitlab.GitlabOcean object at 0x7f641fa8ed68>
Hello world from GitlabEnrich
<plugin_gitlab.enriched.gitlab.GitlabEnrich object at 0x7f641fa8eda0>
```

## 目录说明

```
- plugin  模拟 grimoirelab-elk 目录
  - plugin 模拟 grimoire_elk 目录
    - enriched
      -  __init__.py
      - git.py 模拟 grimoire_elk/enriched 下默认核心backend
    - raw
      -  __init__.py
      - git.py 模拟 grimoire_elk/raw 下默认核心backend
    - __init__.py 
    - util.py 模拟 grimoire_elk/util 文件
  - setup.py  
 ``` 

```
- plugin-gitee  模拟 grimoirelab-elk-gitee 目录
  - plugi-gitee 模拟 grimoire_elk_gitee 目录
    - enriched
      -  __init__.py
      - gitee.py 模拟 grimoire_elk/enriched 下 gitee backend
    - raw
      -  __init__.py
      - gitee.py 模拟 grimoire_elk/raw 下 gitee backend
    __init__.py
  - setup.py  
``` 

```
- plugin-gitlab  模拟 grimoirelab-elk-gitlab 目录
  - plugin-gitlab 模拟 grimoire_elk_gitlab 目录
    - enriched
      -  __init__.py
      - gitlab.py 模拟 grimoire_elk/enriched 下 gitlab backend
    - raw
      -  __init__.py
      - git.py 模拟 grimoire_elk/raw 下 gitlab backend
    __init__.py
  - setup.py  
 ``` 

 ## 插件自动发现/加载机制说明
 TBD
