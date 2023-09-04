import os
import PyPDF2

def remove_metadata(input_pdf_path, output_pdf_path):
    with open(input_pdf_path, 'rb') as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        pdf_writer = PyPDF2.PdfWriter()
        
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
        
        pdf_writer.add_metadata({})

        pdf_writer.add_metadata({'/Producer': 'Microsoft: Print To PDF'})
        
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# Replace this with the path to your directory containing PDF files
pdf_directory = '/Users/andres.baron/Documents/DocumentosAdmisionMaster/cleaning'

output_directory = '/Users/andres.baron/Documents/DocumentosAdmisionMaster/cleaned'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(pdf_directory):
    if filename.lower().endswith('.pdf'):
        input_path = os.path.join(pdf_directory, filename)
        output_path = os.path.join(output_directory, filename)
        
        remove_metadata(input_path, output_path)
        print(f"Removed metadata from {filename}")
