from transformers import pipeline

# Load text generation model
generator = pipeline(
    "text-generation",
    model="google/flan-t5-small"
)

# -------------------------
# Baseline Prompt
# -------------------------
baseline_prompt = "Write a one-paragraph bio of Ada Lovelace."

baseline_output = generator(
    baseline_prompt,
    max_new_tokens=100,
    do_sample=False
)

# -------------------------
# Enhanced Prompt
# -------------------------
enhanced_prompt = """
You are a professional historian.

Write one paragraph (120-150 words) about Ada Lovelace.

Include:
1. Early life
2. Contributions to computing
3. Collaboration with Charles Babbage
4. Why she is considered the first computer programmer

Use clear and simple English.
"""

enhanced_output = generator(
    enhanced_prompt,
    max_new_tokens=150,
    do_sample=False
)

# -------------------------
# Print Results
# -------------------------
print("=" * 70)
print("BASELINE PROMPT")
print("=" * 70)
print(baseline_prompt)
print("\nOUTPUT:\n")
print(baseline_output[0]["generated_text"])

print("\n" + "=" * 70)
print("ENHANCED PROMPT")
print("=" * 70)
print(enhanced_prompt)
print("\nOUTPUT:\n")
print(enhanced_output[0]["generated_text"])