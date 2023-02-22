import jieba.posseg as pseg
# from pyhanlp import *

# 输入文件路径
input_path = "abc.txt"
# 输出文件路径
output_path = "output.txt"
# 停用词文件路径
stopwords_path = "./baidu_stopwords.txt"

# 加载停用词列表
with open(stopwords_path, 'r', encoding='UTF-8') as f:
    stopwords = f.read().splitlines()

# 读取输入文件
with open(input_path, 'r', encoding='UTF-8') as f:
    text = f.read()

# 分词和词性标注
words = pseg.cut(text)

# 去除停用词和标点符号
words_filtered = []
for word, flag in words:
    if word not in stopwords and flag != 'x':
        words_filtered.append((word, flag))

# 实体识别
# result = HanLP.parseDependency(''.join([w[0] for w in words_filtered]))
# for word, flag in words_filtered:
#     if flag == 'nr' or flag == 'nt':
#         for term in result.iterator():
#             if word == term.LEMMA and term.DEPREL == "定中关系":
#                 words_filtered.append((term.HEAD.LEMMA, 'n'))

# 输出结果到文件
with open(output_path, 'w', encoding='UTF-8') as f:
    for word, flag in words_filtered:
        f.write(word + ' ' + flag + '\n')
