# ADLI FIQRULLAH      / NPM. 2117051075
# WALIID ILHAM        / NPM. 2117051094
# TASYA AZZAHRA PUTRI / NPM. 2117051043

class masukan():                                                                      # Class
  def __init__(self, kritik, saran):
    self.__kritik = kritik
    self.__saran = saran

  def _get_kritik(self):
    return self.__kritik

  def _get_saran(self):
    return self.__saran


class user(masukan):                                                                  # Inheritance
  def __init__(self, kritik, saran, namaUser):
    super().__init__(kritik, saran)
    self.namaUser = namaUser

  def get_namaUser(self):
    return self.namaUser

  def info(self):
    print('Nama user : ', self.namaUser)
    print('Kritik    : ', self._get_kritik())
    print('Saran     : ', self._get_saran())


import json, requests, os, random
listmenu = ['[1] 5 Kata-kata random dari anime', 
            '[2] Mencari kata dari kumpulan anime', 
            '[3] Kritik dan saran']


def fungsiSearch(kata):                                                               # Function
  params = {
    'kata':kata,
    'page':random.randint(1, 20)
  }

  cariKata = requests.get('https://katanime.vercel.app/api/carikata', params)
  cariKataSuccess = cariKata.json()
  print()
  
  for i in cariKataSuccess['result']:
    print('English\t\t:', i['english'], '\nIndonesia\t:', i['indo'],
    '\nCharacter\t:', i['character'], '\nAnime\t\t:', i['anime'], '\n')

  simpan = input('Buat file notepad untuk menyalin quotes? [Y/N] : ')
  
  if simpan == 'Y':
    fa = open('Katanime.txt', 'a')                                                    # File handling
    fa.write('')
    print('Notepad Anda berhasil dibuat')
  elif simpan == 'N':
    print('Terima kasih telah berkunjung :)')
  else:
    print('Masukan Anda tidak tersedia')


def main():
  print('Selamat datang di dunia WIBU\n')
  passku = input('Silahkan masukkan passwword Anda : ')

  if passku == 'cemaz':
    print('Password Anda benar')
    try:
      os.system('cls')
      print('\n----------------------------------------\n')
      print('\t\tKATANIME')
      print('\n----------------------------------------\n')
      for i in range(0, len(listmenu)):                                               # Method
        print(listmenu[i])

      pilih = int(input('\nSilahkan pilih menu yang tersedia (WAJIB ANGKA!) : '))

      if pilih == 1:
        os.system('cls')
        kataRandom = requests.get('https://katanime.vercel.app/api/getrandom')
        kataRandomSuccess = kataRandom.json()
        print()
        
        for i in kataRandomSuccess['result']:
          print('English\t\t:', i['english'], '\nIndonesia\t:', i['indo'],
          '\nCharacter\t:', i['character'], '\nAnime\t\t:', i['anime'], '\n')

        simpan = input('Buat file notepad untuk menyalin quotes? [Y/N] : ')
        
          if simpan == 'Y':
            fa = open('Katanime.txt', 'a')                                                    # File handling
            fa.write('')
            print('Notepad Anda berhasil dibuat')
          elif simpan == 'N':
            print('Terima kasih telah berkunjung :)')
          else:
            print('Masukan Anda tidak tersedia')

                
      elif pilih == 2:
        os.system('cls')
        kata = input('\nMasukkan kata yang ingin di cari di anime : ')
        fungsiSearch(kata)

      elif pilih == 3:
        os.system('cls')
        nama = input('\nMasukkan Nama Anda\t : ')
        kritik = input('Masukkan kritik Anda\t : ')
        saran = input('Masukkan saran Anda\t : ')

        print('\nMasukan Anda akan kami simpan untuk developer')
        print('_____________________________________________\n')
        print('#NOTE', random.randint(1, 9999))
        akhiran = user(kritik, saran, nama)
        akhiran.info()
     
      else:
        print('Maaf, pilihan menu Anda tidak tersedia')
    except(ValueError, TypeError):
      print('Maaf, Anda memasukkan input yang salah')

  else:
    if passku.isupper():                                                        # String method
      print('Password harus menggunakan huruf kecil')
    else:
      print('Password Anda salah silahkan coba kembali')

      
main()
