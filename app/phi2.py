import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Setup
torch.set_default_device('cuda')

model_id = "TheBloke/TinyLlama-1.1B-Chat-v1.0-GPTQ"

model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
                                             device_map="auto",
                                             trust_remote_code=False,
                                             revision="main")

# tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)

def respond(message):
#   prompt = f"""
# Instruct: {message}\n
# Output:
# """

#   print(prompt)

#   encodeds = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)

#   device = 'cuda'
#   model_inputs = encodeds.to(device)

#   generated_ids = model.generate(**model_inputs, max_new_tokens=1000, do_sample=True)
#   decoded = tokenizer.batch_decode(generated_ids)
#   print(decoded[0])
#   return decoded[0]
  return "Hello"