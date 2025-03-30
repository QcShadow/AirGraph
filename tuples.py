import time
import re
import PyPDF2
import csv
from openai import OpenAI

def read_text_from_pdf(pdf_path):
    # 打开 PDF 文件
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
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

def triples_from_LLM(text):
    prompt = f"""
    Please extract the entity relationship entity triplet related to the accident from the following text, format: Entity 1 - Relationship - Entity 2, with the requirement to include as many as possible
    text：{text}
    """
    completion = client.chat.completions.create(
      model="meta/llama-3.1-70b-instruct",
      messages=[{"role":"user","content":prompt}],
      temperature=0.3,
      top_p=0.9,
      max_tokens=4096,
      # stream=True
    )
    triples_text = completion.choices[0].message.content
    triples = []
    lines = triples_text.strip().split("\n")
    for line in lines:
        if " - " in line :
            entity1, relation, entity2 = line.split(" - ")
            triples.append([entity1.strip(), relation.strip(), entity2.strip()])
    return triples

triples = triples_from_LLM(text)
for triple in triples:
    print(triple)

def save_triples_as_csv(triples,file):
    with open(file,'w',newline='',encoding='utf-8')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["实体1", "关系", "实体2"])
        for triple in triples:
            writer.writerow(triple)

save_triples_as_csv(triples,'triples.csv')