from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import time

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEN_AI_API_KEY")

client = genai.Client(api_key=API_KEY)
print("Google Generative AI client initialized.")

prompt = "Create a vintage postcard using the image uploaded. Add the text 'Greetings' in a retro font."

image = Image.open("utah.jpg")
image = image.resize((256, 256))  #resize

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents=[image, prompt]
    )
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            image.save("generated_postcard_image.png")
            print("Image saved as generated_postcard_image.png")
    time.sleep(1)
except Exception as e:
    print("Error generating content:", e)

