api_key = "AQ.addd yourerrrrrrrrr"


from google import genai

client = genai.Client(api_key = api_key)

chat = client.chats.create(model="gemini-3.5-flash-lite")

response = chat.send_message("wraite a prorgam to add two numbers in simple code in pythn.")

print(response.text)
