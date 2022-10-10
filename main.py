print('Wants App')
penghasilan = int(input('Masukan Pemasukan Bulanan : '))
pengeluaran = int(input('Harga Barang yang ingin di beli : '))
wants = float(penghasilan) * 0.30
hasil = int(wants - pengeluaran)
sisa = float(hasil) / penghasilan * 100
print(str(hasil))
print(str("{:.2f}".format(sisa)) + "%")
if(sisa >= 20):
  print("Boleh banget nih buat menuhin wants kamu sesekali")
elif(sisa >= 10):
  print("Coba kamu pertimbangin lagi")
elif(sisa >= 1):
  print("Waduh mending ditahan dulu beli barangnya")
else:
  print("Big No! Udah melebihi budget kamu ni!")