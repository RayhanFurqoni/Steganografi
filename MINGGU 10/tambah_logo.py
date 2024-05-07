import PyPDF2
import base64
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io


def create_blank_pages(logo_path, page_size=letter):
    # Buat halaman dengan logo
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=page_size)
    
    # mengatur size iamge logo
    can.drawImage(logo_path, 0, 0, width=page_size[0], height=page_size[1])
    
    # Tambahkan lapisan putih untuk menutupi logo
    can.setFillColorRGB(1, 1, 1)  
    can.rect(0, 0, page_size[0], page_size[1], fill=1, stroke=0)  # Menutupi logo dengan lapisan putih
    
    can.showPage()
    can.save()

    packet.seek(0)  
    new_pdf = PyPDF2.PdfReader(packet)
    
    return new_pdf.pages[0]


def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():  # Hanya ubah karakter alfabet
            # Tentukan apakah karakter besar atau kecil
            start = ord('A') if char.isupper() else ord('a')
            # Pergeseran dengan wrap-around (mod 26)
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result.append(new_char)
        else:
            result.append(char)  # Karakter non-alfabet tetap sama
    return ''.join(result)


def encode_metadata_base64(metadata):
    """Encode metadata dengan Base64."""
    encoded_metadata = {}
    for key, value in metadata.items():
        encoded_str = base64.b64encode(caesar_cipher(value, 4).encode()).decode()
        encoded_metadata[key] = encoded_str
    return encoded_metadata


def edit_pdf_with_modifications(input_pdf, output_pdf, new_metadata, logo_path):

    # membaca PDF asli
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        # Tambahkan halaman dengan logo yang disembunyikan
        hidden_logo_page = create_blank_pages(logo_path)
        pdf_writer.add_page(hidden_logo_page)

        # Tambahkan semua halaman dari input PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Tambahkan halaman kosong 
        pdf_writer.add_page(create_blank_pages(logo_path))

        # Encode metadata baru dengan Caesar cipher dan Base64
        encrypted_metadata = encode_metadata_base64(new_metadata)

        # Tambahkan metadata yang sudah dienkode
        pdf_writer.add_metadata(encrypted_metadata)

        # Tulis ke file output
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)


# Contoh penggunaan
input_pdf = 'E:\kuliah rayhan\SEMESTER 6\Forensik Digital\MINGGU 10\JAIIT_0502_0002+online.pdf'
output_pdf = 'output.pdf'
logo_path = 'TELU.png'    # Ganti dengan path ke file logo Anda
new_metadata = {'/Title': 'Rancang Bangun Sistem Informasi Perencanaan Pengadaan Barang Menggunakan Framework Laravel', 
'/Author': 'Muhammad Muharrom Al Haromainy, Afina Lina Nurlaili 2, Ryan Purnomo 3', '/Subject': 'New Subject'}

edit_pdf_with_modifications(input_pdf, output_pdf, new_metadata, logo_path)