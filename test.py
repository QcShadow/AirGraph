from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

# 登录 Hugging Face API
login("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")

# 设置模型名称，注意如果模型名称与此不同，请根据实际情况修改
model_name = "meta/llama-3.1-70b-instruct"

# 加载模型和 tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 输入文本
input_text = "你会中文吗"
inputs = tokenizer(input_text, return_tensors="pt")

# 生成输出
outputs = model.generate(inputs['input_ids'], max_length=150)

# 输出生成的文本
print(tokenizer.decode(outputs[0], skip_special_tokens=True))





