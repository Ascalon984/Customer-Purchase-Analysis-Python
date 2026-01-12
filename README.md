![dreamina-2026-01-08-6528-A clean and minimalist banner, light gra](https://github.com/user-attachments/assets/7b4e142f-7db7-4c34-afce-4c9a84ec0eb5)

Online Store Sales Analysis Pipeline

Transformasi Data Transaksi Menjadi Strategi Bisnis Berbasis Data.

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-ffffff?style=for-the-badge&logo=matplotlib&logoColor=black)](https://matplotlib.org/)
[![Statsmodels](https://img.shields.io/badge/Statsmodels-Statistical%20Modeling-4B8BBE?style=for-the-badge)](https://www.statsmodels.org/)
[![Tabulate](https://img.shields.io/badge/Tabulate-Table%20Formatting-2C2C2C?style=for-the-badge)](https://pypi.org/project/tabulate/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#)

📖 Overview

Proyek ini merupakan pipeline analisis data histori pembelian pelanggan (Online Store Orders) yang terotomatisasi dengan Python. Alur kerja mencakup pembersihan data yang ketat (regex, perbaikan typo), transformasi fitur, segmentasi pelanggan, hingga analisis regresi dan visualisasi lanjutan untuk mendukung pengambilan keputusan strategis berbasis data.

🚨 Business Impact:
– Mengidentifikasi produk dan kategori dengan kontribusi pendapatan tertinggi
– Memetakan perilaku belanja pelanggan dan loyalitas melalui segmentasi yang bermakna
– Mendukung rekomendasi pemasaran dan strategi inventaris berdasarkan tren nyata dari data transaksi.

📊 Highlight Hasil Analisis
1. Revenue Contribution & Operational Health
Visualisasi menunjukkan dominasi kategori Printer & Chair (masing-masing 15.5%) dalam total pendapatan. Namun, dari sisi operasional, terdapat temuan kritis di mana status Cancelled (250 pesanan) menjadi frekuensi tertinggi, yang mengindikasikan perlunya evaluasi pada sistem pemenuhan pesanan atau kebijakan pembatalan. <img width="400" alt="Revenue and Status" src="https://github.com/user-attachments/assets/2e69d553-acf9-4bdf-8296-05fd2c7c89a4" />

2. Distribusi Sales Performance
Mayoritas transaksi dalam dataset ini (688 transaksi) diklasifikasikan ke dalam kategori Low Sales Performance. Hal ini menunjukkan peluang besar untuk strategi upselling guna mendorong pelanggan di kategori ini berpindah ke kategori Medium (190) atau High (143). <img width="800" alt="Sales Performance" src="https://github.com/user-attachments/assets/3860011b-cc8c-4a34-a74e-09c379a05b1c" />

3. Market Acquisition (Referral)
Saluran Instagram mengungguli semua platform pemasaran lainnya dengan kontribusi penjualan mencapai $275.285,45, melampaui rata-rata performa saluran referral. Ini membuktikan efektivitas kampanye visual dalam menarik pelanggan bernilai tinggi. <img width="1000" alt="Top Referral" src="https://github.com/user-attachments/assets/40fc6750-070f-4ab1-90c4-68cf6b2cbbdf" />

4. Korelasi Volume Barang vs Total Harga
Berdasarkan analisis statistik, ditemukan nilai korelasi sebesar 0.39, yang menunjukkan hubungan positif moderat antara jumlah barang dalam keranjang dengan total harga. Grafik scatter plot memperlihatkan bahwa peningkatan jumlah item cenderung diikuti oleh kenaikan batas atas harga transaksi. <img width="1000" alt="Correlation Plot" src="https://github.com/user-attachments/assets/8dc00b21-4104-46d6-900a-f23e9d56aa22" />

5. Tren Volume Transaksi & Average Value
Frekuensi transaksi tertinggi ditemukan pada keranjang belanja berisi 5 hingga 6 item. Namun, secara strategis, garis tren merah menunjukkan bahwa Average TotalPrice meningkat secara konsisten dan mencapai puncaknya pada transaksi dengan 10 item (mendekati nilai 1.800). <img width="1000" alt="Transaction Volume" src="https://github.com/user-attachments/assets/71a539da-847e-460b-ae9b-13695ca53e5e" />

6. Ringkasan Kinerja Penjualan
Visualisasi klasifikasi performa secara keseluruhan mempertegas dominasi segmen Low dalam volume, namun juga memetakan kehadiran segmen Very High (94 transaksi) yang memberikan margin profitabilitas yang lebih besar per transaksinya. <img width="800" alt="Performance Distribution" src="https://github.com/user-attachments/assets/381106b5-fa74-4d7e-8b97-b04ce8250b58" />
   
💡 Temuan Utama (Executive Insights)
- Market Leader: Produk Printer dan Laptop konsisten memimpin pendapatan, menunjukkan permintaan pasar yang kuat dan perlunya manajemen inventaris yang ketat pada kategori ini.

- Operational Leakage: Angka pembatalan (Cancelled: 250) yang melampaui status Delivered atau Shipped merupakan risiko operasional yang harus segera ditangani untuk mencegah kehilangan potensi profit.

- Optimal Basket Value: Meskipun transaksi terbanyak berisi 5-6 barang, profitabilitas maksimal (nilai rata-rata tertinggi) berada pada transaksi 10 barang. Strategi bundling sangat direkomendasikan.

- Referral ROI: Instagram memberikan ROI tertinggi di atas rata-rata kanal lain, mengindikasikan bahwa alokasi anggaran pemasaran pada platform visual memberikan hasil yang signifikan.

- End-to-End Pipeline: Proyek ini mencakup pembersihan data (regex & typo correction), agregasi statistik, segmentasi pelanggan kustom, serta pemodelan Multiple Linear Regression menggunakan Statsmodels untuk prediksi pendapatan.

🚀 Cara Menjalankan Proyek

Clone repositori ini:
git clone https://github.com/Ascalon984/Customer-Purchase-Analysis-Python

Pastikan dataset (Online-Store-Orders.xlsx) tersedia di folder proyek.

Install dependensi:
pip install pandas numpy matplotlib statsmodels tabulate openpyxl
4. Jalankan script Python sesuai urutan penomoran.

---
Organized by **[Aditya Tri Prasetyo]** • 2026 | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/aditya-tri-prasetyo-7b3a0a396) [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/aditya.trisetya)
