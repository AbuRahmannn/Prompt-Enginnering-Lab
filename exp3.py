from gpt4all import GPT4All

print("=" * 70)
print("Loading Model...")
print("=" * 70)

# Downloads the model automatically the first time
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

prompts = [
    "Summarize the plot of Shakespeare's Romeo and Juliet in two sentences.",

    """Summarize the plot of Shakespeare's Romeo and Juliet in exactly two sentences.
Use simple language suitable for high school students.""",

    """Summarize the plot of Shakespeare's Romeo and Juliet in exactly two sentences.
Use simple language suitable for high school students.
Mention the setting (Verona, Italy) and the central theme of love and conflict."""
]

print("\n")
print("=" * 70)
print("ITERATIVE PROMPT REFINEMENT")
print("=" * 70)

with model.chat_session():
    for i, prompt in enumerate(prompts, start=1):

        print("\n")
        print("=" * 70)
        print("Prompt", i)
        print("=" * 70)

        print(prompt)

        response = model.generate(
            prompt,
            max_tokens=120
        )

        print("\nOutput")
        print("-" * 70)
        print(response)

print("\nExperiment Completed Successfully.")