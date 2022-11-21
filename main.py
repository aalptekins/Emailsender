import os,sys
import ssl 
import smtplib 
from email.message import EmailMessage
from PyQt5.QtWidgets import QWidget, QApplication,QMainWindow,QMessageBox
from PyQt5.uic import loadUi 

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("main.ui", self)

        self.emailButton.clicked.connect(self.send_email) 

    def send_email(self):


        email_sender = 'alptekinenglish@gmail.com'
        email_password = "aiyuigwpmstvfacb"
        email_receiver = self.lineRecipient.text()
        port = 465

        subject = self.lineSubject.text()  
        body =self.textBody.toPlainText()

        if self.lineRecipient.text():

            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_receiver
            em["Subject"] = subject
            em.set_content(body)        

            context = ssl.create_default_context()      

            with smtplib.SMTP_SSL('smtp.gmail.com', port,context=context) as smtp:
                smtp.login(email_sender,email_password)
                smtp.sendmail(email_sender,email_receiver,em.as_string())

            print("Email sent.")

            window.close()

        else:
            #it is a pop-up
            #when user forget add a receiver, it appears
            message = QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setText("Please enter a reciever")
            message.setWindowTitle("ERROR!")
            message.exec_()


if __name__ == '__main__':      

    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit = app.exec_() 
