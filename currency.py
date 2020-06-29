from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot
import requests,ui

url = "https://api.tgju.online/v1/data/sana/json"

def currency():
    try:
        get = requests.get(url)
        currency_json = get.json()
        currency_usd = currency_json['sana_buy_usd']['p']
        return(currency_usd)
    except:
        return False

class App(QtWidgets.QMainWindow,ui.Ui_MainWindow):
    def __init__(self,parent=None):
        super(App,self).__init__(parent)
        self.setupUi(self)
    @pyqtSlot()
    def button_pressed(self):
        re = currency()
        self.output.setText("")
        if not re:
            self.output.setText("لطفا اینترنت خود را چک کنید")
        else:
            self.output.setText("دلار در حال حاضر {0} ریال است".format(re))
def main():
    mainApp = QApplication(['دلار ایران'])
    mainWindow = App()
    mainWindow.show()
    mainApp.exec_()

if __name__ ==  "__main__":
    main()