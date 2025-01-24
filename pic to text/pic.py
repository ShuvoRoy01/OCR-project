import os
import csv
from pypdf import PdfReader
from PIL import Image
import pytesseract as tess

# Set Tesseract OCR Path
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Input and output paths
input_directory = "E:\pic to text\pic"  # Directory containing images and PDFs
output_csv_file = "output.csv"  # Output CSV file

# Function to extract text from an image
def extract_text_from_image(file_path):
    try:
        img = Image.open(file_path)
        return tess.image_to_string(img)
    except Exception as e:
        print(f"Error processing image {file_path}: {e}")
        return ""

# Function to extract text from a PDF
def extract_text_from_pdf(file_path):
    try:
        text = ""
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
        return text.strip()
    except Exception as e:
        print(f"Error processing PDF {file_path}: {e}")
        return ""

# Process all files in the input directory
try:
    with open(output_csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Source', 'Extracted Text'])  # Header row

        for filename in os.listdir(input_directory):
            file_path = os.path.join(input_directory, filename)
            extracted_text = ""

            # Check if the file is an image
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                print(f"Processing image: {filename}")
                extracted_text = extract_text_from_image(file_path)

            # Check if the file is a PDF
            elif filename.lower().endswith(".pdf"):
                print(f"Processing PDF: {filename}")
                extracted_text = extract_text_from_pdf(file_path)

            # Write extracted text to CSV if any
            if extracted_text:
                writer.writerow([filename, extracted_text])

    print(f"Data successfully written to {output_csv_file}.")
except Exception as e:
    print(f"Error processing files: {e}")
