import os
import csv
from pypdf import PdfReader
from PIL import Image
import pytesseract as tess

# Set Tesseract OCR Path
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Paths to your input files
image_path = "images.png"  # Replace with your image file path
pdf_path = "sample-local-pdf.pdf"  # Replace with your PDF file path

# Variables to store extracted text
image_text = ""
pdf_text = ""

# Extract text from the image if it exists
if os.path.exists(image_path):
    try:
        img = Image.open(image_path)
        image_text = tess.image_to_string(img)
        print(f"Text extracted from image: {image_path}")
    except Exception as e:
        print(f"Error processing image: {e}")
else:
    print(f"Image file not found: {image_path}")

# Extract text from the PDF if it exists
if os.path.exists(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            pdf_text += page.extract_text()
        print(f"Text extracted from PDF: {pdf_path}")
    except Exception as e:
        print(f"Error processing PDF: {e}")
else:
    print(f"PDF file not found: {pdf_path}")

# Write extracted text to a CSV file
csv_file = "output.csv"
try:
    with open(csv_file, mode="w", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Source', 'Extracted Text'])  # Header row
        
        # Write image text if extracted
        if image_text:
            writer.writerow(['Image', image_text])
        
        # Write PDF text if extracted
        if pdf_text:
            writer.writerow(['PDF', pdf_text])
        
    print(f"Data successfully written to {csv_file}.")
except Exception as e:
    print(f"Error writing to CSV: {e}")
