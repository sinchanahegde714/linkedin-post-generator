from groq_llm import generate_groq_post, generate_groq_hashtags

def generate_post(topic, length, language):
    # Main post
    post_text = generate_groq_post(topic, length, language)

    # Hashtags
    hashtags = generate_groq_hashtags(topic)

    # Basic engagement metric
    engagement = round(len(post_text) / 250, 2)

    return {
        "post": post_text,
        "hashtags": hashtags,
        "engagement": engagement
    }
