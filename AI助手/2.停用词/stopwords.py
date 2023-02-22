import jieba
import os

# 输入文件路径
input_path = "bbb.txt"
# 输出文件路径
output_path = "output.txt"
# 停用词文件路径
stopwords_path = "./stopwords/baidu_stopwords.txt"
# 中文常用停用词表

# | 词表名 | 词表文件 |
# | - | - |
# | 中文停用词表                | cn_stopwords.txt    |
# | 哈工大停用词表              | hit_stopwords.txt   |
# | 百度停用词表                | baidu_stopwords.txt |
# | 四川大学机器智能实验室停用词库 | scu_stopwords.txt   |

# 加载停用词列表
stopwords = set()
with open(stopwords_path, "r", encoding="utf-8") as f:
    for line in f:
        stopwords.add(line.strip())

# 读取输入文件内容
with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

# 使用jieba进行分词和停用词过滤
words = []
for word in jieba.cut(text):
    if word not in stopwords:
        words.append(word)

# 将结果写入输出文件
with open(output_path, "w", encoding="utf-8") as f:
    f.write(" ".join(words))
    
print("完成停用词过滤并写入文件：%s" % os.path.abspath(output_path))
