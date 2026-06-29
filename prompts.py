SUMMARY_PROMPT = """
You are an insurance expert.

Read the insurance policy carefully.

Think step by step internally before answering.

Return ONLY exactly five bullet points in plain English.

Policy:

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