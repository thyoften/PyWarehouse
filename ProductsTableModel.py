import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

# Implements a TableModel to view Product data into a QTableView


class ProductsTableModel(QtCore.QAbstractTableModel):
    def __init__(self, headers, data):
        super(ProductsTableModel, self).__init__()
        self.__headers = headers
        self.__data = data
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.__data[index.row()][index.column()]
    
    def rowCount(self, parent):
        return len(self.__data)
    
    def columnCount(self, parent):
        return len(self.__data[0])
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Vertical: # for rows
                return ' ' #str(section)
            
            if orientation == Qt.Horizontal: # for columnss
                return self.__headers[section]