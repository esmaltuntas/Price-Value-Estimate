from fpdf import FPDF

class SQLStudyPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "VERİ TABANI ÇALIŞMA KAĞIDI (MSSQL / T-SQL)", ln=True, align="C")
        self.ln(5)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def question(self, text):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, text)
        self.ln(2)

pdf = SQLStudyPDF()
pdf.add_page()

# 1. Temel Sorgular
pdf.section_title("1. Temel Sorgular")
pdf.question("Soru 1:\nSELECT * FROM Ogrenciler WHERE Sehir = 'Bursa';\nAçıklama: Belirtilen şehirdeki öğrencileri listeler.")
pdf.question("Soru 2:\nSELECT * FROM Ogrenciler ORDER BY Ad ASC;")

# 2. Fonksiyonlar
pdf.section_title("2. Fonksiyonlar ve Filtreleme")
pdf.question("Soru 3:\nSELECT AVG(Yas) AS OrtalamaYas FROM Ogrenciler;")
pdf.question("Soru 4:\nSELECT Sehir, COUNT(*) AS OgrenciSayisi FROM Ogrenciler GROUP BY Sehir;")

# 3. JOIN
pdf.section_title("3. JOIN – Tabloları Birleştirme")
pdf.question("Soru 5:\nSELECT O.Ad, N.Vize, N.Final\nFROM Ogrenciler O\nINNER JOIN Notlar N ON O.OgrenciID = N.OgrenciID;")

# 4. CRUD
pdf.section_title("4. Kayıt Ekleme, Güncelleme ve Silme")
pdf.question("Soru 6:\nINSERT INTO Ogrenciler (Ad, Soyad, Sehir) VALUES ('Esma', 'Altuntaş', 'Bursa');")
pdf.question("Soru 7:\nUPDATE Ogrenciler SET Sehir = 'İstanbul' WHERE OgrenciID = 3;")
pdf.question("Soru 8:\nDELETE FROM Ogrenciler WHERE OgrenciID = 5;")

# 5. Subquery
pdf.section_title("5. Alt Sorgu (Subquery)")
pdf.question("Soru 9:\nSELECT * FROM Ogrenciler\nWHERE Yas > (SELECT AVG(Yas) FROM Ogrenciler);")

# 6. Tablo Oluşturma
pdf.section_title("6. Tablo Oluşturma")
pdf.question("Soru 10:\nCREATE TABLE Dersler (\n    DersID INT PRIMARY KEY,\n    DersAdi NVARCHAR(50)\n);")

# Terim Açıklamaları
pdf.section_title("EKSTRA: Terim Açıklamaları")
pdf.question("INNER JOIN:\nİki tabloyu ortak sütuna göre birleştirir.")
pdf.question("HAVING:\nGROUP BY sonrası filtreleme yapar.")
pdf.question("PRIMARY KEY:\nBenzersiz ve boş olmayan kimlik sütunu.")
pdf.question("FOREIGN KEY:\nBaşka bir tablodaki PRIMARY KEY’e referans olur.")

# PDF olarak kaydet
pdf.output("veri_tabani_calisma_kagidi.pdf")
