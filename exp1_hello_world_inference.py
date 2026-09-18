from transformers import pipeline

# Load a text generation pipeline
generator = pipeline(
    "text-generation",
    model="sshleifer/tiny-gpt2"
)

# Give a prompt
prompt = "Hello, World!"

# Generate response
response = generator(
    prompt,
    max_new_tokens=50,
    do_sample=True,
    temperature=0.7
)

# Print output
print("Prompt:")
print(prompt)

print("\nGenerated Text:")
print(response[0]["generated_text"])
