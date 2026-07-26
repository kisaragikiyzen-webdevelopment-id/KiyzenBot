# !!! Tools ini gratis dan tak boleh dijual-belikan !!!
# !!! Tools ini tak boleh diubah oleh pemula karna bisa saja rusak !!!
# !!! Perhatian, Jika Bot terkena limit, ganti Email dan App Password Bot dengan milik sendiri agar tetap bisa berjalan !!!
# !!! App Password: https:// !!!
# !!! © 2026 KiyzenBot • Created By 𝙆𝙞𝙨𝙖𝙧𝙖𝙜𝙞 𝙆𝙞𝙮𝙯𝙚𝙣 !!!

import os
import smtplib
from colorama import Fore, Style, init
from email.message import EmailMessage

os.system("clear")
init(autoreset=True)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER = "gmail.bot.by.kisaragi.kiyzen@gmail.com"
APP_PASSWORD = "ugws kpvi wayd xqxm"

RECEIVER = "noreply@support.whatsapp.com"

Banner = """   ██████╗  █████╗ ███╗   ██╗    ██╗    ██╗ █████╗
   ██╔══██╗██╔══██╗████╗  ██║    ██║    ██║██╔══██╗
   ██████╔╝███████║██╔██╗ ██║    ██║ █╗ ██║███████║
   ██╔══██╗██╔══██║██║╚██╗██║    ██║███╗██║██╔══██║
   ██████╔╝██║  ██║██║ ╚████║    ╚███╔███╔╝██║  ██║
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚══╝╚══╝ ╚═╝  ╚═╝                              
    © 2026 KiyzenBot • Created By 𝙆𝙞𝙨𝙖𝙧𝙖𝙜𝙞 𝙆𝙞𝙮𝙯𝙚𝙣"""                                                                                                                                                               print(Fore.MAGENTA + Banner)                                                     reported_number = input("kiyzen@bot:~$ ").strip()

SUBJECT = "Laporan pengguna yang melanggar kebijakan WhatsApp!"

BODY = """Halo Tim WhatsApp,

Saya ingin melaporkan sebuah akun WhatsApp yang saya duga telah melakukan pelanggaran terhadap Ketentuan Layanan dan Kebijakan WhatsApp.

Nomor yang dilaporkan: """ + reported_number + """\n\nAlasan Pelaporan:
- Spam tanpa henti
- Penipuan berulang-kali
- Phishing dan Malware
- penyamaran identitas
- Aktivitas merugikan dan mencurigakan lainnya

Saya memohon agar tim WhatsApp melakukan peninjauan terhadap akun tersebut. Apabila setelah dilakukan pemeriksaan ditemukan adanya pelanggaran terhadap kebijakan yang berlaku, saya berharap tindakan yang sesuai dapat diterapkan.

Terima kasih.
"""

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
        print("[-] Login Success ✓")

        # Loading...
        print("[+] Sending E-Mail...")

        while True:
            smtp.send_message(msg)
            print("[+] Spam Report...")

except Exception as e:
    print("[!] Error:", e)
