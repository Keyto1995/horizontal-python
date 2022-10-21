# horizontal-python

一个用来表现 python 在后台开发中效果的项目

## 环境

- python 3.10
- fastapi

## 安装

```bash
$ pip install -r requirement.txt
```
> 生成requirement.txt: `pip freeze >requirement.txt`

## 启动

```bash
# dev
$ uvicorn main:app --port 80 --reload

# prod
$ uvicorn main:app --host '0.0.0.0' --port 80
```

- [x] /ping
- [x] /clientIP
