# 说明

## 环境

- python3.11

- open3d

- numpy

## 文件说明

`pcd_binary2ascii.py` binary格式和ascii格式的pcd文件互转

> 需要安装`open3d`
> 
> `pip install open3d`

`pcd_binary2ascii.exe` 可直接运行的exe文件

`pcd2txt.m` Matlab程序, 转换单个文件须定义输入输出名称

```matlab
%输入和输出文件路径及名称
input_pcd = '7_ascii.pcd';
output_txt = 'output.txt';
```

`pcd2txt.py` Python程序, 转换单个文件需输入名称(无拓展名). 也可批量转换本文件夹内的pcd文件(需ascii格式)

> 须安装`numpy`
> 
> `pip install numpy`

`pcd2txt.exe` 可直接运行的exe文件


## 使用方法

先将binary格式的pcd文件转换为ascii格式

> 与pcd_binary2ascii.exe放在同一文件夹下, 运行并选择1单独转换2批量转换

再把ascii类型的pcd文件放在单独的文件夹内（与pcd2txt.exe文件一起），再运行pcd2txt.exe， 即可转换为txt文件同时剔除无效值点（nan）

> 也可选择1单独 2批量(当前文件夹内的所有pcd文件--binary格式会转换失败)