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

### Sample PDF

A small sample statement `sample_statement.pdf` is provided for quick testing.
Parse it with:

```bash
python parse_subscriptions.py sample_statement.pdf
```

You can regenerate the sample using `python create_sample_pdf.py` if needed.

The script will display lines that look like subscriptions in a table. You can choose a number to remove an entry as a way to "cancel" it. This is a demonstration and does not actually cancel services.
