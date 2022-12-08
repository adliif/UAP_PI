import json, requests, os, random

listmenu = ['[1] 5 Kata-kata random dari anime', '[2] Mencari kata dari kumpulan anime']

def fungsiSearch(kata):
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

print('Selamat datang di dunia WIBU\n')
passku = input('Silahkan masukkan passwword Anda : ')

if passku == 'cemaz':
  print('Password Anda benar')
  try:
    os.system('cls')
    print('\n----------------------------------------\n')
    print('\t\tKATANIME')
    print('\n----------------------------------------\n')
    for i in range(0, len(listmenu)):
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
              
    elif pilih == 2:
      os.system('cls')
      kata = input('\nMasukkan kata yang ingin di cari di anime : ')
      fungsiSearch(kata)
      
    else:
      print('Maaf, pilihan menu Anda tidak tersedia')
  except(ValueError, TypeError):
    print('Maaf, Anda memasukkan input yang salah')

else:
  if passku.isupper():
    print('Password harus menggunakan huruf kecil')
  else:
    print('Password Anda salah silahkan coba kembali')
