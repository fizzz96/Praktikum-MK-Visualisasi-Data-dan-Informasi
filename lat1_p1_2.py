import matplotlib.pyplot as plt

#  figsize dlm inci: 512 / 100 = 5.12 inci
fig = plt.figure(figsize=(5.12, 5.12), dpi=100)
ax = fig.add_subplot(111)

ax.text(0.5, 0.5, 'Gambar 512x512 piksel', ha='center', va='center')

# save figure
plt.savefig('ans_lat1_222313179_LuthfiaNurulIzza.png', dpi=100)
plt.show()