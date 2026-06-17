import os
from dotenv import load_dotenv
from groq import Groq

# 从 .env 文件加载环境变量
load_dotenv()

# 创建 Groq 客户端，读取 GROQ_API_KEY
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# 发送第一次 API 请求
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",   # Groq 上运行的 Llama 模型
    messages=[
        {"role": "user", "content": "What is a neural network in one sentence?"}
    ]
)

# 打印返回结果
print(response.choices[0].message.content)
