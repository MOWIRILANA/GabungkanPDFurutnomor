import fitz  # PyMuPDF
import os
import re

def sorted_numerically(pdf_list):
    return sorted(pdf_list, key=lambda f: [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', f)])

def merge_pdfs(input_folder, output_pdf):
    pdf_merger = fitz.open()
    pdf_files = sorted_numerically([f for f in os.listdir(input_folder) if f.endswith(".pdf")])
    
    if len(pdf_files) < 1:
        print("Tidak ada file PDF yang ditemukan di folder.")
        return
    
    for pdf in pdf_files:
        pdf_path = os.path.join(input_folder, pdf)
        print(f"Menambahkan: {pdf}")
        doc = fitz.open(pdf_path)
        pdf_merger.insert_pdf(doc)
    
    pdf_merger.save(output_pdf)
    pdf_merger.close()
    print(f"Gabungan PDF tersimpan sebagai: {output_pdf}")

# Ganti 'pdf_folder' dengan path folder tempat menyimpan file PDF
pdf_folder = "C:/lokasifolderpdfyangterpisah"  # Ubah sesuai lokasi folder 
output_file = "C:/simpanfilehasilgabungpdf.pdf"  # Nama file output

merge_pdfs(pdf_folder, output_file)


