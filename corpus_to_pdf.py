import os
from PyPDF2 import PdfFileMerger

def combine_pdfs(directory_path, output_file_path):
    # Initialize a PdfFileMerger object
    pdf_merger = PdfFileMerger()

    # Loop through files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory_path, filename)
            
            # Append each PDF file to the merger object
            pdf_merger.append(file_path)

    # Write the combined PDF to the specified output file
    with open(output_file_path, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

    print(f"Combined PDF saved to: {output_file_path}")

    # Return the combined PDF file path
    return output_file_path

