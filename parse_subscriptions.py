import sys
import re
import pdfplumber
from tabulate import tabulate

SUBSCRIPTION_KEYWORDS = [
    "subscription",
    "recurring",
    "monthly",
    "autopay",
]

def extract_text(pdf_path: str) -> str:
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def parse_subscriptions(text: str):
    lines = text.splitlines()
    matches = []
    for line in lines:
        line_lc = line.lower()
        if any(keyword in line_lc for keyword in SUBSCRIPTION_KEYWORDS):
            matches.append(line.strip())
    return matches

def main(pdf_path: str):
    text = extract_text(pdf_path)
    subscriptions = parse_subscriptions(text)
    if not subscriptions:
        print("No subscriptions found.")
        return
    table = [[idx + 1, sub] for idx, sub in enumerate(subscriptions)]
    print(tabulate(table, headers=["#", "Line"], tablefmt="github"))
    while True:
        choice = input("Enter the number of the subscription to cancel (or 'q' to quit): ")
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print("Invalid choice.")
            continue
        idx = int(choice) - 1
        if idx < 0 or idx >= len(subscriptions):
            print("Invalid choice.")
            continue
        print(f"Canceling subscription: {subscriptions[idx]}")
        subscriptions.pop(idx)
        if not subscriptions:
            print("No more subscriptions.")
            break
        table = [[i + 1, sub] for i, sub in enumerate(subscriptions)]
        print(tabulate(table, headers=["#", "Line"], tablefmt="github"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} path/to/statement.pdf")
        sys.exit(1)
    main(sys.argv[1])
