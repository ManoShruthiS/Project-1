from transformers import pipeline

def generate_stories(model, tokenizer, prompt, genre):
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
    prompt = f"{genre} Story: {prompt}"
    results = generator(prompt, max_length=200, do_sample=True, num_return_sequences=3)
    return [r['generated_text'] for r in results]
