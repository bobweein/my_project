# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4

# this is the login part of the MDCinema

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Login_Dialog(object):
    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName("Login_Dialog")
        Login_Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        Login_Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Login_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_welcome = QtWidgets.QLabel(Login_Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_welcome.setFont(font)
        self.label_welcome.setObjectName("label_welcome")
        self.verticalLayout.addWidget(self.label_welcome)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_UserName = QtWidgets.QLabel(Login_Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_UserName.setFont(font)
        self.label_UserName.setObjectName("label_UserName")
        self.horizontalLayout.addWidget(self.label_UserName)
        self.lineEdit_UserName = QtWidgets.QLineEdit(Login_Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_UserName.setFont(font)
        self.lineEdit_UserName.setObjectName("lineEdit_UserName")
        self.horizontalLayout.addWidget(self.lineEdit_UserName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_PassWord = QtWidgets.QLabel(Login_Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_PassWord.setFont(font)
        self.label_PassWord.setObjectName("label_PassWord")
        self.horizontalLayout_2.addWidget(self.label_PassWord)
        self.lineEdit_PassWord = QtWidgets.QLineEdit(Login_Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_PassWord.setFont(font)
        self.lineEdit_PassWord.setObjectName("lineEdit_PassWord")
        self.horizontalLayout_2.addWidget(self.lineEdit_PassWord)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_signup = QtWidgets.QPushButton(Login_Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_signup.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/班戟.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_signup.setIcon(icon)
        self.pushButton_signup.setIconSize(QtCore.QSize(26, 26))
        self.pushButton_signup.setObjectName("pushButton_signup")
        # connect sign up bottton to signup function
        self.pushButton_signup.clicked.connect(self.signup)
        self.horizontalLayout_3.addWidget(self.pushButton_signup)
        self.pushButton_signIn = QtWidgets.QPushButton(Login_Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_signIn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Image/泡芙.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_signIn.setIcon(icon1)
        self.pushButton_signIn.setIconSize(QtCore.QSize(26, 26))
        self.pushButton_signIn.setObjectName("pushButton_signIn")
        # connect signin botton to signin function
        self.pushButton_signIn.clicked.connect(self.signin)
        self.horizontalLayout_3.addWidget(self.pushButton_signIn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_loginstate = QtWidgets.QLabel(Login_Dialog)
        self.label_loginstate.setText("")
        self.label_loginstate.setObjectName("label_loginstate")
        self.verticalLayout.addWidget(self.label_loginstate)

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)
        self.state =False 

    def retranslateUi(self, Login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "Login"))
        self.label_welcome.setText(_translate("Login_Dialog", "Welcome to The MDCinema"))
        self.label_UserName.setText(_translate("Login_Dialog", "UserName:"))
        self.label_PassWord.setText(_translate("Login_Dialog", "PassWord:"))
        self.pushButton_signup.setText(_translate("Login_Dialog", "Sign Up"))
        self.pushButton_signIn.setText(_translate("Login_Dialog", "Sign In"))

    # sign up function
    def signup(self):
        UserName = self.lineEdit_UserName.text()
        PassWord = self.lineEdit_PassWord.text()
        if UserName!="" and PassWord!="":
            try:
                conn = sqlite3.connect("cinema.db")
                cur = conn.cursor()
                sql = "INSERT INTO User (UserName,PassWord) VALUES (?,?)"
                value = (UserName,PassWord)
                cur.execute(sql,value)
                conn.commit()
                self.label_loginstate.setText("Sign Up Successfully! Your can Sign In now")
                self.state =False

            except sqlite3.Error as e:
                print(e)
                self.label_loginstate.setText("Sign Up Failed! Please change another UserName!")
                self.state = False
        else:
            self.label_loginstate.setText("Error !Please Enter UserName and PassWord")
            self.state = False 

    # sign in function
    def signin(self):
        UserName = self.lineEdit_UserName.text()
        PassWord = self.lineEdit_PassWord.text()
        if UserName!="" and PassWord!="":
            try:
                conn = sqlite3.connect("cinema.db")
                cur = conn.cursor()
                sql = '''SELECT PassWord FROM User WHERE UserName= {}'''.format(UserName)
                
                cur.execute(sql)
                result = cur.fetchone()
                #print(result)
                if result!= None and result[0]==PassWord:
                        
                    sql2 = "UPDATE MovieArrangement SET UserID ={}".format(UserName)
                    cur.execute(sql2)
                    conn.commit()
                    self.label_loginstate.setText("Sign In Successfully")
                    self.state = True 
                else :
                    self.state = False 
                    self.label_loginstate.setText("Sign In Failed!")
                        
            except sqlite3.Error as e:
                self.state = False 
                print(e)
        else:
            self.label_loginstate.setText("Error !Please Enter UserName and PassWord")
            self.state = False 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Dialog = QtWidgets.QDialog()
    ui = Ui_Login_Dialog()
    ui.setupUi(Login_Dialog)
    Login_Dialog.show()
    sys.exit(app.exec_())
