# this is the center of MDCinema System!

from PyQt5.QtWidgets import QMainWindow,QDialog,QMessageBox

from MDCinema import Ui_MainWindow
from buyTicket import BUY_Dialog
from bounceTicket import Bounce_Dialog
from viewTicket import view_Dialog
from comment import comment_Dialog
from loginUi import Ui_Login_Dialog




class MDCSystem(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # get login state to check whether the login is successful
        self.loginState = False 
        self.login()
        
        self.setupUi(self)
        
        # buy tickets
        self.toolButton_BuyTicket.clicked.connect(self.buyTicket)
        # bounce tickets
        self.toolButton_bounceTickets.clicked.connect(self.bounceTicket)
        # view tickets
        self.toolButton_viewTicket.clicked.connect(self.viewTicket)
        # give comments
        self.toolButton_giveComments.clicked.connect(self.comments)

        self.show()

    def login(self):
        # login function 
        dialog = QDialog()
        ui = Ui_Login_Dialog()
        ui.setupUi(dialog)
        dialog.exec()
        # get login state to check whether the login is successful
        self.loginState = ui.state
        dialog.close()
        
        
    

    def buyTicket(self):
        # if the login is successeful ,you can buy ticket!
        if self.loginState:
            dialog = QDialog()
            ui = BUY_Dialog()
            ui.setupUi(dialog)
            dialog.exec()
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")


    def bounceTicket(self):
        # if the login is successeful ,you can bounce ticket!
        if self.loginState:
            dialog = QDialog()
            ui = Bounce_Dialog()
            ui.setupUi(dialog)
            dialog.exec()
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")

    def viewTicket(self):
        # if the login is successeful ,you can view ticket!
        if self.loginState:
            dialog = QDialog()
            ui = view_Dialog()
            ui.setupUi(dialog)
            dialog.exec()
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")

    def comments(self):
        # if the login is successeful ,you can view comment!
        if self.loginState:
            dialog = QDialog()
            ui = comment_Dialog()
            ui.setupUi(dialog)
            dialog.exec()
        else:
            QMessageBox.about(self,"Warming ","Please Login Firstly!")

    
    


