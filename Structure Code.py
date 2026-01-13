import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from tabulate import tabulate

# Load Data Tipe Excel
df=pd.read_excel(r'C:\Users\User\Downloads\Online-Store-Orders.xlsx', sheet_name='Sheet1')

# TAHAP CLEANING DATA  

# Cek 10 Baris Pertama
print(df.head(10))

# Cek Informasi Data Lengkap Termasuk Kolom, NaN, Tipe Data, dan Ukuran File
print(df.info())

# Cek Dimensi Jumlah Baris dan Kolom
print(df.shape)

# Cek Data NaN Per Kolom
print(df.isnull().sum())

# Hapus Kolom Kosong
df=df.drop(columns=['ShippingEfficiency'])

# Hapus Spasi Awal dan Akhir Semua Kolom
df.columns=df.columns.str.strip()
df=df.apply(lambda x:x.str.strip() if x.dtypes =='object' else x)

# Hapus Spasi Di Tengah Kolom Agar Rapi
df.columns=df.columns.str.replace(r'\s+', '', regex=True)

# Perbaikan Typo Kolom
df.rename(columns={'OderID': 'OrderID', 'CustonerID': 'CustomerID', 'SippingAddres': 'ShippingAddres'}, inplace=True)

# Isi Data CouponCode NaN dengan Label UNKNOWN
df['CouponCode']=df['CouponCode'].fillna('UNKNOWN')

# Cek Hasil Perubahan Pelabelan CouponCode
print(df['CouponCode'].unique())

# Optimasi Tipe Data Atas STR, INT, ,FLOAT, DATE
df=df.convert_dtypes()

df['Date']=pd.to_datetime(df['Date'], errors='coerce')
df['Quantity']=pd.to_numeric(df['Quantity'], errors='coerce')
df['UnitPrice']=pd.to_numeric(df['UnitPrice'], errors='coerce')
df['ItemsInCart']=pd.to_numeric(df['ItemsInCart'], errors='coerce')
df['TotalPrice']=pd.to_numeric(df['TotalPrice'], errors='coerce')

# Mengelompokkan Periode Date Terdiri D (Harian), M (Bulanan), Q (Kuartalan), Y (Tahunan)
df['Date']=df['Date'].dt.to_period('M').astype(str)

#  TAHAP ANALISIS DATA

# Deksripsi Singkat Data INT / Float dengan Desimal 2 ke Dalam Tabulasi
deskripsi=df[['Quantity', 'UnitPrice', 'TotalPrice']].describe().round(2)
if deskripsi is not None:
    print(tabulate(deskripsi, headers='keys', tablefmt='pretty'))
else:
    print('None')

# Tren Penjualan Kumulatif Setiap Product
tren_penjualan=df.groupby('Product')['TotalPrice'].sum()
print(tren_penjualan)

# Cara Alternatif Menghitung Tren Penjualan dengan Pivot Table
pivot_penjualan=df.pivot_table(index='Product', values='TotalPrice', aggfunc='sum')
tabel_pivot=pivot_penjualan.rename_axis(None, axis=1).reset_index()
print(tabel_pivot)

# Total Penjualan Berdasarkan Produk Tertentu (SUMIF)
penjualan_produk=df[df['Product']=='Laptop']['TotalPrice'].sum()
print(penjualan_produk)

# Alternatif Total Penjualan Berdasarkan Produk Tertentu (SUMIF) Mekanisme Looping Agar Fleksibel
def penjualan_produk_tertentu(produk, kolom):
    data=df[df['Product'].str.contains(produk, case=False, na=False)]
    if data.empty:
        return f'Pencarian Produk {produk} Tidak Ditemukan'
    return data[kolom].sum()
print(penjualan_produk_tertentu('Phone', 'TotalPrice'))

# Menghitung Jumlah Product yang Dibatalkan
pesanan_batal=df[df['OrderStatus']=='Cancelled']
hasil=pesanan_batal['Product'].count()
print(hasil)

# Menghitung Jumlah Product Tertentu yang Dibatalkan
produk_batal_tertentu=df[(df['Product']=='Laptop') & (df['OrderStatus']=='Cancelled')]
jumlah_produk_batal=len(produk_batal_tertentu)
print(jumlah_produk_batal)

