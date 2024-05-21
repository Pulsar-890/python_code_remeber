# 常用代码段管理器

#### 介绍

​	更方便地查询你常用的代码段

#### 软件架构

​	您可以代码段整理到文本文件中，并通过本程序方便地调用

#### 使用说明

​	用管理功能创建文本文件，向里面写入代码段或者别的你想记的东西。

​	文件序号最好起单数字或者小写单字母方便访问，然后文件名是可以进行更改的没关系

​	可以在行首加上///使后面的代码在查询时执行，（我自己用这个功能一般是用来打开相关图片用的，例子如下）	   

```python
///os.startfile(图片路径)
```

​	也可以用两个###来注释掉一部分代码（我自己用这个功能一般是因为命令行框里不方便显示太多代码段，所以很长的代码段只能先注释掉，然后再通过打开文本文件的方式查看）

```
###需要被注释的内容###
###
需要被注释的内容
###
```

​	管理功能快捷代码：

```
000								 //编辑所有文件介绍
02						    	 //打开本文件夹
05[宽度]							//更改选项显示宽度
01[文件序号] [文件序号] 			//创建文件(文件序号最好起单数字或者小写单字母方便访问)
00[文件序号] [文件名]				//编辑文件
03[文件序号] [新文件名]				//文件重命名
04[文件序号] [文件名]			     //删除文件
```

#### 使用案例

​	小明经常使用python来画图，但是小明每次都需要手打一遍python的plot包和代码，特别麻烦。于是小明就想到可以使用这个工具。然后，他就先把他经常用的这段代码记录下来，比如说这段：

```
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('X轴')
plt.ylabel('Y轴')

x = [1, 2, 3, 4, 5] 
y = [2, 8, 4, 6, 10]
plt.plot(x, y,linewidth=1)
plt.title('折线图')
plt.show()
```

​	那就可以打开这个工具，输入"011 画图"

![image-20240521000505262](https://github.com/Pulsar-890/python_code_remeber/blob/main/example_pictures/image-20240521000505262.png)

​	然后就会打开这个画图.txt，接下来将上面的代码粘贴进去并保存

![image-20240521000822021](https://github.com/Pulsar-890/python_code_remeber/blob/main/example_pictures/image-20240521000815295.png)

​	然后回到命令行，输入1

![image-20240521001056431](https://github.com/Pulsar-890/python_code_remeber/blob/main/example_pictures/image-20240521001056431.png)

​	以后小明就可以直接方便调用这段代码啦

​	但是小明后来想，只画折线图可不行，他还要把饼图的代码也一并复制下来

```
labels = ['A', 'B', 'C', 'D']
sizes = [30, 25, 15, 30]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('饼图')
plt.show()
```

​	那他就可以输入"001"，对这段代码段进行添加，粘贴进去，保存。再输入1，非常的棒！

![image-20240521001709655](https://github.com/Pulsar-890/python_code_remeber/blob/main/example_pictures/image-20240521001709655.png)

​	小明后来还想，这个名字不够明确，他打算改个名字，改叫plot画图，那也好办，只需要输入"031 plot 画图"，就可以了

![image-20240521001923478](https://github.com/Pulsar-890/python_code_remeber/blob/main/example_pictures/image-20240521001923478.png)

​	后来，小明觉得这个程序设计的不行，我要对它进行魔改，我来定义这个程序应该长什么样。那么，他就输入了"02"直接进入到了这个文件夹里，这样就可以对里面的内容进行手动修改啦。

![image-20240521002143336](https://github.com/Pulsar-890/python_code_remeber/blob/main/example_pictures/image-20240521002143336.png)

​	最后的最后，为了进一步提高效率，我们可以在桌面创建一个txt文本文件，将以下内容写进文本文件中，然后将文件名改为常用程序.bat，就可以在需要的时候双击快速使用啦。

```bat
@echo off
cd convenience.py的文件夹路径
python convenience.py
pause
```

![image-20240521083522533](https://github.com/Pulsar-890/python_code_remeber/blob/main/example_pictures/image-20240521083522533.png)

#### 参与贡献

​	Pulsar

