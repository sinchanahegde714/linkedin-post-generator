import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# ✅ Load API key safely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ Missing GROQ_API_KEY in .env file")

client = Groq(api_key=GROQ_API_KEY)

# -----------------------------------------------------
# ✅ Build prompt
# -----------------------------------------------------
def build_prompt(topic, length, language, tone="professional"):
    return f"""
You are a LinkedIn post writing expert.

Write a {length} LinkedIn post about **{topic}** in **{language}** using a **{tone}** tone.

Rules:
- Should sound human, engaging, structured
- Include short paragraphs & bullet points
- Add a hook, insights, and a final question
- DO NOT add hashtags
"""

# -----------------------------------------------------
# ✅ MAIN POST GENERATION
# -----------------------------------------------------
def generate_groq_post(topic, length, language, tone="professional"):
    prompt = build_prompt(topic, length, language, tone)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

# -----------------------------------------------------
# ✅ HASHTAG GENERATION
# -----------------------------------------------------
def generate_groq_hashtags(topic):
    prompt = f"""
Generate 8 short trending LinkedIn hashtags for the topic: {topic}
Rules:
- Return ONLY hashtags
- Space separated
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    raw = response.choices[0].message.content.strip()
    tags = raw.split()

    # Ensure all tags start with #
    tags = [t if t.startswith("#") else f"#{t}" for t in tags]

    return tags[:8]
