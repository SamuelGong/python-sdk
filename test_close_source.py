import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from test_open_source_select import messages


if __name__ == '__main__':
    # model_name = "meta-llama/Llama-3.1-8B-Instruct"
    model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    print(f"Length of prompt in tokens: {len(inputs[0])}")

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
    )
    model.to(device)
    model.eval()

    max_new_tokens = 256
    do_sample = True
    temperature = 1.0
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        temperature=temperature,
        pad_token_id=tokenizer.eos_token_id,
    )
    full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # response = full_output[len(prompt):].strip()
    print(full_output)
