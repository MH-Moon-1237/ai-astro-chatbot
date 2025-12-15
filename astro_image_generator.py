import os
import requests
from openai import OpenAI
from PIL import Image as PILImage
from io import BytesIO

# ✅ Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("⚠️ Please set your OPENAI_API_KEY environment variable first!")

client = OpenAI(api_key=api_key)

def generate_astro_image(prompt: str, size="1024x1024"):
    """
    Generate an astrology or zodiac-themed image using DALL·E 3.
    Example: "a glowing Libra constellation with a cosmic nebula background"
    """
    try:
        result = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size
        )
        image_url = result.data[0].url
        print(f"✅ Image generated! Downloading from: {image_url}")

        # Download the image and save locally
        response = requests.get(image_url)
        img = PILImage.open(BytesIO(response.content))
        filename = "astro_image.png"
        img.save(filename)
        print(f"🌠 Saved image as {filename}")

    except Exception as e:
        print(f"⚠️ Error generating image: {e}")

# 🪄 Example usage
if __name__ == "__main__":
    user_prompt = input("🔮 Enter your astrology image idea: ")
    generate_astro_image(user_prompt)
