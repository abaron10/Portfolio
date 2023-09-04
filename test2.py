import PyPDF2

def split_pdf(input_pdf, output_folder):
    pdf = PyPDF2.PdfReader(input_pdf)

    for page_num in range(len(pdf.pages)):
        output_page = PyPDF2.PdfWriter()
        output_page.add_page(pdf.pages[page_num])
        
        output_file_path = f"{output_folder}/page_{page_num + 1}.pdf"
        with open(output_file_path, "wb") as output_file:
            output_page.write(output_file)
            print(f"Page {page_num + 1} saved as {output_file_path}")

if __name__ == "__main__":
    input_pdf_path = "/Users/andres.baron/Downloads/scan.pdf"
    output_folder_path = "/Users/andres.baron/Downloads/Carlos"
    split_pdf(input_pdf_path, output_folder_path)
    print("PDF splitting complete.")