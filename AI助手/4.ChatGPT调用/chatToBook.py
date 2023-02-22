import openai
import os

# 输入文件路径
input_path = "abc.txt"
# 输出文件路径
output_path = "out.txt"

OPENAI_API_KEY = "你自己的key"

# 将OpenAI API key存储在环境变量中，避免明文存储在代码中
openai.api_key = OPENAI_API_KEY

# 读取文件
with open(input_path, "r", encoding="utf-8") as f:
    input_text = f.read()

# 调用ChatGPT API生成内容
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=input_text,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# 输出生成的内容
output_text = response.choices[0].text
print(output_text)

# 输出结果到文件
with open(output_path, 'w', encoding='UTF-8') as f:
    f.write(output_text)
