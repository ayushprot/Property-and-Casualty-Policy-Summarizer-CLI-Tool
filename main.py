import json
import os
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


def save_output(policy_path, summary, coverage, exclusions, verification):
    """
    Save the generated output to a text file inside the output folder.
    """

    # Create output folder if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Generate output filename
    file_name = os.path.splitext(os.path.basename(policy_path))[0]
    output_path = os.path.join("output", f"{file_name}_output.txt")

    with open(output_path, "w", encoding="utf-8") as file:

        file.write("========== SUMMARY ==========\n\n")
        file.write(summary)
        file.write("\n\n")

        file.write("========== COVERAGE JSON ==========\n\n")
        file.write(json.dumps(coverage, indent=4))
        file.write("\n\n")

        file.write("========== EXCLUSIONS ==========\n\n")

        for item in exclusions:
            file.write(f"- {item}\n")

        file.write("\n========== SELF CHECK ==========\n\n")
        file.write(verification)

    print(f"\nOutput saved successfully to: {output_path}")


def main():

    if len(sys.argv) != 2:

        print("Usage:")
        print("python main.py policies/policy1.txt")
        return

    policy_path = sys.argv[1]

    policy = read_policy(policy_path)

    print("Generating summary...")
    summary = summarize(policy)

    print("Extracting coverage...")
    coverage = extract(policy)

    exclusions = extract_exclusions(policy)

    print("Running self verification...")
    verification = verify(policy, summary)

    # Display output
    print("\n========== SUMMARY ==========\n")
    print(summary)

    print("\n========== COVERAGE JSON ==========\n")
    print(json.dumps(coverage, indent=4))

    print("\n========== EXCLUSIONS ==========\n")
    for item in exclusions:
        print("-", item)

    print("\n========== SELF CHECK ==========\n")
    print(verification)

    # Save output to file
    save_output(
        policy_path,
        summary,
        coverage,
        exclusions,
        verification
    )


if __name__ == "__main__":
    main()