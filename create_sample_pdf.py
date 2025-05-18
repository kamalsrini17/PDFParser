lines = [
    "05/01/2025 Coffee Shop $5.00",
    "05/02/2025 Streaming Service Subscription $9.99",
    "05/03/2025 Cloud Storage Monthly $0.99",
    "05/04/2025 Grocery Store $50.00",
    "05/05/2025 Recurring donation $20.00",
]

text_stream = "BT\n/F1 12 Tf\n50 750 Td\n"
for line in lines:
    text_stream += f"({line}) Tj\n0 -15 Td\n"
text_stream += "ET\n"

objects = []
objects.append("1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
objects.append("2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n")
objects.append("3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>\nendobj\n")
objects.append(f"4 0 obj\n<< /Length {len(text_stream)} >>\nstream\n{text_stream}endstream\nendobj\n")
objects.append("5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n")

content = ["%PDF-1.4\n"]
offsets = []
current_offset = len(content[0])
for obj in objects:
    offsets.append(current_offset)
    content.append(obj)
    current_offset += len(obj)
content.append(f"xref\n0 {len(objects)+1}\n")
content.append("0000000000 65535 f \n")
for off in offsets:
    content.append(f"{off:010d} 00000 n \n")
content.append(f"trailer\n<< /Root 1 0 R /Size {len(objects)+1} >>\nstartxref\n{current_offset}\n%%EOF")

with open("sample_statement.pdf", "wb") as f:
    f.write("".join(content).encode("latin-1"))
print("Created sample_statement.pdf")
