import PyPDF2
def edit_pdf_metadata(input_pdf, output_pdf, new_metadata, logo_path):
    # Open the input PDF file in read-binary mode
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        # Copy pages and metadata from the input PDF to the output PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Insert a blank page after each page from the original PDF
        pdf_writer.add_blank_page()
        # Update metadata
        pdf_writer.add_metadata(new_metadata)
         # Open the logo image file
        with open(logo_path, 'rb') as logo_file:
            logo_page = PyPDF2.PdfReader(logo_file).pages[0]
            logo_width = logo_page.mediaBox.getWidth()
            logo_height = logo_page.mediaBox.getHeight()
         # Add the logo to each page
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
                pdf_writer.add_page(logo_page)

        # Write the updated metadata to the output PDF file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

input_pdf = 'E:\kuliah rayhan\SEMESTER 6\Forensik Digital\MINGGU 10\JAIIT_0502_0002+online.pdf'
output_pdf = 'E:\kuliah rayhan\SEMESTER 6\Forensik Digital\MINGGU 10\output.pdf'
new_metadata = {'/Title': 'Rancang Bangun Sistem Informasi Perencanaan Pengadaan Barang Menggunakan Framework Laravel', 
'/Author': 'Muhammad Muharrom Al Haromainy, Afina Lina Nurlaili 2, Ryan Purnomo 3', '/Subject': 'New Subject'}
logo_path = 'E:\kuliah rayhan\SEMESTER 6\Forensik Digital\MINGGU 10\TELU.png'


edit_pdf_metadata(input_pdf, output_pdf, new_metadata, logo_path)

