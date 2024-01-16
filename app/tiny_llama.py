from llama_cpp import Llama

# Setup
llm = Llama(
  model_path="./resources/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
  n_ctx=2048,            # Max token length
  n_threads=4,           # CPU threads
  n_gpu_layers=0,        # No GPU
  chat_format="llama-2"
)

def respond(message):
  output = llm.create_chat_completion(
    messages = [
        {"role": "system", "content": "You are a story writing assistant."},
        {
            "role": "user",
            "content": "Write a story about llamas."
        }
    ]
  )
  print (output)
  return output["choices"][0]["message"]["content"]