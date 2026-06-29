from groq_client import client, MODEL
from prompts import VERIFY_PROMPT


def verify(policy, summary):

    prompt = VERIFY_PROMPT.format(
        policy=policy,
        summary=summary
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content