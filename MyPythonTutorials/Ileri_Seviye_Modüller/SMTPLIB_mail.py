import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["FROM"] = "turguterkan55@gmail.com"
mesaj["TO"] = "turguterkan1306@gmail.com"
mesaj["Subject"] = "Merhaba Erkan"

yazi = """
Merhaba ERKAN, SMTLIB ile  mesaj aldın

ERKAN TURGUT
"""

mesaj_govdesi = MIMEText(yazi, "plain")
mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()  # SMTP serverına kendimizi tanıtıyoruz.
    mail.starttls()  # Adresimizin ve Parolamızın şifrelenmesi için gerekli

    # Gmail hesabınızda 2 adımlı doğrulama varsa, uygulama şifresi kullanın
    mail.login("turguterkan55@gmail.com", "lcvi hvav xpsb puol")

    mail.sendmail(mesaj["FROM"], mesaj["TO"], mesaj.as_string())
    print("Mail başarıyla gönderildi....")
    mail.close()  # Bağlantıyı kesiyoruz.

except Exception as e:
    sys.stderr.write(f"Mail göndermesi başarısız oldu... Hata: {str(e)}")
    sys.stderr.flush()
