# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'comment.ui'
#
# Created by: PyQt5 UI code generator 5.15.4

# this is the comment part where user can give thire comments after watching the movie

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class comment_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        self.lineEdit_MAID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_MAID.setGeometry(QtCore.QRect(11, 11, 230, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_MAID.setFont(font)
        self.lineEdit_MAID.setObjectName("lineEdit_MAID")
        
        self.label_moviename = QtWidgets.QLabel(Dialog)
        self.label_moviename.setGeometry(QtCore.QRect(11, 48, 400, 24))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_moviename.setFont(font)
        self.label_moviename.setObjectName("label_moviename")
        self.pushButton_commit = QtWidgets.QPushButton(Dialog)
        self.pushButton_commit.setGeometry(QtCore.QRect(11, 452, 93, 37))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_commit.setFont(font)
        self.pushButton_commit.setObjectName("pushButton_commit")
        # give comments
        self.pushButton_commit.clicked.connect(self.givecomments)
        
        self.textEdit_comments = QtWidgets.QTextEdit(Dialog)
        self.textEdit_comments.setGeometry(QtCore.QRect(10, 90, 441, 281))
        self.textEdit_comments.setObjectName("textEdit_comments")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # check whether the user buy the tickle before giving the comments! 
    def checkifbuy(self,MAID):
        flag  = None
        try :
            conn  = sqlite3.connect("cinema.db")
            cur = conn.cursor()
            sql = "SELECT ID FROM Ticket  WHERE ID = {}".format(MAID)
            cur.execute(sql)
            flag = cur.fetchone()
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        return flag
    # give comments function 
    def givecomments(self):
        MAID = self.lineEdit_MAID.text()
        # # ????????????????????????????????????????????????????????????
        flag = self.checkifbuy(MAID)
        if flag!= None:
            comment = self.textEdit_comments.toPlainText()
            if comment!= "":
                try:
                    conn = sqlite3.connect("cinema.db")
                    cur = conn.cursor()
                    sql0 = '''SELECT MovieID,UserID FROM  MovieArrangement WHERE ID = {}'''.format(MAID)
                    cur.execute(sql0)
                    result = cur.fetchone()
                    MovieID,UserID = result[0],result[1]
                    sql00 = '''SELECT MovieName FROM Movie WHERE MovieID = {}'''.format(MovieID)
                    cur.execute(sql00)
                    MovieName = cur.fetchone()
                    for mn in MovieName:
                        res = mn
                    MovieName = res
                    sql = '''
                    INSERT INTO Comments (MovieID,UserID,Content) VALUES (?,?,?)'''
                    value = (MovieID,UserID,comment)
                    cur.execute(sql,value)
                    conn.commit()
                    self.label_moviename.setText("{}       Give Comments successfully!!!!".format(MovieName))
                except sqlite3.Error as e:
                    print(e)
            else :
                self.label_moviename.setText("Please give Comments!!!!")
        else:
            self.label_moviename.setText("You didn't buy this Tickets! Please buy ticket firstly")
    
    def commentsIsMAID(self,MAID):
        flag  = None
        try :
            conn  = sqlite3.connect("cinema.db")
            cur = conn.cursor()
            sql = "SELECT ID FROM MovieArrangement WHERE ID = {}".format(MAID)
            cur.execute(sql)
            flag = cur.fetchone()
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        return flag
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bounce Ticket"))
        self.lineEdit_MAID.setPlaceholderText(_translate("Dialog", "Please Enter the MAID"))
        self.label_moviename.setText(_translate("Dialog", "Movie Name:"))
        self.pushButton_commit.setText(_translate("Dialog", "Commit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = comment_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
