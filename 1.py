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

# l = [5, 0, 1, 2, 3]
# print(l)
# print(l[:2] + l[2 + 1:])

# print(sorted(l))

def sum_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    if len(divisors) < 5:
        return 0
    divisors.sort()
    return sum(divisors[-5:])

count = 0
n = 20000001
while count < 5:
    m = sum_divisors(n)
    if m > 20000000:
        str_m = str(m)
        num1 = int(str_m[-3:])
        num2 = int(str_m[-6:-3])
        if num1+num2 > 0 and (num1+num2) % 5 == 0:
            print(n, m)
            count += 1
    n += 1

