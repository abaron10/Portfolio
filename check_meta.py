import PyPDF2

def check_pdf_metadata(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Accessing metadata using PyPDF2
        metadata = pdf_reader.info
        for key, value in metadata.items():
            print(f"{key}: {value}")
            
        print("Custom Metadata:")
        for xmp_key in pdf_reader.metadata:
            print(f"{xmp_key}: {pdf_reader.metadata[xmp_key]}")

# Replace this with the path to your PDF file
pdf_path = '/Users/andres.baron/Documents/DocumentosAdmisionMaster/Cartas Recomendacion Andres Barón - Carlos Lozano/University of Columbia - Recommendation Letter Andres Baron.pdf'

check_pdf_metadata(pdf_path)