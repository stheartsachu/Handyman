import smtplib

def smtp(name,l,otp,email):
    msg = "--*---*------WELCOME TO OUR HandyMan -----*---*--\n\n\n" \
          "          HI,%s \n\n" \
          "          This OTP is confidential." \
          " For security reasons,\n" \
          "           DO NOT share the LINK with anyone. \n\n" \
          "             LINK   : %s \n\n" \
          "          LINK GENERATION TIME      : %s \n\n" % (name, l, str(otp))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('stheartsachu@gmail.com', 'sachu20529')
    server.sendmail('stheartsachu@gmail.com', email, msg)
    server.quit()