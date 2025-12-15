import os
from openai import OpenAI
from PIL import Image
from io import BytesIO
import requests

# ✅ SET YOUR OPENAI API KEY HERE

client = OpenAI()



print("🔮 AstroGuide ready! Ask about your zodiac, chart, or cosmic energy.")
print("Type 'image:' before your request to generate an astrology image.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("✨ You: ").strip()
    if user_input.lower() == "exit":
        print("🌙 Goodbye, star traveler!")
        break

    # --- Image generation ---
    if user_input.lower().startswith("image:"):
        prompt = user_input[len("image:"):].strip()
        print("🌠 Generating your cosmic image...")

        try:
            result = client.images.generate(
                model="dall-e-3",       # use DALL·E 3 for image generation
                prompt=prompt,
                size="1024x1024"
            )

            # Extract the image URL
            image_url = result.data[0].url

            # Download the image
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))

            # Save image
            file_name = "astro_image.png"
            image.save(file_name)
            print(f"✅ Image saved as: {file_name}")

            # Display the image automatically
            image.show()

        except Exception as e:
            print(f"⚠️ Error generating image: {e}")

    # --- Text (chat) response ---
    else:
        try:
            chat = client.chat.completions.create(
                model="gpt-4o-mini",  # or "gpt-4-turbo" if you prefer
                messages=[
                    {"role": "system", "content": "You are AstroGuide, a mystical astrologer who gives cosmic insights."},
                    {"role": "user", "content": user_input}
                ]
            )

            reply = chat.choices[0].message.content
            print(f"🔮 AstroGuide: {reply}\n")

        except Exception as e:
            print(f"⚠️ Error: {e}\n")
