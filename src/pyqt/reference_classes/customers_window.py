# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customers_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CustomersWindow(object):
    def setupUi(self, CustomersWindow):
        CustomersWindow.setObjectName("CustomersWindow")
        CustomersWindow.resize(1366, 697)
        self.gridLayout = QtWidgets.QGridLayout(CustomersWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.add_customer_btn = QtWidgets.QPushButton(CustomersWindow)
        self.add_customer_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_customer_btn.sizePolicy().hasHeightForWidth())
        self.add_customer_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_customer_btn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-dodaj-użytkownika-mężczyzna-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_customer_btn.setIcon(icon)
        self.add_customer_btn.setIconSize(QtCore.QSize(30, 30))
        self.add_customer_btn.setObjectName("add_customer_btn")
        self.gridLayout.addWidget(self.add_customer_btn, 0, 0, 1, 1)
        self.edit_customer_btn = QtWidgets.QPushButton(CustomersWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_customer_btn.sizePolicy().hasHeightForWidth())
        self.edit_customer_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_customer_btn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-edycja-użytkownika-mężczyzna-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_customer_btn.setIcon(icon1)
        self.edit_customer_btn.setIconSize(QtCore.QSize(30, 30))
        self.edit_customer_btn.setObjectName("edit_customer_btn")
        self.gridLayout.addWidget(self.edit_customer_btn, 0, 1, 1, 1)
        self.delete_customer_bnt = QtWidgets.QPushButton(CustomersWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_customer_bnt.sizePolicy().hasHeightForWidth())
        self.delete_customer_bnt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.delete_customer_bnt.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-usuń-użytkownika-mężczyzna-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_customer_bnt.setIcon(icon2)
        self.delete_customer_bnt.setIconSize(QtCore.QSize(30, 30))
        self.delete_customer_bnt.setObjectName("delete_customer_bnt")
        self.gridLayout.addWidget(self.delete_customer_bnt, 0, 2, 1, 1)
        self.customersTableView = QtWidgets.QTableView(CustomersWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customersTableView.sizePolicy().hasHeightForWidth())
        self.customersTableView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.customersTableView.setFont(font)
        self.customersTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.customersTableView.setAlternatingRowColors(True)
        self.customersTableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.customersTableView.setTextElideMode(QtCore.Qt.ElideNone)
        self.customersTableView.setSortingEnabled(True)
        self.customersTableView.setObjectName("customersTableView")
        self.customersTableView.horizontalHeader().setCascadingSectionResizes(False)
        self.customersTableView.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.customersTableView, 2, 0, 1, 6)

        self.retranslateUi(CustomersWindow)
        QtCore.QMetaObject.connectSlotsByName(CustomersWindow)

    def retranslateUi(self, CustomersWindow):
        _translate = QtCore.QCoreApplication.translate
        CustomersWindow.setWindowTitle(_translate("CustomersWindow", "Form"))
        self.add_customer_btn.setText(_translate("CustomersWindow", "Dodaj"))
        self.edit_customer_btn.setText(_translate("CustomersWindow", "Edytuj"))
        self.delete_customer_bnt.setText(_translate("CustomersWindow", "Usuń"))

import resources_rc
