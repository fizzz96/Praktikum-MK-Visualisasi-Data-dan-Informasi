import matplotlib.pyplot as plt

# 10 cm = (10 / 2.54) inci
fig, ax_cm = plt.subplots(figsize=(10/2.54, 2))

# sumbu bawah untuk cm
ax_cm.set_xlim(0, 10)
ax_cm.set_xlabel('cm')

# twin axis untuk inci di bagian atas
ax_inch = ax_cm.twiny()
ax_inch.set_xlim(0, 10 / 2.54)
ax_inch.set_xlabel('inch')

plt.tight_layout()
plt.savefig('ans_lat2_222313179_LuthfiaNurulIzza.png', dpi=300)
plt.show()
