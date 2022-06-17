# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buyTicket.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from multiprocessing import connection
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from sqlite3 import Error

class BUY_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_MAID = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_MAID.setFont(font)
        self.lineEdit_MAID.setObjectName("lineEdit_MAID")
        self.verticalLayout.addWidget(self.lineEdit_MAID)
        self.label_moviename = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_moviename.setFont(font)
        self.label_moviename.setObjectName("label_moviename")
        self.verticalLayout.addWidget(self.label_moviename)
        self.label_starttime = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_starttime.setFont(font)
        self.label_starttime.setObjectName("label_starttime")
        self.verticalLayout.addWidget(self.label_starttime)
        self.label_endtime = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_endtime.setFont(font)
        self.label_endtime.setObjectName("label_endtime")
        self.verticalLayout.addWidget(self.label_endtime)
        self.label_Price = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Price.setFont(font)
        self.label_Price.setObjectName("label_Price")
        self.verticalLayout.addWidget(self.label_Price)
        self.pushButton_buy = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_buy.setFont(font)
        self.pushButton_buy.setObjectName("pushButton_buy")
        self.pushButton_buy.clicked.connect(self.buy)
        self.verticalLayout.addWidget(self.pushButton_buy)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def buy(self):
        MAID = self.lineEdit_MAID.text()
        flag = self.buyIsMAID(MAID)
        if flag != None:
            try:
                conn = sqlite3.connect("cinema.db")
                cur = conn.cursor()
                # 查找放映厅
                sql0 = '''SELECT HallID FROM MovieArrangement WHERE ID={} '''.format(MAID)
                cur.execute(sql0)
                HallID = cur.fetchone()
                HallID = HallID[0]
                #print(HallID)
                # 查看该放映厅的票数
                sql = '''SELECT Seats FROM ScreenHall  WHERE ID ={} '''.format(HallID)
                cur.execute(sql)
                seatnumber = cur.fetchone()
                seatnumber=seatnumber[0]
                #print(seatnumber)
                if int(seatnumber)>=1:
                    # 查看UserName
                    sql2 = '''SELECT UserID FROM MovieArrangement WHERE ID = {}'''.format(MAID)
                    cur.execute(sql2)
                    UserName = cur.fetchone()
                    UserName=UserName[0]
                    #print(UserName)
                        
                    # 购票操作（一个人可以购买多张电影票）
                    sql3 = """INSERT INTO Ticket (ID,UserID) VALUES (?,?)"""
                    value = (MAID,UserName)
                    cur.execute(sql3,value)
                    # 将该放映厅中的余票数减一
                    seatnumber-=1
                    sql4 = "UPDATE ScreenHall SET Seats = {} WHERE ID   = {} ".format(seatnumber,HallID)
                    cur.execute(sql4)
                    #展示电影票的一些信息
                    sql5 = '''
                    SELECT 
                    M.MovieName,MA.StartTime,MA.EndTime,M.Price 
                    FROM 
                    Movie M,(SELECT * FROM MovieArrangement WHERE ID = {})MA 
                    WHERE 
                    M.MovieID = MA.MovieID'''.format(MAID)
                    cur.execute(sql5)
                    result1 = cur.fetchone()
                    self.label_moviename.setText("MovieName: "+result1[0])
                    self.label_starttime.setText("StartTime: "+result1[1])
                    self.label_endtime.setText("EndTime: "+result1[2])
                    self.label_Price.setText("Price: "+str(result1[3]) )
                    conn.commit()
                else:
                    self.label_moviename.setText("All tickets are sold out.Please choose another movie from Movie Menu")
                    self.label_starttime.setText("")
                    self.label_endtime.setText("")
                    self.label_Price.setText("")
            except Error as e:
                print(e)

        else:
            self.label_moviename.setText("Please Enter the Right MAID")
            self.label_starttime.setText("")
            self.label_endtime.setText("")
            self.label_Price.setText("")

    
    # 检测输入的MAID 是否在MocieMenu 中。
    def buyIsMAID(self,MAID):
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
        Dialog.setWindowTitle(_translate("Dialog", "Buy Ticket"))
        self.lineEdit_MAID.setPlaceholderText(_translate("Dialog", "Please Enter the MAID"))
        self.label_moviename.setText(_translate("Dialog", "Movie Name:"))
        self.label_starttime.setText(_translate("Dialog", "Starttime:"))
        self.label_endtime.setText(_translate("Dialog", "EndTime:"))
        self.label_Price.setText(_translate("Dialog", "Price:"))
        self.pushButton_buy.setText(_translate("Dialog", "Buy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = BUY_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())