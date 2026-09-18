print("=" * 70)
print("ROLE-BASED AND NEGATIVE PROMPTING")
print("=" * 70)

# ------------------------------------------------------------
# TOPIC
# ------------------------------------------------------------

topic = "Cybersecurity"


# ------------------------------------------------------------
# ROLE-BASED PROMPT
# ------------------------------------------------------------

role_prompt = """
You are a cybersecurity instructor teaching B.Tech students.

Explain the importance of cybersecurity in simple language.

Include:
1. Definition
2. Major threats
3. Preventive measures
4. Real-world example
"""

print("\n" + "=" * 70)
print("ROLE-BASED PROMPT")
print("=" * 70)

print(role_prompt)


# ------------------------------------------------------------
# SIMULATED ROLE-BASED RESPONSE
# ------------------------------------------------------------

role_response = """
Cybersecurity is the practice of protecting computers, networks,
applications, and data from unauthorized access and attacks.

Major threats include:
1. Phishing attacks
2. Malware
3. Password attacks

Preventive measures include using strong passwords, updating
software regularly, using secure networks, and avoiding
suspicious links.

A real-world example is when an attacker sends a fake email
to trick a user into revealing a password.
"""

print("\nROLE-BASED OUTPUT:")
print(role_response)


# ------------------------------------------------------------
# NEGATIVE PROMPT
# ------------------------------------------------------------

negative_prompt = """
Explain cybersecurity in simple language.

Do not mention:
- Company names
- Brand names
- Product names

Do not use complicated technical jargon.
Do not exceed 150 words.
"""

print("=" * 70)
print("NEGATIVE PROMPT")
print("=" * 70)

print(negative_prompt)


# ------------------------------------------------------------
# SIMULATED NEGATIVE-PROMPT RESPONSE
# ------------------------------------------------------------

negative_response = """
Cybersecurity means protecting computers, networks, and information
from unauthorized access and harmful activities.

Common threats include phishing, malware, weak passwords, and
unauthorized access.

People can improve security by using strong passwords, enabling
multi-factor authentication, updating software, avoiding suspicious
links, and protecting confidential information.

Cybersecurity is important because it helps protect personal,
academic, financial, and organizational information.
"""

print("\nNEGATIVE-PROMPT OUTPUT:")
print(negative_response)


# ------------------------------------------------------------
# CHECK FOR UNWANTED CONTENT
# ------------------------------------------------------------

print("=" * 70)
print("NEGATIVE PROMPT EVALUATION")
print("=" * 70)

# Restricted company/brand names
restricted_words = [
    "google",
    "microsoft",
    "apple",
    "amazon",
    "facebook",
    "instagram"
]

found = []

text = negative_response.lower()

for word in restricted_words:
    if word in text:
        found.append(word)

if len(found) == 0:
    print("No restricted company or brand names found.")
else:
    print("Restricted names found:", found)


# ------------------------------------------------------------
# WORD COUNT CHECK
# ------------------------------------------------------------

word_count = len(negative_response.split())

print("Word count:", word_count)

if word_count <= 150:
    print("Response is within the 150-word limit.")
else:
    print("Response exceeds the 150-word limit.")


# ------------------------------------------------------------
# COMBINED ROLE-BASED + NEGATIVE PROMPT
# ------------------------------------------------------------

combined_prompt = """
You are a cybersecurity instructor teaching B.Tech students.

Explain the importance of cybersecurity in simple language.

Include:
1. Definition
2. Three major threats
3. Three preventive measures
4. One real-world example

Do not mention any company or brand names.
Do not use complicated technical jargon.
Keep the answer within 150 words.
"""

print("\n" + "=" * 70)
print("COMBINED ROLE-BASED + NEGATIVE PROMPT")
print("=" * 70)

print(combined_prompt)


# ------------------------------------------------------------
# COMPARISON
# ------------------------------------------------------------

print("=" * 70)
print("COMPARISON")
print("=" * 70)

print("""
ROLE-BASED PROMPT:
- Establishes a specific persona.
- Controls the perspective and style of the response.
- Example: Cybersecurity instructor.

NEGATIVE PROMPT:
- Specifies what should be avoided.
- Helps suppress unwanted content.
- Example: Do not mention company or brand names.

COMBINED PROMPT:
- Uses both role instructions and restrictions.
- Provides greater control over the generated response.
""")


# ------------------------------------------------------------
# END
# ------------------------------------------------------------

print("=" * 70)
print("Experiment completed successfully.")
print("=" * 70)
