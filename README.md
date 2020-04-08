# dict

命令行下[中英，中俄，中日，中韩，中法，中德，中西]文互翻译工具（Command line translation tool for Chinese English, 
Chinese French, Chinese Japanese, Chinese Korean, Chinese German），目前支持中英互译，翻译服务基于有道翻译。


## 安装(Install)

```
sudo pip3 install dictfire
```

## 用法(Usage)

#### 中译英(Chinese To English)

1. 单词(Word)
```
$ dict 测试
####################################################################
#  
#  测试 
#  
#  test
#
####################################################################
```

2. 句子(sentence)
```
$ dict 我爱你
####################################################################
#  
#  我爱你
#  
#  I love you
#
####################################################################
```

#### 英译中(English To Chinese)
1. 单词(Word)
```
$ dict test
####################################################################
#  
#  test
#  
#  测试
#  
####################################################################
```

2. 句子(sentence)
```
$ dict I love you
####################################################################
#  
#  I love you
#
#  我爱你。
#
####################################################################
```
***


打包上传
```
删除之前的构建文件，重新构建，打包，上传到正式pypi，推送git，并打上tag版本
python setup.py upload


分步：
python setup.py sdist build bdist_wheel

twine upload dist/*

git add .
git commit -m "描述"
git push origin dev
git tag v{0}
git push --tags
```
