from pickletools import read_stringnl_noescape
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from WarehouseViewerUI import UIProductsViewer
import Model

def logout_on_exit():
    Model.logout()

if Model.login('localhost/EMPPDB'):
    print('Logged in, starting the Product Viewer...')
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(logout_on_exit)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = UIProductsViewer()
    ui.setupUi(MainWindow)
    ui.register(MainWindow)
    
    try:
        MainWindow.show()
        sys.exit(app.exec_())
    except RuntimeError as r_exc:
        print(r_exc)
    except Exception as e:
        print(e)
        
else:
    print('Login incorrect')