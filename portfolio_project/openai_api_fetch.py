import os
import json
import openai


openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Say HI"}
    ]
)

answer = response.choices[0].message['content']  #access to content

print(answer)


# openai.api_key = "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"

# response = openai.ChatCompletion.create(
#     model = "gpt-3.5-turbo",
#     message = [
#         {"role": "user", "content": "Say HI"}
#         ]
# )
# answer = response.choices[0].message["content"]

# print (answer)


#result.insert("0.0", answer)

