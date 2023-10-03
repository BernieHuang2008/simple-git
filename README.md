# simple-git
simple-git是一个python写的，简单版本的git。这里有着很全的注释，帮助开发者们更好地理解git的原理。

simple-git is a python project tried to write a simple version of git with full comments, help devs to learn "how git works".

# v1
### requirements
```
difflib ............... python built-in package
```

### supported features
|简称|功能描述|用法|
|-|-|-|
|commit|git提交操作，可以生成hash id|commit(content)|
|new branch|新建空分支操作|new_branch(name)|
|fork branch|复制分支|fork_branch(source, target)|
|switch branch|切换分支|switch_branch(name)|
