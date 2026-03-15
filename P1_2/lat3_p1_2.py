import matplotlib.pyplot as plt

bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"]
penjualan = [120, 150, 170, 140, 180, 200]

# a) ukuran 8x4 inci
fig, ax = plt.subplots(figsize=(8, 4))
# b) warna bar bebas, edgecolor hitam
ax.bar(bulan, penjualan, color='lightblue', edgecolor='black')
# c) semua label tick pada sumbu x dibuat tebal
for label in ax.get_xaxis().get_ticklabels():
    label.set_fontweight("bold")

# d)  judul dan label
ax.set_title("Penjualan Semester 1")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Penjualan")

# e)  tight_layout()
plt.tight_layout()
plt.savefig('ans_lat3_222313179_LuthfiaNurulIzza.png', dpi=300)
plt.show()
