from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import bot

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('front.ui')
        self.ui.show()
        self.ui.find_btn.clicked.connect(self.find_unfollowers)
        
    def find_unfollowers(self):
        username = self.ui.user_field.text()
        password = self.ui.pass_field.text()
        bot.login(username,password)
        unfollowers = bot.get_unfollowers(username)
        for unfollower in unfollowers:
            new_label = QLabel(unfollower)
            self.ui.verticalLayout_2.addWidget(new_label)
        

app = QApplication([])
window = Window()
app.exec()
        
        