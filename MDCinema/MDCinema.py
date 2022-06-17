# this is the mainwindow of the project!

# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'MDCinema.ui'
# Created by: PyQt5 UI code generator 5.15.4


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets  import QMessageBox,QTableWidgetItem
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidgetMovieMenu = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidgetMovieMenu.setObjectName("tableWidgetMovieMenu")
        self.tableWidgetMovieMenu.setColumnCount(8)
        self.tableWidgetMovieMenu.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMovieMenu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMovieMenu.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMovieMenu.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMovieMenu.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMovieMenu.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMovieMenu.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMovieMenu.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMovieMenu.setHorizontalHeaderItem(7, item)
        self.verticalLayout_2.addWidget(self.tableWidgetMovieMenu)
        self.pushButton_ViewMenu = QtWidgets.QPushButton(self.tab_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/鱼子酱.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ViewMenu.setIcon(icon)
        self.pushButton_ViewMenu.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_ViewMenu.setObjectName("pushButton_ViewMenu")

        # if you clicked "movie Menu" botton ,you can connect to the movieMenu function ! 
        self.pushButton_ViewMenu.clicked.connect(self.movieMenu)

        self.verticalLayout_2.addWidget(self.pushButton_ViewMenu)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_viewcommentMAID = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_viewcommentMAID.setObjectName("lineEdit_viewcommentMAID")
        self.verticalLayout_5.addWidget(self.lineEdit_viewcommentMAID)
        self.tableWidget_viewComments = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_viewComments.setObjectName("tableWidget_viewComments")
        self.tableWidget_viewComments.setColumnCount(3)
        self.tableWidget_viewComments.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_viewComments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_viewComments.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_viewComments.setHorizontalHeaderItem(2, item)
        self.tableWidget_viewComments.horizontalHeader().setDefaultSectionSize(230)
        self.verticalLayout_5.addWidget(self.tableWidget_viewComments)
        self.pushButton_viewComments = QtWidgets.QPushButton(self.tab_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Image/口香糖.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_viewComments.setIcon(icon1)
        self.pushButton_viewComments.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_viewComments.setObjectName("pushButton_viewComments")

        # view comments
        # connect "view comments " botton to the "viewComments" function
        self.pushButton_viewComments.clicked.connect(self.viewComments)
        
        self.verticalLayout_5.addWidget(self.pushButton_viewComments)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget_Tickets = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_Tickets.setObjectName("tableWidget_Tickets")
        self.tableWidget_Tickets.setColumnCount(5)
        self.tableWidget_Tickets.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Tickets.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Tickets.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Tickets.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Tickets.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Tickets.setHorizontalHeaderItem(4, item)
        self.tableWidget_Tickets.horizontalHeader().setDefaultSectionSize(142)
        self.verticalLayout_3.addWidget(self.tableWidget_Tickets)
        self.pushButton_viewTickets = QtWidgets.QPushButton(self.tab_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Image/果冻.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_viewTickets.setIcon(icon2)
        self.pushButton_viewTickets.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_viewTickets.setObjectName("pushButton_viewTickets")

        # view order
        # connect "view order " botton to the "view order" function
        self.pushButton_viewTickets.clicked.connect(self.viewOrder)

        self.verticalLayout_3.addWidget(self.pushButton_viewTickets)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.toolButton_BuyTicket = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_BuyTicket.setMaximumSize(QtCore.QSize(200, 200))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Image/爆米花.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_BuyTicket.setIcon(icon3)
        self.toolButton_BuyTicket.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_BuyTicket.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_BuyTicket.setObjectName("toolButton_BuyTicket")
        
        

        self.verticalLayout_4.addWidget(self.toolButton_BuyTicket)
        self.toolButton_bounceTickets = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_bounceTickets.setMaximumSize(QtCore.QSize(200, 200))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Image/奶酪.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_bounceTickets.setIcon(icon4)
        self.toolButton_bounceTickets.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_bounceTickets.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_bounceTickets.setObjectName("toolButton_bounceTickets")
        
        
        self.verticalLayout_4.addWidget(self.toolButton_bounceTickets)
        self.toolButton_viewTicket = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_viewTicket.setMaximumSize(QtCore.QSize(200, 200))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Image/华夫饼.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_viewTicket.setIcon(icon5)
        self.toolButton_viewTicket.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_viewTicket.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_viewTicket.setObjectName("toolButton_viewTicket")
        
        
        self.verticalLayout_4.addWidget(self.toolButton_viewTicket)
        self.toolButton_giveComments = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_giveComments.setMaximumSize(QtCore.QSize(200, 200))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Image/冰块.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_giveComments.setIcon(icon6)
        self.toolButton_giveComments.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_giveComments.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_giveComments.setObjectName("toolButton_giveComments")
        
        #MainWindow.setGeometry(QtCore.QRect(800,500,1000,800))
        self.verticalLayout_4.addWidget(self.toolButton_giveComments)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        self.menuwenjian = QtWidgets.QMenu(self.menubar)
        self.menuwenjian.setTitle("")
        self.menuwenjian.setObjectName("menuwenjian")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuwenjian.menuAction())
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def movieMenu(self):
        # if the login is successful ,you can view movie Menu
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
                #Drop data from the database into tableWidget
                self.tableWidgetMovieMenu.setRowCount(0)
                for row_number,row_data in enumerate(result):
                    self.tableWidgetMovieMenu.insertRow(row_number)
                    for column_nember,data in enumerate(row_data):
                        self.tableWidgetMovieMenu.setItem(row_number,column_nember,QTableWidgetItem(str(data)))


            except sqlite3.Error as e:
                print(e)
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")
            
    def viewComments(self):
        # if the login is successful ,you can view comments
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
                #Drop data from the database into tableWidget
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
                
                sql = '''
                SELECT 
                TB.ID,m.MovieName,TB.StartTime,TB.EndTime,m.Price
                FROM 
Movie m,(SELECT MA.ID,MA.MovieID,MA.StartTime,MA.EndTime FROM Ticket T,MovieArrangement MA WHERE T.ID = MA.ID and T.UserID = {} ) TB
                WHERE 
                TB.MovieID = m.MovieID'''.format(UserID)
                cur.execute(sql)
                result = cur.fetchall()
                #Drop data from the database into tableWidget
                self.tableWidget_Tickets.setRowCount(0)
                for row_number,row_data in enumerate(result):
                    self.tableWidget_Tickets.insertRow(row_number)
                    for column_nember,data in enumerate(row_data):
                        self.tableWidget_Tickets.setItem(row_number,column_nember,QTableWidgetItem(str(data)))
                

            except sqlite3.Error as e:
                print(e)
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")


    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MDCinema"))
        item = self.tableWidgetMovieMenu.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MAID"))
        item = self.tableWidgetMovieMenu.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MovieName"))
        item = self.tableWidgetMovieMenu.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Director"))
        item = self.tableWidgetMovieMenu.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Actors"))
        item = self.tableWidgetMovieMenu.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "StartTime"))
        item = self.tableWidgetMovieMenu.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "EndTime"))
        item = self.tableWidgetMovieMenu.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Price"))
        self.pushButton_ViewMenu.setText(_translate("MainWindow", "View Menu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Movie Menu"))
        self.lineEdit_viewcommentMAID.setPlaceholderText(_translate("MainWindow", "Please Enter the MAID "))
        item = self.tableWidget_viewComments.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Users"))
        item = self.tableWidget_viewComments.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MovieName"))
        item = self.tableWidget_viewComments.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Comments"))
        self.pushButton_viewComments.setText(_translate("MainWindow", "View Comments"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "View Comments"))
        item = self.tableWidget_Tickets.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MAID"))
        item = self.tableWidget_Tickets.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MovieName"))
        item = self.tableWidget_Tickets.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "StartTime"))
        item = self.tableWidget_Tickets.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "EndTime"))
        item = self.tableWidget_Tickets.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Price"))
        self.pushButton_viewTickets.setText(_translate("MainWindow", "View Tickets"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Your Orders"))
        self.toolButton_BuyTicket.setText(_translate("MainWindow", "Buy Ticket"))
        self.toolButton_bounceTickets.setText(_translate("MainWindow", "BounceTicket"))
        self.toolButton_viewTicket.setText(_translate("MainWindow", "ViewTicket"))
        self.toolButton_giveComments.setText(_translate("MainWindow", "Give Comment"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
