# dict

>命令行下[中英，中俄，中日，中韩，中法，中德，中西]文互翻译工具（Command line translation tool for Chinese English, 
Chinese French, Chinese Japanese, Chinese Korean, Chinese German），目前支持中英互译，翻译服务基于有道翻译。
>同时也支持程序调用


## 安装(Install)

```
sudo pip3 install dictfire
```

## 用法(Usage)

### 命令行使用

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

### 程序调用
```
result = DictFire(is_command=False).translate("I love you")
或者
d = DictFire(is_command=False)
result = d.translate("I love you")

print(result)
```

1. 返回成功：
```
{
    "code": 0,
    "type": "EN2ZH_CN",
    "src": "I love you",
    "tgt": "我爱你",
    "msg": "获取成功"
}
```

2. 返回失败：
```
{
    "code": 20,
    "type": "EN2ZH_CN",
    "src": "I love you",
    "tgt": "",
    "msg": "WORD TO LONG"
}
```

