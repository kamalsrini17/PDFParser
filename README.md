# PDFParser

This repository contains a small script to extract subscription-related lines from a credit card statement PDF.

## Setup

Install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the parser with the path to your PDF statement:

```bash
python parse_subscriptions.py /path/to/statement.pdf
```

The script will display lines that look like subscriptions in a table. You can choose a number to remove an entry as a way to "cancel" it. This is a demonstration and does not actually cancel services.
