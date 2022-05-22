# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\warehouseinsert.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Model

class UIWarehouseInsert(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 188)
        MainWindow.setMaximumSize(QtCore.QSize(800, 188))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbSuppliersNames = QtWidgets.QComboBox(self.centralwidget)
        self.cbSuppliersNames.setGeometry(QtCore.QRect(200, 40, 591, 22))
        self.cbSuppliersNames.setObjectName("cbSuppliersNames")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 201, 21))
        self.label_2.setObjectName("label_2")
        self.lineEditProductName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditProductName.setGeometry(QtCore.QRect(200, 10, 591, 22))
        self.lineEditProductName.setObjectName("lineEditProductName")
        self.spinQuantity = QtWidgets.QSpinBox(self.centralwidget)
        self.spinQuantity.setGeometry(QtCore.QRect(200, 70, 591, 22))
        self.spinQuantity.setProperty("value", 1)
        self.spinQuantity.setObjectName("spinQuantity")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 181, 21))
        self.label_3.setObjectName("label_3")
        self.dspinUnitPrice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dspinUnitPrice.setGeometry(QtCore.QRect(200, 100, 591, 22))
        self.dspinUnitPrice.setMaximum(9999.99)
        self.dspinUnitPrice.setSingleStep(0.5)
        self.dspinUnitPrice.setObjectName("dspinUnitPrice")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 181, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 150, 781, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.register(MainWindow)
        self.bind_events()
        self.load_suppliers()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Warehouse Product Insertion"))
        self.label.setText(_translate("MainWindow", "Product Name"))
        self.label_2.setText(_translate("MainWindow", "Supplier:"))
        self.label_3.setText(_translate("MainWindow", "Quantity to add:"))
        self.label_4.setText(_translate("MainWindow", "Unit price:"))
        self.pushButton.setText(_translate("MainWindow", "Insert new product"))

    def register(self, MainWindow):
        self.__mainwin = MainWindow

    def set_parent(self, parent_win):
        self.__mainwin.setParent(parent_win)

    def bind_events(self):
        self.pushButton.clicked.connect(self.on_insert_button_clicked)
    
    def load_suppliers(self):
        suppliers = Model.query('SELECT NAME FROM SUPPLIERS')
        for supplier in suppliers:
            self.cbSuppliersNames.addItem(supplier[0])
            
    def on_insert_button_clicked(self):
        supp_name = self.cbSuppliersNames.currentText()
        prod_name = self.lineEditProductName.text()
        qty = self.spinQuantity.value()
        u_price = self.dspinUnitPrice.value()
        
        Model.insert_product(supp_name, prod_name, qty, u_price)
        self.__mainwin.close()
        
