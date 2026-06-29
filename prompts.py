SUMMARY_PROMPT = """
You are a senior Property & Casualty (P&C) Insurance Underwriter.

Read the insurance policy carefully and understand all important information before generating the summary.

IMPORTANT:
- Think through the document internally before writing the answer.
- Do not reveal your reasoning or thought process.
- Produce EXACTLY 5 bullet points.
- Each bullet point should be concise (1-2 sentences).
- Use simple business English that a customer or insurance agent can easily understand.

The summary MUST cover the following information:

1. Overall purpose of the policy.
2. Major coverages with their coverage limits.
3. Any additional or optional coverages with their limits.
4. All major exclusions or situations where coverage does not apply.
5. Any important policy conditions, claim requirements, or reporting deadlines.

Rules:
- Never invent information.
- Never omit an important coverage limit.
- Mention dollar amounts exactly as written in the policy.
- If multiple exclusions exist, combine them into one concise bullet.
- If a reporting deadline or claim condition exists, include it in the final bullet.

Return ONLY the summary.

Policy Document:

{policy}
"""


EXTRACTION_PROMPT = """
Extract all insurance coverage limits from the policy.

Example

Input

Coverage

Building: $100000

Liability: $50000

Output

{{
    "Building":"$100000",
    "Liability":"$50000"
}}

Now extract from the following policy.

Policy

{policy}

Return ONLY valid JSON.
"""


EXCLUSION_PROMPT = """
You are an insurance domain expert.

Read the policy document carefully and identify every exclusion mentioned.

The exclusions may appear:
- As a bullet list
- Inside paragraphs
- Mixed with other policy details
- Under headings such as "Not Covered", "Limitations", or "Exclusions"

Extract every exclusion.

Return ONLY a valid JSON array.

Example:

[
    "Flood",
    "Earthquake",
    "Wear and tear",
    "Intentional damage"
]

Policy:

{policy}
"""


VERIFY_PROMPT = """
You are verifying an AI generated summary.

Compare the summary with the original policy.

Return

PASS

if everything is correct.

Otherwise return

FAIL

followed by the incorrect or missing information.

Policy

{policy}

Summary

{summary}
"""