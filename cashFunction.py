class cashFunc:
  # Fungsi Menghitung Cash
      def __init__ (self) :
        self.barang = {
          "housing" : 20,
          "transportation" : 10,
          "gadget" : 5,
          "travel" : 0.08,
        }

      def inputSys (self):
        self.penghasilan = int(input('Masukan Pemasukan Bulanan : '))
        self.pengeluaran = int(input('Harga Barang yang ingin di beli : '))
        self.pilihBarang = input("\nBarang yang ingin di beli : \n1.Housing\n2.Transportation\n3.Gadget\n4.Travel\nPilih Barang : ").lower()
        
      def countCash(self):
        self.wants = float(self.penghasilan) * 0.30
        self.hasil = float(self.wants - self.pengeluaran)
        self.sisa = float(self.hasil) / self.penghasilan * 100

      def count(self):
        self.countCash()
        if self.sisa <= 0:
          print("\nKarena udah melebihi perkiraan Assets kamu, maka kami menghitung dengan Amortisasi")
          if self.pilihBarang in ['housing','1' ,'rumah']:
            self.pengeluaran = self.pengeluaran / self.barang['housing']/12
            self.countCash()
          elif self.pilihBarang in ['transportation', '2','transportasi']:
            self.pengeluaran = self.pengeluaran /self.barang['transportation']/12
            self.countCash()
          elif self.pilihBarang in ['gadget', '3','smartphone']:
            self.pengeluaran = self.pengeluaran /self.barang['gadget']/12
            self.countCash()
          elif self.pilihBarang in ['travel', '4','tiket']:
            self.pengeluaran = self.pengeluaran /self.barang['travel']/12
            self.countCash()
            
        print(str("\nSisa uang kamu : {:.2f}".format(self.hasil)))
        print(str("Dan sisa Wants kamu {:.2f}".format(self.sisa)) + "%")   
            