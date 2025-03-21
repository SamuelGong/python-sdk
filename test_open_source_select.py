import torch
from transformers import (AutoModelForCausalLM,
                          AutoTokenizer, BitsAndBytesConfig)

from test_closed_source_select import messages


if __name__ == '__main__':
    model_name = "meta-llama/Meta-Llama-3-8B-Instruct"  # context length: 8k
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # not available for low version of transformers' PreTrainedTokenizerFast
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    num_tokens = len(inputs[0])
    print(f"Length of prompt in tokens: {num_tokens}")

    model = AutoModelForCausalLM.from_pretrained(
        model_name
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
    full_output = tokenizer.decode(outputs[0][num_tokens:], skip_special_tokens=True)
    print(full_output)
    # expected output: FINAL_ANSWER: get_alerts
