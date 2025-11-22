

from openai import OpenAI


# Read the key from environment
client = OpenAI(api_key="YOUR_API_KEY_HERE")     # add your OpenAI API key here
# Ask the model about the image
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url":"https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0"

                    },
                },
            ],
        }
    ]
)

print(response.choices[0].message.content)
