from groq_client import client, MODEL
from prompts import SUMMARY_PROMPT


def summarize(policy):

    prompt = SUMMARY_PROMPT.format(policy=policy)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content