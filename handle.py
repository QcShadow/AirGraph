import csv
import os

# 定义文件路径
input_file = 'triples.csv'  # 原始文件
output_file = 'triples1.csv'  # 新路径保存输出文件

# 确保输出目录存在
if not os.path.exists('output'):
    os.makedirs('output')

# 打开原始 CSV 文件和新 CSV 文件
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 读取第一行并跳过标题
    header = next(reader)

    # 写入新文件的标题行
    writer.writerow(['entity1', 'relationship', 'entity2'])

    # 逐行处理
    for row in reader:
        if len(row) >= 3:  # 确保每行至少有三列
            try:
                # 去掉第一列的序号部分，例如 "1. Boeing 787-8" -> "Boeing 787-8"
                entity1 = row[0].split('.', 1)[1].strip()  # 通过 . 分割，取第二部分作为实体1
                relationship = row[1].strip()
                entity2 = row[2].strip()

                # 写入新文件
                writer.writerow([entity1, relationship, entity2])
            except IndexError:
                # 如果遇到格式不正确的行，跳过
                print(f"跳过不完整的行: {row}")
                continue

print(f'文件已处理并保存为 {output_file}')


