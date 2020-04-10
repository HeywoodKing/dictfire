
打包上传(python setup.py upload)
```
删除之前的构建文件，重新构建，打包，上传到正式pypi，推送git，并打上tag版本
python setup.py upload


分步：
python setup.py sdist build bdist_wheel
python setup.py build sdist bdist_wheel bdist_egg

twine upload dist/*

git add .
git commit -m "描述"
git push origin dev
git tag v{0}
git push --tags
```

测试上传(python setup.py uploadtest)
```
构建
python setup.py build bdist bdist_wheel bdist_egg
python setup.py sdist bdist bdist_wheel bdist_egg

上传
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
