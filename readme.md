## pypssh
`pypssh` 命令行程序是一款简易易用的 ssh 批处理工具，它支持直接通过命令行或者配置文件的方式对多台主机进行操作。

## 用户指南
`pypssh` 的大多数帮助文档或示例都可以通过 `--help` 进行获取，所以这里仅对 `pypssh` 做一个简单的介绍。

### 关于基本使用
`pypssh` 无需配置即可进行简单的使用，示例：
```bash
# 通过命令行传入 ssh用户名/密码/端口 对 192.168.1.100 执行命令，并且注入环境变量
pypssh -u root -p 'root!@#$' -P 22 -h 192.168.1.100 -e NAME=peter execute 'echo hello $NAME'
# 
pypssh -u root -p 'root!@#$' -P 22 -h 192.168.1.100 put [localfile] [remotefile]
# 
pypssh -u root -p 'root!@#$' -P 22 -h 192.168.1.100 get [remotefile] [localdir]
```

但对于中大规模的主机数量而言，没有配置文件不便于管理，所以 `pypssh` 提供配置的方式对主机/主机组进行操作。我们可以通过 命令行 或者 手动编写 两种形式进行配置。
命令行的配置方式：
```bash
# 添加主机 192.168.1.100 并且为该主机设置账户密码以及端口和分组 test1 和 test2
pypssh config add-host 192.168.1.100 -u root -p 'root$123' -P 22 -t test1=x1 -t test2=x2
# 删除 test 组中的主机 192.168.1.100
pypssh config del-host 192.168.1.100 -t test
# 删除所有组中的主机 192.168.1.100
pypssh config del-host 192.168.1.100
# 列出所有主机信息
pypssh config list
# 列出存在 test1=x1 标签的主机
pypssh config list -t test1=x1

# 加载特殊格式的配置文件，该子命令使得 pypssh 支持多种格式的配置文件
# -p 默认值，加载普通格式的主机清单到配置中，普通格式主机清单每一项以换行符分割，每项格式为 hostname:[sshPort]:[sshUser]:[sshPassword]:[group1]:[group2]....
# -o 加载老版本 pypssh 配置文件的
# ....
pypssh config load -o inventory.conf 
```


### 关于能力
`pypssh` 提供以下子命令：
- config：提供配置的命令行接口
- execute：批量远程执行命令
- put：批量上传文件
- get：批量下载文件
- test：测试 ssh 是否可用
- execfile：将脚本上传到远程并执行
- version：版本/发行信息

## pypssh 开发者指南

该项目基于以下依赖：  
- paramiko: 提供 ssh 客户端支持  
- click: 提供 cli 支持  
- PyYAML: 提供 yaml 配置文件解析支持  
- PyInstaller: 提供二进制程序发布支持  


## 开发者参考
[click文档](https://click.palletsprojects.com/en/7.x/)