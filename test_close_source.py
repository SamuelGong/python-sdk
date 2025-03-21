import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Set the model name or path (adjust to your local checkpoint for Llama 3.1 8B Instruct)
MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"
device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if device == "cuda" else None,
)
model.to(device)
model.eval()
