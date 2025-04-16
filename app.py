import openai

openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "NULL"


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = ";",
        messages = [{"role":"user","content":prompt}]
        )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        human_input = input("human")

        if human_input.lower() in ["quit","exit","bye"]:
            break

        response = chat_with_gpt (human_input)

        print("chatbot: ",response)
