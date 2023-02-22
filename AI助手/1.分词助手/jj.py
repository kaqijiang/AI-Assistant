import jieba

# 输入文件路径
input_path = "abc.txt"
# 输出文件路径
output_path = "output.txt"

# 读取输入文件
with open(input_path, 'r', encoding='UTF-8') as f:
    text = f.read()

# 对文本进行分词
seg_list = jieba.cut(text)

# 将分词结果转换为字符串，以空格分隔
seg_text = ' '.join(seg_list)

# 输出结果到文件
with open(output_path, 'w', encoding='UTF-8') as f:
    f.write(seg_text)