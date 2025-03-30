import time
import re
import PyPDF2

from openai import OpenAI

def read_text_from_pdf(pdf_path):
    # 打开 PDF 文件
    with open(pdf_path, "rb") as file:
        # 创建 PDF 读取器
        reader = PyPDF2.PdfReader(file)
        # 获取 PDF 页数
        num_pages = len(reader.pages)
        text = ""
        # 遍历每一页，提取文本
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s.,;!?]", "", text)
    return text.strip()

pdf_path = "D:\\桌面\\文献\\香港MAX-Investigation Report 3-2023.pdf"
start_time = time.time()

text = read_text_from_pdf(pdf_path)
text = clean_text(text)

end_time = time.time()
run_time = end_time-start_time
# print(text)
print(f"用时：{run_time}s")

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="meta/llama-3.1-70b-instruct",
  messages=[{"role":"user","content":"请用回答事故的详细经过和原因"+text}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")