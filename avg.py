import os

def read_columns(file_path):
    first_two_columns = []
    third_column = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 3:
                first_two_columns.append(columns[:2])
                third_column.append(float(columns[2]))
    return first_two_columns, third_column

def main(input_directory, output_file):
    all_third_columns = []
    file_count = 0
    first_two_columns = []

    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_directory, filename)
            if not first_two_columns:
                first_two_columns, third_column = read_columns(file_path)
            else:
                _, third_column = read_columns(file_path)
            if len(all_third_columns) < len(third_column):
                all_third_columns.extend([0] * (len(third_column) - len(all_third_columns)))
            for i in range(len(third_column)):
                all_third_columns[i] += third_column[i]
            file_count += 1
    
    if file_count == 0:
        print("No files found.")
        return
    
    average_third_column = [value / file_count for value in all_third_columns]
    
    with open(output_file, 'w') as out_file:
        for i in range(len(average_third_column)):
            if i < len(first_two_columns):
                out_file.write(f"{first_two_columns[i][0]} {first_two_columns[i][1]} {average_third_column[i]}\n")
            else:
                out_file.write(f"NA NA {average_third_column[i]}\n")
    
    print(f"Averages saved to {output_file}")

# 使用你文件所在的目录路径和输出文件路径
input_directory_path = './avg'
output_file_path = 'avg.txt'
main(input_directory_path, output_file_path)