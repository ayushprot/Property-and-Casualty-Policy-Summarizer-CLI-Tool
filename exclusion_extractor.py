import json

from groq_client import client, MODEL
from prompts import EXCLUSION_PROMPT


def extract_exclusions(policy):

    prompt = EXCLUSION_PROMPT.format(policy=policy)

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

    text = response.choices[0].message.content.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")

    text = text.replace("```", "").strip()

    return json.loads(text)