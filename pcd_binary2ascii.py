import os
import open3d as o3d

def binary_to_ascii(pcd_name):
    if not os.path.isfile(pcd_name):
        print(f"文件不存在: {pcd_name}")
        return
    try:
        # 读取binary格式的PCD文件
        pcd = o3d.io.read_point_cloud(pcd_name)
        # 将点云从binary格式转换为ASCII格式
        o3d.io.write_point_cloud(pcd_name.rsplit('.', 1)[0] + "_ascii.pcd", pcd, write_ascii=True)
    except Exception as e:
        print(f"转换失败: {e}")

def ascii_to_binary(pcd_name):
    if not os.path.isfile(pcd_name):
        print(f"文件不存在: {pcd_name}")
        return
    try:
        # 读取ascii格式的PCD文件
        pcd = o3d.io.read_point_cloud(pcd_name)
        # 将点云从ascii格式转换为binary格式
        o3d.io.write_point_cloud(pcd_name.rsplit('.', 1)[0] + "_binary.pcd", pcd, write_ascii=False)
    except Exception as e:
        print(f"转换失败: {e}")

def convert_single_file():
    pcd_name = input("请输入PCD文件名: ")
    convert_file(pcd_name+ ".pcd")

def convert_directory(conversion_type):
    directory = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(directory):
        if filename.endswith(".pcd"):
            if conversion_type == '1':
                binary_to_ascii(os.path.join(directory, filename))
                print(f"文件已转换为ASCII格式: {filename.rsplit('.', 1)[0]}_ascii.pcd")
            elif conversion_type == '2':
                ascii_to_binary(os.path.join(directory, filename))
                print(f"文件已转换为Binary格式: {filename.rsplit('.', 1)[0]}_binary.pcd")

def convert_file(pcd_name):
    print("选择转换类型:")
    print("1. Binary to ASCII")
    print("2. ASCII to Binary")
    choice = input("请输入选择 (1 或 2): ")

    if choice not in ['1', '2']:
        print("无效选择，请输入1或2")
        return

    if choice == '1':
        binary_to_ascii(pcd_name)
        print(f"文件已转换为ASCII格式: {pcd_name.rsplit('.', 1)[0]}_ascii.pcd")
    elif choice == '2':
        ascii_to_binary(pcd_name)
        print(f"文件已转换为Binary格式: {pcd_name.rsplit('.', 1)[0]}_binary.pcd")

def main():
    print("选择转换模式:")
    print("1. 单个文件转换")
    print("2. 批量转换文件夹内的PCD文件")
    mode = input("请输入选择 (1 或 2): ")

    if mode == '1':
        convert_single_file()
    elif mode == '2':
        print("选择转换类型:")
        print("1. Binary to ASCII")
        print("2. ASCII to Binary")
        conversion_type = input("请输入选择 (1 或 2): ")

        if conversion_type not in ['1', '2']:
            print("无效选择，请输入1或2")
            return

        convert_directory(conversion_type)
    else:
        print("无效选择，请输入1或2")

if __name__ == "__main__":
    main()