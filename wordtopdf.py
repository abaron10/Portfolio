
import os
from docx2pdf import convert

def batch_convert_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".docx"):
            input_docx_file = os.path.join(input_folder, filename)
            output_pdf_file = os.path.join(output_folder, filename.replace(".docx", ".pdf"))

            # Print the paths for debugging
            print("Converting:", input_docx_file, "->", output_pdf_file)

            convert(input_docx_file, output_pdf_file)

if __name__ == "__main__":
    input_folder = "/Users/andres.baron/Downloads/pdfsDario"  # Replace with the path to your input folder
    output_folder = "/Users/andres.baron/Downloads/pdfsDario2"  # Replace with the path to your output folder
    
    batch_convert_folder(input_folder, output_folder)
    print("Batch conversion complete.")
