import json
import sys

from extractor import extract
from summarizer import summarize
from verifier import verify


def read_policy(path):

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def extract_exclusions(policy):

    exclusions = []

    lines = policy.splitlines()

    capture = False

    for line in lines:

        text = line.strip()

        if text.lower() == "exclusions":
            capture = True
            continue

        if capture:

            if text == "":
                continue

            if ":" in text:
                break

            exclusions.append(text.strip("- ").strip())

    return exclusions


def main():

    if len(sys.argv) != 2:

        print("Usage:")
        print("python main.py policies/policy1.txt")
        return

    policy = read_policy(sys.argv[1])

    print("Generating summary...")

    summary = summarize(policy)

    print("Extracting coverage...")

    coverage = extract(policy)

    print("Running self verification...")

    verification = verify(policy, summary)

    exclusions = extract_exclusions(policy)

    print("\n========== SUMMARY ==========\n")

    print(summary)

    print("\n========== COVERAGE JSON ==========\n")

    print(json.dumps(coverage, indent=4))

    print("\n========== EXCLUSIONS ==========\n")

    for item in exclusions:
        print("-", item)

    print("\n========== SELF CHECK ==========\n")

    print(verification)


if __name__ == "__main__":
    main()