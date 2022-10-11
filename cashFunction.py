class cashFunc:
  # Fungsi Menghitung Cash
      def __init__ (self) :
        self.penghasilan = int(input('Masukan Pemasukan Bulanan : '))
        self.pengeluaran = int(input('Harga Barang yang ingin di beli : '))
        self.wants = float(self.penghasilan) * 0.30
        self.hasil = int(self.wants - self.pengeluaran)
        self.sisa = float(self.hasil) / self.penghasilan * 100
        print(str(self.hasil))
        print(str("{:.2f}".format(self.sisa)) + "%")