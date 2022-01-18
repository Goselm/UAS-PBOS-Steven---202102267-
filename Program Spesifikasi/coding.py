class Data():
    def init(self,nama,alamat,nim):
        
        print("Inputkan Data Anda")
        
    def input(self):
        self.nama = input("Nama   : ")
        self.alamat = input("Alamat : ")
        self.nim = input("NIM    : ")
        
class datapribadi(Data):
    def cetak(self):
        print("Data Anda : ")
        print ("Nama   : ", self.nama)
        print ("Alamat : ", self.alamat)
        print ("NIM    : ", self.nim)
        
data = datapribadi()
data.input()
data.cetak()