# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\warehousevwr.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Model
from ProductsTableModel import ProductsTableModel
import ResultView
from WarehouseInsertUI import UIWarehouseInsert

class UIProductsViewer(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 740)
        MainWindow.setMaximumSize(QtCore.QSize(1117, 740))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(400, 10, 461, 91))
        self.groupBox.setObjectName("groupBox")
        self.btnGenPDF = QtWidgets.QPushButton(self.groupBox)
        self.btnGenPDF.setGeometry(QtCore.QRect(10, 27, 181, 41))
        self.btnGenPDF.setObjectName("btnGenPDF")
        self.btnGenOrder = QtWidgets.QPushButton(self.groupBox)
        self.btnGenOrder.setGeometry(QtCore.QRect(200, 27, 241, 41))
        self.btnGenOrder.setObjectName("btnGenOrder")
        self.tblProducts = QtWidgets.QTableView(self.centralwidget)
        self.tblProducts.setGeometry(QtCore.QRect(10, 120, 1101, 611))
        self.tblProducts.setObjectName("tblProducts")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(870, 10, 231, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnInsertNew = QtWidgets.QPushButton(self.groupBox_2)
        self.btnInsertNew.setGeometry(QtCore.QRect(10, 20, 211, 31))
        self.btnInsertNew.setObjectName("btnInsertNew")
        self.btnRefresh = QtWidgets.QPushButton(self.groupBox_2)
        self.btnRefresh.setGeometry(QtCore.QRect(10, 50, 211, 31))
        self.btnRefresh.setObjectName("btnRefresh")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(240, 10, 151, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioOrderByQty = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioOrderByQty.setGeometry(QtCore.QRect(10, 20, 131, 20))
        self.radioOrderByQty.setChecked(True)
        self.radioOrderByQty.setObjectName("radioOrderByQty")
        self.radioOrderByName = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioOrderByName.setGeometry(QtCore.QRect(10, 50, 121, 20))
        self.radioOrderByName.setObjectName("radioOrderByName")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 221, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.btnTotalQty = QtWidgets.QPushButton(self.groupBox_4)
        self.btnTotalQty.setGeometry(QtCore.QRect(10, 20, 201, 28))
        self.btnTotalQty.setObjectName("btnTotalQty")
        self.btnTotalAmount = QtWidgets.QPushButton(self.groupBox_4)
        self.btnTotalAmount.setGeometry(QtCore.QRect(10, 50, 201, 28))
        self.btnTotalAmount.setObjectName("btnTotalAmount")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Bind events to functions
        self.bind_events()
        # Load initial data
        self.init_results()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Warehouse Product Viewer"))
        self.groupBox.setTitle(_translate("MainWindow", "Reporting"))
        self.btnGenPDF.setText(_translate("MainWindow", "Generate PDF report"))
        self.btnGenOrder.setText(_translate("MainWindow", "Generate report for orders"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Activities"))
        self.btnInsertNew.setText(_translate("MainWindow", "Insert new"))
        self.btnRefresh.setText(_translate("MainWindow", "Force refresh"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sorting"))
        self.radioOrderByQty.setText(_translate("MainWindow", "Order by quantity"))
        self.radioOrderByName.setText(_translate("MainWindow", "Order by name"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Calculations"))
        self.btnTotalQty.setText(_translate("MainWindow", "Cumulative quantity"))
        self.btnTotalAmount.setText(_translate("MainWindow", "Total quantity x prices"))

    def register(self, MainWindow):
        self.__wnd_instance = MainWindow
        
        #Prepare the Insert window
        self.__dlg_insert = UIWarehouseInsert()
        wnd = QtWidgets.QMainWindow()
        self.__dlg_insert.setupUi(wnd)
        self.__dlg_insert.register(wnd)
        self.__dlg_wnd = wnd
        
    def bind_events(self):
        self.btnInsertNew.clicked.connect(self.on_btn_insert_clicked)
        self.btnRefresh.clicked.connect(self.on_btn_refresh_clicked)
        self.btnGenPDF.clicked.connect(self.on_btn_genPdf_clicked)
        self.btnGenOrder.clicked.connect(self.on_btn_genOrder_clicked)
        self.btnTotalQty.clicked.connect(self.on_btn_cumulat_quantity_clicked)
        self.btnTotalAmount.clicked.connect(self.on_btn_cumulat_amount_clicked)
        self.radioOrderByName.toggled.connect(self.on_radio_orderName_toggled)
        self.radioOrderByQty.toggled.connect(self.on_radio_orderQty_toggled)
    
    def on_btn_refresh_clicked(self):
        if self.radioOrderByName.isChecked():
            query = 'SELECT * FROM PROD_SUPPLIERS ORDER BY PROD_NAME'
        else:
            query = 'SELECT * FROM PROD_SUPPLIERS ORDER BY QUANTITY'
        results = Model.query(query)
        headers = ['Product', 'Quantity', 'Unit Price (€)', 'Supplied by']
        data = ProductsTableModel(headers, results)
        self.tblProducts.setModel(data)
        self.tblProducts.resizeColumnsToContents()
        
    def on_btn_insert_clicked(self):
        self.__dlg_wnd.show()

    def on_btn_genPdf_clicked(self):
        query = ''
        if self.radioOrderByName.isChecked():
            query = 'SELECT * FROM PROD_SUPPLIERS ORDER BY PROD_NAME'
        else:
            query = 'SELECT * FROM PROD_SUPPLIERS ORDER BY QUANTITY'
        results = Model.query(query)
        headers = ['Product', 'Quantity', 'Unit Price (EUR)', 'Supplied by']
        
        ResultView.report_to_pdf('PRODUCTS REPORT', headers, results)
        self.qt_msgbox('Report generation', 'Report generated: PRODUCTS REPORT.pdf')
    
    def on_btn_genOrder_clicked(self):
        results = Model.query('SELECT * FROM PROD_SUPPLIERS WHERE QUANTITY <= 0')
        headers = ['Product', 'Quantity', 'Unit Price (EUR)', 'Supplied by']
        
        ResultView.report_to_pdf('PRODUCTS TO ORDER REPORT', headers, results)
        self.qt_msgbox('Report generation', 'Report generated: ORDER PRODUCTS REPORT.pdf')
    
    def on_btn_cumulat_quantity_clicked(self):
        query = 'SELECT SUM(QUANTITY) FROM PRODUCTS'
        results = Model.query(query)
        n_prod = results[0][0]
        self.qt_msgbox('Cumulative quantity', 'Total quantity is {} products.'.format(n_prod))
    
    def on_btn_cumulat_amount_clicked(self):
        query = 'SELECT SUM(QUANTITY * UNIT_PRICE) FROM PRODUCTS'
        results = Model.query(query)
        amount = results[0][0]
        self.qt_msgbox('Total amount', 'Total quantity x unit prices is {} €.'.format(amount))
    
    def on_radio_orderQty_toggled(self, enabled):
        if enabled:
            results = Model.query('SELECT * FROM PROD_SUPPLIERS ORDER BY QUANTITY')
            headers = ['Product', 'Quantity', 'Unit Price (€)', 'Supplied by']
            data = ProductsTableModel(headers, results)
            self.tblProducts.setModel(data)
            self.tblProducts.resizeColumnsToContents()
        
    def on_radio_orderName_toggled(self, enabled):
        if enabled:
            results = Model.query('SELECT * FROM PROD_SUPPLIERS ORDER BY PROD_NAME')
            headers = ['Product', 'Quantity', 'Unit Price (€)', 'Supplied by']
            data = ProductsTableModel(headers, results)
            self.tblProducts.setModel(data)
            self.tblProducts.resizeColumnsToContents()
    
    def init_results(self):
        results = Model.query('SELECT * FROM PROD_SUPPLIERS ORDER BY QUANTITY')
        headers = ['Product', 'Quantity', 'Unit Price (€)', 'Supplied by']
        data = ProductsTableModel(headers, results)
        self.tblProducts.setModel(data)
        self.tblProducts.resizeColumnsToContents()
        
    def qt_msgbox(self, title, text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()