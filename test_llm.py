from mistralai import Mistral

model = "mistral-large-latest"

client = Mistral(api_key='B4HRyk4lAmuY42FNd2oafVjWEFn91mjo')

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "Sklasyfikuj czy podane stwierdzenie jest prawdziwe czy fałszywe: ZSRR ustalił ze Stanami Zjednoczonymi, że #NATO nie będzie się rozszerzać na wschód",
        },
    ]
)

print(chat_response)