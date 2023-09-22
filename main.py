from api import get_setted_up_model
import openai

openai.api_key = "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"

def get_response_from_llm(matrix):
    messages = get_setted_up_model(openai)
    messages.append({"role": "user", "content": matrix})
    #print(messages)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    return reply

reply = get_response_from_llm("0UUU,1UUU,2UUU")
print(reply)