# Alternatif Menghitung Jumlah Setiap Product Berdasarkan Tiap Status Pemesanan dengan Pivot Table
produk_batal=df.pivot_table(index='Product', columns='OrderStatus', values='OrderID', aggfunc='count')
daftar_produk=produk_batal.rename_axis(None, axis=1).reset_index()
print(daftar_produk)

# Mencari Metode Pembayaran yang Sering Digunakan Transaksi
metode_pembayaran=df.groupby('PaymentMethod')['Product'].count()
print(metode_pembayaran)

# Mencari Metode Pembayaran yang Sering Digunakan Transaksi Tiap Produk
metode_pembayaran_produk=df.pivot_table(index='Product', columns='PaymentMethod', values='OrderID', aggfunc='count')
daftar_metode_pembayaran=metode_pembayaran_produk.rename_axis(None, axis=1).reset_index() # Dalam bentuk tabel
dictionary_metode_pembayaran=metode_pembayaran_produk.to_dict(orient='index') # Dalam bentuk dictionary
print(dictionary_metode_pembayaran)

# Komparasi Banyaknya Jenis Kupon Yang Di gunakan Transaksi
jenis_kupon=df.pivot_table(index='Product', columns='CouponCode', values='OrderID', aggfunc='count')
kupon_by_produk=jenis_kupon.rename_axis(None, axis=1).reset_index()
print(kupon_by_produk)

# Menentukan Multi Kategori Kinerja Penjualan (IF)
def kategori_kinerja(kolom):
    data=df[kolom].values
    hasil=[]

    for nilai in data:
        if nilai >= 2500:
            hasil.append('Very high')
        elif nilai >= 1800:
            hasil.append('High')
        elif nilai >= 1500:
            hasil.append('Medium High')
        elif nilai >= 1000:
            hasil.append('Medium')
        else:
            hasil.append('Low')
    return hasil
df['Sales Performance']=kategori_kinerja('TotalPrice')
tampilkan=df[['Product', 'TotalPrice', 'Sales Performance']].head(10)
if not tampilkan.empty:
    print(tabulate(tampilkan, headers='keys', tablefmt='pretty'))
else:
    print('None')

# Rata-Rata Penjualan berdasarkan Kriteria Kinerja Penjualan
tren_jual=df.groupby('Sales Performance')['TotalPrice'].mean()
print(tren_jual)

# Menentukan Standar Prioritas Pelayanan Customer
# Step 1: Mendeskripsikan Karakteristik Data untuk Memperoleh Acuan Konkrit
karakteristik_belanja=df[['Quantity', 'ItemsInCart']].describe()

# Step 2: Memetakan Kondisi (IF AND)
kondisi_transaksi=[
    (df['Quantity'] >= 4) & (df['ItemsInCart'] >= 8),
    (df['Quantity'] >= 3) & (df['ItemsInCart'] >= 5),
    (df['Quantity'] >= 2) & (df['ItemsInCart'] >= 4)
]
petakan_label=['Platinum', 'Gold', 'Silver']
df['Priority Customer']=np.select(kondisi_transaksi, petakan_label, default='Bronze')
# print(df[['CustomerID', 'Quantity', 'ItemsInCart', 'Priority Customer']].head(10))

# Menghitung Frekuensi Prioritas Customer
frekuensi_prioritas=df['Priority Customer'].value_counts()
print(frekuensi_prioritas)

# Meembuat kolom baru untuk persentase pajak 12% berdasarkan totalprice
df['Tax']=df['TotalPrice']*0.12
print(df[['Product', 'TotalPrice', 'Tax']].head(10))

# visualisasi penjualan produk berdasarkan totalprice warna unik
import matplotlib.pyplot as plt

# 1. Agregasi data
data = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)
# 2. Visualisasi
plt.figure(figsize=(10,6))
data.plot(
    kind='bar', 
    title='Top Products based on Total Sales',
    color=plt.cm.Paired(range(len(data)))) # Membuat warna berbeda tiap bar

