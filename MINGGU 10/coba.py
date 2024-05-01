import PyPDF2

def edit_pdf_metadata(input_pdf, output_pdf, new_metadata):
    # Open the input PDF file in read-binary mode
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        # Add two empty pages at the beginning
        pdf_writer.add_blank_page()
        pdf_writer.add_blank_page()

        # Copy pages from the input PDF to the output PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Add two empty pages at the end
        pdf_writer.add_blank_page()
        pdf_writer.add_blank_page()

        # Update metadata
        pdf_writer.add_metadata(new_metadata)

        # Write the updated metadata to the output PDF file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

input_pdf = 'E:\kuliah rayhan\SEMESTER 6\Forensik Digital\MINGGU 10\JAIIT_0502_0002+online.pdf'
output_pdf = 'E:\kuliah rayhan\SEMESTER 6\Forensik Digital\MINGGU 10/output.pdf'
new_metadata = {'/Title': 'Rancang Bangun Sistem Informasi Perencanaan Pengadaan Barang Menggunakan Framework Laravel', 
                '/Author': 'Muhammad Muharrom Al Haromainy, Afina Lina Nurlaili 2, Ryan Purnomo 3', 
                '/Subject': 'New Subject'}

edit_pdf_metadata(input_pdf, output_pdf, new_metadata)
