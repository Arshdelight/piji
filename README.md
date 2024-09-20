# Piji
Piji是一款可以更便捷使用Pyimagej的GUI
试行版，本仓库及软件本身暂且针对中国地区做优化，国际化开发会在后续跟进。可关注b站账户https://space.bilibili.com/3546758690900309  
目前没有打包版本，请先使用python虚拟环境运行piji，后续也未必有打包版本，因为目前我认为不打包版本可以提供更好的拓展性。不过我还不是很熟悉打包，也许打包也能保证python的包拓展性。  
很多功能没写，特别是设置页面里的检查更新、feedback等等，请先不要使用，直至正式版发布  
欢迎pull request  
**QQ讨论群：945612412  群密码：240918**

# 使用指南
建议安装Anaconda或者Miniconda。  
## 下载本仓库或git clone
[下载](https://github.com/Arshdelight/piji/archive/refs/heads/main.zip)
## 创建虚拟环境并进入
考虑到要使用cellpose，请使用python3.8
```powershell
conda create -n piji python=3.8
conda activate piji
```
## 安装依赖
```powershell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```
如果仍有缺失的依赖，请自行补装，也可以在github issue中提交这个问题  
## 启动软件
```powershell
python main.py
```
启动软件的一些简化策略：【会出一期视频，还没做】

## 安装Fiji（若已安装可跳过）
[Fiji官网](https://fiji.sc/)  
[点击下载最新64位](https://downloads.imagej.net/fiji/latest/fiji-win64.zip)

## 软件使用（精简说明）
### 基础使用：
#### 启动
1. 设置Java最大使用内存，考虑到虚拟内存，软件会自动给出 0~2倍内存 的设置范围
2. 选择Fiji的路径
3. 选择Java jre的路径，在Fiji目录中的java文件夹中往里可以找到一个jre目录，使用这个即可
#### 导入数据
1. 在“数据”页面打开一系列图像，目前建议把待处理图像放在一个文件夹中，因为目前仅支持一次性打开全部图像，目前只支持tif格式，以后会扩展，但是建议使用tif格式的图像进行分析
2. 点击“生成分析队列”按钮（如果已经创建过，想要复用，可以点击“加载已有队列”按钮）
#### 图像操作
1. 在“操作”页面可以进行一系列操作，首先要选择处理对象，目前可以选择单张图像或全选。全选会对所有的图像进行同一操作，建议在清楚全选的工作机制后使用。  
2. 操作可以直接运行，也可以拖动到右侧的编程列表进行可视化可排序模块化编程，编程列表中的操作可以按序运行，可以一键生成整合的操作脚本
### 进阶操作:
#### 操作脚本编写
1. 点击“脚本”页面可以进行脚本编写、修改、试运行等操作
2. “操作”页面中操作列表里的操作可以点击查看代码以再编辑等
3. “脚本”页面有快捷的按钮可以导入脚本模板，也可以在操作列表里的Template类别中选择需要的模板以修改

如果是macro脚本，使用macro模板可以快速建立，难度较小
如果是python脚本，需要操作pijiunit对象，这个后面会出视频及详细文档