# 3. Garis rata-rata
avg = data.mean()
plt.axhline(y=avg, color='r', linestyle='--', label=f'Average: {avg:,.2f}')
# 4. Menambahkan label angka (Data Label) di atas bar
for i, v in enumerate(data):
    # Format nominal dengan pemisah ribuan titik
    nominal = '{:,.2f}'.format(v).replace(',', 'x').replace('.', ',').replace('x', '.')
    plt.text(i, v + (max(data)*0.01), nominal, ha='center', color='black', fontsize=9, fontweight='bold')

# 5. Finishing
plt.xticks(rotation=15)
plt.xlabel('Product', fontweight='bold')
plt.ylabel('Total Sales ($)', fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.3) # Tambah grid halus agar lebih pro
plt.tight_layout()
plt.show()

def visualisasi_pie_pendapatan():
    data_pie = df.groupby('Product')['TotalPrice'].sum()
    plt.figure(figsize=(10, 8))
    explode = [0.05] * len(data_pie) 

    data_pie.plot(
        kind='pie', 
        autopct='%1.1f%%',
        startangle=140, 
        explode=explode, 
        colors=plt.cm.Paired.colors,
        shadow=True
    )
    plt.title('Revenue Contribution per Product Category', fontsize=14, pad=20)
    plt.ylabel('')
    plt.legend(title="Category", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.tight_layout()
    plt.show()
visualisasi_pie_pendapatan()

# Pie Chart Distribusi Status Pemesanan
def distribusi_order():
    data = df.groupby('OrderStatus')['Product'].count()
    explode = [0.05] * len(data)
    
    plt.figure(figsize=(8, 6), facecolor='aliceblue')
    
    # Fungsi lambda untuk menampilkan angka asli
    # pct adalah nilai persentase otomatis dari matplotlib
    # (pct/100.*data.sum()) menghitung kembali ke angka aslinya
    def func(pct, allvals):
        absolute = int(round(pct/100.*allvals.sum()))
        return "{:d}".format(absolute)

    data.plot(
        kind='pie', 
        autopct=lambda pct: func(pct, data), # Menggunakan fungsi pemformat angka
        explode=explode, 
        startangle=120, 
        colors=plt.cm.Paired.colors, 
        shadow=True,
        textprops={'fontsize': 10, 'fontweight': 'bold'} # Agar angka lebih jelas
    )
    
    plt.title('Total Transactions per Order Status', fontsize=12, pad=15)
    plt.ylabel('')
    
    # Menambahkan legenda di samping agar lebih rapi jika angka menumpuk
    plt.legend(data.index, title="Order Status", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.show()
distribusi_order()

# Pie Chart Popularitas Metode Pembayaran Tiap Transaksi
def distribusi_metode_pembayaran():
    data=df.groupby('PaymentMethod')['OrderID'].count()
    explode=[0.05]*len(data)
    plt.figure(figsize=(6.5,4), facecolor='aliceblue')
    data.plot(kind='pie', autopct='%1.1f%%', explode=explode, startangle=120, colors=plt.cm.Paired.colors, shadow=True)
    plt.title('Distribution of Payment Methods for Each Transaction', fontsize=12, pad=15)
    plt.ylabel('')
    plt.tight_layout()
    plt.show()
distribusi_metode_pembayaran()

# 1. Menghitung koefisien korelasi (Pearson)
korelasi = df['ItemsInCart'].corr(df['TotalPrice'])

plt.figure(figsize=(10, 6))
plt.scatter(df['ItemsInCart'], df['TotalPrice'], alpha=0.5, color='green')
plt.title(f'Relationship between Number of Goods vs Total Price (Correlation: {korelasi:.2f})')
plt.xlabel('Number of Items in Cart (ItemsInCart)')
plt.ylabel('Total price (TotalPrice)')
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()

summary = df.groupby('ItemsInCart').agg(
    jumlah_transaksi=('TotalPrice', 'count'),
    rata_total=('TotalPrice', 'mean')
).reset_index()

fig, ax1 = plt.subplots(figsize=(10,6))

ax1.bar(summary['ItemsInCart'], summary['jumlah_transaksi'], alpha=0.6)
ax1.set_ylabel('Number of Transactions')

ax2 = ax1.twinx()
ax2.plot(summary['ItemsInCart'], summary['rata_total'], marker='o', color='red')
ax2.set_ylabel('Average TotalPrice')

plt.title('Number of Transactions & Average Value per Items in cart')
plt.show()

# chart distribusi sales performance berdasarkan jumlah produk
def distribusi_kinerja_penjualan():
    data = df['Sales Performance'].value_counts().reindex(['Very high', 'High', 'Medium High', 'Medium', 'Low'])
    explode = [0.05] * len(data)
    
    plt.figure(figsize=(8, 6), facecolor='aliceblue')
    
    # Fungsi lambda untuk menampilkan angka asli
    # pct adalah nilai persentase otomatis dari matplotlib
    # (pct/100.*data.sum()) menghitung kembali ke angka aslinya
    def func(pct, allvals):
        absolute = int(round(pct/100.*allvals.sum()))
        return "{:d}".format(absolute)

    data.plot(
        kind='pie', 
        autopct=lambda pct: func(pct, data), # Menggunakan fungsi pemformat angka
        explode=explode, 
        startangle=120, 
        colors=plt.cm.Paired.colors, 
        shadow=True,
        textprops={'fontsize': 10, 'fontweight': 'bold'} # Agar angka lebih jelas
    )
    
    plt.title('Distribution of Sales Performance Categories', fontsize=12, pad=15)
    plt.ylabel('')
    
    # Menambahkan legenda di samping agar lebih rapi jika angka menumpuk
    plt.legend(data.index, title="Sales Performance", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.show()
distribusi_kinerja_penjualan()

# referral source penjualan tertinggi
def referral_terbaik():
    data=df.groupby('ReferralSource')['TotalPrice'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10,6))
    warna=plt.cm.Paired(range(len(data)))
    data.plot(kind='bar', color=warna, title='Top Referral Sources based on Total Sales')
    avg=data.mean()
    plt.axhline(y=avg, color='r', linestyle='--', label=f'Average: {avg:,.2f}')
    plt.legend()
    for i, v in enumerate(data):
        nominal='{:,.2f}'.format(v).replace(',','.')
        plt.text(i, v + (max(data)*0.01), nominal, ha='center', color='black', fontsize=9, fontweight='bold')
    plt.xticks(rotation=15)
    plt.xlabel('Referral Source', fontweight='bold')
    plt.ylabel('Total Sales ($)', fontweight='bold')
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()
referral_terbaik()

# distribusi besaran pajak tiap produk dalam pie chart no persen
def distribusi_pajak_produk():
    data = df.groupby('Product')['Tax'].sum()
    explode = [0.05] * len(data)

    plt.figure(figsize=(10, 8), facecolor='aliceblue')

    data.plot(
        kind='pie',
        autopct=lambda pct: "{:,.2f}".format(pct/100.*data.sum()).replace(',', 'x').replace('.', ',').replace('x', '.'),
        startangle=140,
        explode=explode,
        colors=plt.cm.Paired.colors,
        shadow=True,
        textprops={'fontsize': 10, 'fontweight': 'bold'}
    )
    plt.title('Tax Distribution per Product', fontsize=14, pad=20)
    plt.ylabel('')
    plt.legend(title="Product", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.tight_layout()
    plt.show()
distribusi_pajak_produk()

def regresi_linier_berganda():
    # 1. Pilih kolom yang diperlukan dan hapus baris yang ada NaN
    # Pastikan nama kolom sesuai (Quantity, UnitPrice, TotalPrice)
    df_clean = df[['UnitPrice', 'Quantity', 'TotalPrice']].dropna()

    # 2. Paksa semua kolom menjadi tipe data float (ANGKA)
    # Ini untuk menghilangkan error "dtype of object"
    df_clean = df_clean.astype(float)

    # 3. Tentukan X (Prediktor) dan Y (Target)
    X = df_clean[['UnitPrice', 'Quantity']]
    X = sm.add_constant(X) # Menambahkan intercept
    Y = df_clean['TotalPrice']

    # 4. Jalankan Model
    try:
        model = sm.OLS(Y, X).fit()
        print(model.summary())
    except Exception as e:
        print(f"Masih terjadi error: {e}")

regresi_linier_berganda()


df.to_excel(r'C:\Users\User\Downloads\Online-Store-Orders-Cleaned.xlsx', index=False)

