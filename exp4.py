# Experiment No. 4
# Diagnosing Prompt Failures & Edge Cases

print("=" * 70)
print("PROMPT FAILURE DIAGNOSIS AND IMPROVEMENT")
print("=" * 70)


def check_prompt(prompt):
    """Identify common problems in a prompt."""

    problems = []
    text = prompt.lower()

    # 1. Ambiguity
    ambiguous_words = ["it", "this", "that", "good", "best", "short"]
    words = text.replace(".", "").replace(",", "").split()

    if any(word in words for word in ambiguous_words):
        problems.append("Ambiguity")

    # 2. Missing Context
    context_words = [
        "student", "customer", "employee", "company",
        "topic", "document", "paragraph"
    ]

    if not any(word in text for word in context_words):
        problems.append("Missing Context")

    # 3. Contradictory Instructions
    if "exactly" in text and ("brief" in text or "short" in text):
        problems.append("Contradictory Instructions")

    # 4. Formatting Error
    if "table" in text and "columns" not in text:
        problems.append("Formatting Error")

    return problems


# ----------------------------------------------------------
# Example 1: Ambiguity
# ----------------------------------------------------------

prompt1 = "Write about it in a good way."

print("\n1. AMBIGUITY")
print("Original Prompt:")
print(prompt1)

problems = check_prompt(prompt1)
print("Detected Problem:", ", ".join(problems))

improved1 = """
Write a simple 100-word explanation of Artificial Intelligence.
Explain its meaning, two applications, and one advantage.

Use language suitable for first-year engineering students.
"""

print("\nImproved Prompt:")
print(improved1)


# ----------------------------------------------------------
# Example 2: Missing Context
# ----------------------------------------------------------

prompt2 = "Explain machine learning."

print("\n2. MISSING CONTEXT")
print("Original Prompt:")
print(prompt2)

problems = check_prompt(prompt2)
print("Detected Problem:", ", ".join(problems))

improved2 = """
Explain Machine Learning to B.Tech CSE students.
Define Machine Learning, describe supervised and unsupervised learning,
and give one real-world example for each.

Use simple technical language and limit the answer to 150 words.
"""

print("\nImproved Prompt:")
print(improved2)


# ----------------------------------------------------------
# Example 3: Contradictory Instructions
# ----------------------------------------------------------

prompt3 = "Write a short answer with exactly 500 words."

print("\n3. CONTRADICTORY INSTRUCTIONS")
print("Original Prompt:")
print(prompt3)

problems = check_prompt(prompt3)
print("Detected Problem:", ", ".join(problems))

improved3 = """
Write an explanation of Internet of Things in exactly 150 words.
Cover its definition, major components, and two applications.
Use clear and concise language.
"""

print("\nImproved Prompt:")
print(improved3)


# ----------------------------------------------------------
# Example 4: Formatting Error
# ----------------------------------------------------------

prompt4 = "Give student details in a table."

print("\n4. FORMATTING ERROR")
print("Original Prompt:")
print(prompt4)

problems = check_prompt(prompt4)
print("Detected Problem:", ", ".join(problems))

improved4 = """
Provide student details in a table with the following columns:
Roll Number, Name, Department, and CGPA.

Use one row for each student.
"""

print("\nImproved Prompt:")
print(improved4)


# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("""
Prompt Failure          Improvement
----------------------------------------------------------------------
Ambiguity               Specify exactly what is required
Missing Context         Provide background and target audience
Contradiction           Remove conflicting instructions
Formatting Error        Clearly specify the required format
----------------------------------------------------------------------
""")

print("Experiment completed successfully.")