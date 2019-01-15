from ftplib import FTP

#Mediciomes FTP Temperatura
file_o = '/home/pi/Desktop/mediciones/med_temp.csv'
file_d = 'med_temp.csv'

#Mediciones FTP Humedad
file_oo = '/home/pi/Desktop/mediciones/med_hum.csv'
file_dd = 'med_hum.csv'

ftp = FTP()
#ftp.connect('ip',puerto,timeout)
ftp.connect('server_ip',21, 50)
ftp.login('user', 'pass')
print(ftp.getwelcome())
#ftp.mkd('folder_mediciones_v1')
ftp.cwd('folder_mediciones_v1')
print(ftp.pwd())
print(ftp.dir())
ftp.storlines('STOR ' + file_dd, open(file_oo, 'rb'))
ftp.close()