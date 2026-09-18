from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# ============================================================
# LOAD MODEL
# ============================================================

print("=" * 60)
print("LOADING MODEL")
print("=" * 60)

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model loaded successfully!")


# ============================================================
# FUNCTION TO GENERATE RESPONSE
# ============================================================

def generate_response(prompt):
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=10
    )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return response.strip()


# ============================================================
# TEST DATA
# ============================================================

test_data = [
    ("The product is excellent and works perfectly.", "Positive"),
    ("The application crashes frequently and is frustrating.", "Negative"),
    ("The package arrived yesterday.", "Neutral"),
    ("I am very happy with the quality of this product.", "Positive"),
    ("The service was slow and disappointing.", "Negative")
]


# ============================================================
# ZERO-SHOT CLASSIFICATION
# ============================================================

print("\n" + "=" * 60)
print("ZERO-SHOT CLASSIFICATION")
print("=" * 60)

zero_shot_results = []

for sentence, expected in test_data:

    zero_shot_prompt = f"""
Classify the sentiment of the following sentence.

Choose exactly one label:
Positive
Negative
Neutral

Sentence: {sentence}

Sentiment:
"""

    result = generate_response(zero_shot_prompt)
    zero_shot_results.append(result)

    print("\nSentence:", sentence)
    print("Expected:", expected)
    print("Predicted:", result)


# ============================================================
# FEW-SHOT CLASSIFICATION
# ============================================================

print("\n" + "=" * 60)
print("FEW-SHOT CLASSIFICATION")
print("=" * 60)

few_shot_results = []

for sentence, expected in test_data:

    few_shot_prompt = f"""
Classify the sentiment of a sentence as Positive, Negative, or Neutral.

Examples:

Sentence: I really enjoyed this product.
Sentiment: Positive

Sentence: The product stopped working and I am disappointed.
Sentiment: Negative

Sentence: The order was delivered this morning.
Sentiment: Neutral

Now classify the following sentence.

Sentence: {sentence}
Sentiment:
"""

    result = generate_response(few_shot_prompt)
    few_shot_results.append(result)

    print("\nSentence:", sentence)
    print("Expected:", expected)
    print("Predicted:", result)


# ============================================================
# CALCULATE ACCURACY
# ============================================================

expected_labels = [item[1] for item in test_data]

zero_correct = 0
few_correct = 0

for expected, predicted in zip(expected_labels, zero_shot_results):
    if expected.lower() == predicted.lower():
        zero_correct += 1

for expected, predicted in zip(expected_labels, few_shot_results):
    if expected.lower() == predicted.lower():
        few_correct += 1

zero_accuracy = (zero_correct / len(test_data)) * 100
few_accuracy = (few_correct / len(test_data)) * 100


# ============================================================
# FINAL COMPARISON
# ============================================================

print("\n" + "=" * 60)
print("FINAL COMPARISON")
print("=" * 60)

print("\nExpected Labels:")
print(expected_labels)

print("\nZero-Shot Results:")
print(zero_shot_results)

print("\nFew-Shot Results:")
print(few_shot_results)

print("\nZero-Shot Accuracy:", zero_accuracy, "%")
print("Few-Shot Accuracy:", few_accuracy, "%")

print("\nEvaluation Criteria:")
print("1. Accuracy")
print("2. Consistency")
print("3. Adherence to examples")

print("\nZero-Shot:")
print("- Uses only task instructions.")
print("- No examples are provided.")

print("\nFew-Shot:")
print("- Uses three input-output examples.")
print("- Examples demonstrate the expected classification pattern.")

print("\nExperiment completed successfully.")