## Question

1. 打包不能生成tar.gz的问题
```
linux 下生成的是tar.gz
windows 下生成的是tar
```

2. 上传提示description描述格式问题
```
将readme.md使用pypandoc(pandoc) convert_file转换为rst文件，然后去取rst文件内容即可
```

3. pip3安装测试，提示fake-useragent的依赖问题
```
将在线读取fake_useragent.json包提前预打包到包里面，这样避免因为网络问题造成的安装依赖出错问题
```

4. 安装dictfire后，输入dict a测试报错如下
```
D:\Flack\Project\Github\dictfire>dict -h
Traceback (most recent call last):
  File "d:\programdata\.pyenv\pyenv-win\versions\3.7.4-amd64\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "d:\programdata\.pyenv\pyenv-win\versions\3.7.4-amd64\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "D:\ProgramData\.pyenv\pyenv-win\versions\3.7.4-amd64\Scripts\dict.exe\__main__.py", line 4, in <module>
ModuleNotFoundError: No module named 'dict'
```
原因：在setup.py文件中配置的setup中的'console_scripts'参数的值指向的包名的文件夹名错误
错误写法：
```
'console_scripts': [
    'dict = dict:main',
]
```
正确写法：
```
'console_scripts': [
    'dict = dictfire:main',
]
因为我的核心包的父级文件夹为dictfire
```

5. 编译后生成的包名问题
``` 
dictfire-1.0.1-py2.py3-none-any.whl
```
原因：
方案：

6. pypi上传过一次包，然后删除之后再上传，提示报名已经被使用的问题
原因：可能是虽然是删除了在pypi,test.pypi上的包，但是还没有删除平台上用于下载分发的包，导致上传的时候提示包名被占用，因为版本重复了
方案：将版本号增加即可解决

7. 编译打包项目的是提示警告的问题
```
warning: build_py: byte-compiling is disabled, skipping.
warning: install_lib: byte-compiling is disabled, skipping.
```

8. 使用python setup.py upload
```
HTTPError: 403 Client Error: Invalid or non-existent authentication information. 
See https://pypi.org/help/#invalid-auth for details for url: https://upload.pypi.org/legacy/
```
原因：pypi.org的用户名或密码输入错误
方案：输入正确的用户名和密码

9. 增加帮助和参数命令
```

```

10. 第一次安装使用fake-useragent重试次数达到最大报错问题
```
fake_useragent.errors.FakeUserAgentError: Maximum amount of retries reached （fake_useragent代理获取失败）
下载最新版本json文件（网页拉到最低保存为json文件（fake_useragent.json））
https://fake-useragent.herokuapp.com/browsers/0.1.11

在项目中引用即可
location = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + '/fake_useragent_v0.1.11.json'
self.ua = UserAgent(verify_ssl=False, path=location)
```

11. ubuntu18.04 安装失败
```

```

12. Upload failed (403): Invalid or non-existent authentication information.
```
错误的用户验证信息，你需要创建一个用户验证文件 ~/.pypirc
```

13. Upload failed (403): You are not allowed to edit 'xxx' package information

这个已经不需要了，直接使用upload上传代替了
你需要先注册你的包才可以开始上传，运行注册命令：
```
python setup.py register
```

14. Server response (401): Incomplete registration; check your email
你的PyPI账户还没完成邮箱验证，你需要去注册邮箱找到一封验证邮件完成验证后再重试失败的步骤。


15. Server response (400): Invalid classifier "Topic :: Software Development :: Utilities"
你的setup.py文件中的classifier信息有误，请按官网的正确分类书写classifier.

16. error: No dist file created in earlier command
你还没打包就开始了上传命令，建议打包和上传的操作放在一起做，比如：
```
python setup sdist upload
```

17. error: Upload failed (499): Client Disconnected
这应该是网络问题，多重试几次。

18. Upload failed (400): File already exists
文件已经存在了，你每一次上次都应该更新版本号
