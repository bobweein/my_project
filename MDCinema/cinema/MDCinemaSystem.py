from PyQt5.QtWidgets import QMainWindow,QDialog,QMessageBox,QTableWidgetItem,QWidget,QApplication
import sys


from MDCinema import Ui_MainWindow
from buyTicket import BUY_Dialog
from bounceTicket import Bounce_Dialog
from viewTicket import view_Dialog
from comment import comment_Dialog
from loginUi import Ui_Login_Dialog

import sqlite3
from sqlite3 import Error


class MDCSystem(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.loginState = False 
        self.login()
        
        self.setupUi(self)
        self.toolButton_BuyTicket.clicked.connect(self.buyTicket)
        self.toolButton_bounceTickets.clicked.connect(self.bounceTicket)
        self.toolButton_viewTicket.clicked.connect(self.viewTicket)
        self.toolButton_giveComments.clicked.connect(self.comments)
        self.pushButton_ViewMenu.clicked.connect(self.movieMenu)
        self.pushButton_viewComments.clicked.connect(self.viewComments)
        self.pushButton_viewTickets.clicked.connect(self.viewOrder)
        self.show()

    def login(self):
        dialog = QDialog()
        ui = Ui_Login_Dialog()
        ui.setupUi(dialog)
        dialog.exec()
        self.loginState = ui.state
        dialog.close()
        
        
    def movieMenu(self):
        if self.loginState:
            try:
                conn = sqlite3.connect("cinema.db")
                cur = conn.cursor()
                sql = """SELECT 
                MA.ID,M.MovieName,M.Director,M.Actors,MA.StartTime,MA.EndTime,M.Price 
                FROM 
                Movie M ,MovieArrangement MA 
                WHERE 
                M.MovieID = MA.MovieID"""
                cur.execute(sql)
                result = cur.fetchall()
                self.tableWidgetMovieMenu.setRowCount(0)

                for row_number,row_data in enumerate(result):
                    self.tableWidgetMovieMenu.insertRow(row_number)
                    for column_nember,data in enumerate(row_data):
                        self.tableWidgetMovieMenu.setItem(row_number,column_nember,QTableWidgetItem(str(data)))


            except Error as e:
                print(e)
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")
            
    def viewComments(self):
        if  self.loginState:
            MAID = self.lineEdit_viewcommentMAID.text()
            if MAID!= "":
                conn = sqlite3.connect("cinema.db")
                cur = conn.cursor()
                sql ="SELECT MovieID,UserID FROM MovieArrangement WHERE ID = {}".format(MAID)
                cur.execute(sql)
                result = cur.fetchone()
                MovieID = result[0]

                sql2 = "SELECT c.UserID,m.MovieName,c.Content FROM (SELECT * FROM Comments WHERE MovieID ={}) c ,Movie m WHERE m.MovieID = c.MovieID".format(MovieID)

                cur.execute(sql2)
                result = cur.fetchall()
                self.tableWidget_viewComments.setRowCount(0)

                for row_number,row_data in enumerate(result):
                    self.tableWidget_viewComments.insertRow(row_number)
                    for column_nember,data in enumerate(row_data):
                        self.tableWidget_viewComments.setItem(row_number,column_nember,QTableWidgetItem(str(data)))

            else:
                QMessageBox.about(self,"Warming ","Please Enter MAID")
        else :
            QMessageBox.about(self,"Warming ","Please Login Firstly!")

    def viewOrder(self):
        if self.loginState:
            try:
                conn = sqlite3.connect("cinema.db")
                cur = conn.cursor()
                sql0 = '''SELECT UserID from MovieArrangement'''
                cur.execute(sql0)
                result  = cur.fetchone()
                UserID = 0
                for User in result:
                    UserID = User
                #print(UserID)
                sql = '''
                SELECT 
                TB.ID,m.MovieName,TB.StartTime,TB.EndTime,m.Price
                FROM 
Movie m,(SELECT MA.ID,MA.MovieID,MA.StartTime,MA.EndTime FROM Ticket T,MovieArrangement MA WHERE T.ID = MA.ID and T.UserID = {} ) TB
                WHERE 
                TB.MovieID = m.MovieID'''.format(UserID)
                cur.execute(sql)
                result = cur.fetchall()
                self.tableWidget_Tickets.setRowCount(0)

                for row_number,row_data in enumerate(result):
                    self.tableWidget_Tickets.insertRow(row_number)
                    for column_nember,data in enumerate(row_data):
                        self.tableWidget_Tickets.setItem(row_number,column_nember,QTableWidgetItem(str(data)))
                

            except Error as e:
                print(e)
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")

    def buyTicket(self):
        if self.loginState:
            dialog = QDialog()
            ui = BUY_Dialog()
            ui.setupUi(dialog)
            dialog.exec()
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")


    def bounceTicket(self):
        if self.loginState:
            dialog = QDialog()
            ui = Bounce_Dialog()
            ui.setupUi(dialog)
            dialog.exec()
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")

    def viewTicket(self):
        if self.loginState:
            dialog = QDialog()
            ui = view_Dialog()
            ui.setupUi(dialog)
            dialog.exec()
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")

    def comments(self):
        if self.loginState:
            dialog = QDialog()
            ui = comment_Dialog()
            ui.setupUi(dialog)
            dialog.exec()
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")

    
    


