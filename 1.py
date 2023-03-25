# import random
# import smtplib
# import time
#
# from email.mime.text import MIMEText
#
#
# def send_email(message):
#     my_email = "japanholiput@gmail.com"
#     password = "qxfbhoiwuuspbdkl"
#     em = "cheb-liceischool2@rchuv.ru"
#     em2 = "irina_1908@mail.ru"
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#
#     server.login(my_email, password)
#     msg = MIMEText(message)
#     msg["Subject"] = "PIN"
#     server.sendmail(my_email, em, msg.as_string())
#     server.sendmail(my_email, em2, msg.as_string())
#
# while True:
#     send_email(str(random.randint(1000000, 9999999)))
#     time.sleep(5)

l = [5, 0, 1, 2, 3]
print(l)
print(l[:2] + l[2 + 1:])

# print(sorted(l))
