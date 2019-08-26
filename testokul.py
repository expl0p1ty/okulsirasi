import requests
import os
url = 'http://testokul.karnemiz.com/?pg=ogrgiris'
headers = {'testokul':'olcum.karnemiz.com',
'Content-Type':'application/x-www-form-urlencoded',
'Content-Lenght':'60'}
f = open("isimler.txt", "r")
#print(f.read().split('-\n')[0])
siralistesi =[];



for x in f.read().split('\n'):
  

  ogrencino = x.split('-')[0]
  isim = x.split('-')[1]
  credentials = {'seviye':'700',
'ilkodu':'24',
'kurumkodu':'317381',
'ogrencino':ogrencino,'isim':isim,'bulbtn1':'Bul'}


  r = requests.post(url,headers=headers, data=credentials)
  sayfa = r.content.decode()
  try:
    
    sira = sayfa.split('<td>')[11].split('<')[0]
    numara = sayfa.split('<td>')[2].split('<')[0]
    ad= sayfa.split('<td>')[3].split('<')[0]
    net= sayfa.split('<td class="zemindolu3">')[24].split('<')[0]
    siralistesi.append(sira + '  ' + numara + '  '+ad+'  '+net)
    siralistesi = sorted(siralistesi, key=lambda x: float(x.split()[0]))
    os.system("clear");
    for x in siralistesi:
      print(x)
    
  except IndexError:
    sira,numara,ad,net = 'null' 


