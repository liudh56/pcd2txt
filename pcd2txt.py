import os
import numpy as np


def pcd2txt(input_pcd, output_txt):
    # 读取PCD文件
    try:
        with open(input_pcd, 'r') as file:
            data_lines = file.readlines()
    except IOError:
        raise IOError(f"无法打开文件: {input_pcd}")

    # 初始化结果数组
    result = []

    # 解析数据行
    for line in data_lines:
        # 跳过以#开头的注释行和空行
        if line.startswith('#') or not line.strip():
            continue
        try:
            values = list(map(float, line.split()))
            if len(values) >= 3:
                x, y, z = values[:3]
                if np.isfinite(x) and np.isfinite(y) and np.isfinite(z):
                    result.append([x, y, z])
            else:
                print(f'解析失败的行: {line.strip()}')
        except ValueError:
            print(f'无法转换为浮点数的行: {line.strip()}')

    # 检查结果是否为空
    if not result:
        print('结果数组为空，未找到有效数据')

    # 保存结果到TXT文件
    np.savetxt(output_txt, result, delimiter=' ')

def convert_single_file():
    input_pcd = input("请输入PCD文件名: ")
    output_dir = r"./avg"
    output_txt = os.path.join(output_dir, input_pcd.rsplit('.', 1)[0] + ".txt")
    pcd2txt(input_pcd, output_txt)
    print(f"文件已转换并保存为: {output_txt}")

def convert_directory():
    directory = r"./2txt"
    output_dir = r"./avg"
    for filename in os.listdir(directory):
        if filename.endswith(".pcd"):
            input_pcd = os.path.join(directory, filename)
            output_txt = os.path.join(output_dir, filename.rsplit('.', 1)[0] + ".txt")
            pcd2txt(input_pcd, output_txt)
            print(f"文件已转换并保存为: {output_txt}")

def main():
    print("选择转换类型:")
    print("1. 单个文件转换")
    print("2. 批量转换文件夹内的PCD文件")
    choice = input("请输入选择 (1 或 2): ")

    if choice == '1':
        convert_single_file()
    elif choice == '2':
        convert_directory()
    else:
        print("无效选择，请输入1或2")

if __name__ == "__main__":
    main()