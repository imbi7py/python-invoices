# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CustomerDialog(object):
    def setupUi(self, CustomerDialog):
        CustomerDialog.setObjectName("CustomerDialog")
        CustomerDialog.resize(800, 383)
        CustomerDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(CustomerDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setObjectName("formLayout")
        self.alias_lbl = QtWidgets.QLabel(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.alias_lbl.setFont(font)
        self.alias_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.alias_lbl.setObjectName("alias_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.alias_lbl)
        self.alias_line_edit = QtWidgets.QLineEdit(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.alias_line_edit.setFont(font)
        self.alias_line_edit.setObjectName("alias_line_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alias_line_edit)
        self.firm_label = QtWidgets.QLabel(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.firm_label.setFont(font)
        self.firm_label.setAlignment(QtCore.Qt.AlignCenter)
        self.firm_label.setObjectName("firm_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.firm_label)
        self.firm_line_edit = QtWidgets.QLineEdit(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.firm_line_edit.setFont(font)
        self.firm_line_edit.setObjectName("firm_line_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firm_line_edit)
        self.firstname_lbl = QtWidgets.QLabel(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.firstname_lbl.setFont(font)
        self.firstname_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.firstname_lbl.setObjectName("firstname_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.firstname_lbl)
        self.name_line_edit = QtWidgets.QLineEdit(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name_line_edit.setFont(font)
        self.name_line_edit.setObjectName("name_line_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.name_line_edit)
        self.lastname_lbl = QtWidgets.QLabel(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lastname_lbl.setFont(font)
        self.lastname_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lastname_lbl.setObjectName("lastname_lbl")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.lastname_lbl)
        self.lastname_line_edit = QtWidgets.QLineEdit(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lastname_line_edit.setFont(font)
        self.lastname_line_edit.setObjectName("lastname_line_edit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lastname_line_edit)
        self.tax_id_lbl = QtWidgets.QLabel(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tax_id_lbl.setFont(font)
        self.tax_id_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.tax_id_lbl.setObjectName("tax_id_lbl")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.tax_id_lbl)
        self.taxid_line_edit = QtWidgets.QLineEdit(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.taxid_line_edit.setFont(font)
        self.taxid_line_edit.setObjectName("taxid_line_edit")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.taxid_line_edit)
        self.address_lbl = QtWidgets.QLabel(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.address_lbl.setFont(font)
        self.address_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.address_lbl.setObjectName("address_lbl")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.address_lbl)
        self.address_line_edit = QtWidgets.QLineEdit(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.address_line_edit.setFont(font)
        self.address_line_edit.setObjectName("address_line_edit")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.address_line_edit)
        self.postal_code_lbl = QtWidgets.QLabel(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.postal_code_lbl.setFont(font)
        self.postal_code_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.postal_code_lbl.setObjectName("postal_code_lbl")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.postal_code_lbl)
        self.postalcode_line_edit = QtWidgets.QLineEdit(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.postalcode_line_edit.setFont(font)
        self.postalcode_line_edit.setInputMask("")
        self.postalcode_line_edit.setObjectName("postalcode_line_edit")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.postalcode_line_edit)
        self.city_lbl = QtWidgets.QLabel(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.city_lbl.setFont(font)
        self.city_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.city_lbl.setObjectName("city_lbl")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.city_lbl)
        self.city_line_edit = QtWidgets.QLineEdit(CustomerDialog)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        self.city_line_edit.setFont(font)
        self.city_line_edit.setObjectName("city_line_edit")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.city_line_edit)
        self.label = QtWidgets.QLabel(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cash_radio_btn = QtWidgets.QRadioButton(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cash_radio_btn.setFont(font)
        self.cash_radio_btn.setIconSize(QtCore.QSize(25, 17))
        self.cash_radio_btn.setChecked(True)
        self.cash_radio_btn.setObjectName("cash_radio_btn")
        self.horizontalLayout_2.addWidget(self.cash_radio_btn)
        self.bank_transfer_radio_btn = QtWidgets.QRadioButton(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bank_transfer_radio_btn.setFont(font)
        self.bank_transfer_radio_btn.setIconSize(QtCore.QSize(25, 17))
        self.bank_transfer_radio_btn.setObjectName("bank_transfer_radio_btn")
        self.horizontalLayout_2.addWidget(self.bank_transfer_radio_btn)
        self.formLayout.setLayout(16, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(CustomerDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CustomerDialog)
        self.buttonBox.accepted.connect(CustomerDialog.accept)
        self.buttonBox.rejected.connect(CustomerDialog.reject)
        self.buttonBox.accepted.connect(CustomerDialog._validate_input)
        QtCore.QMetaObject.connectSlotsByName(CustomerDialog)

    def retranslateUi(self, CustomerDialog):
        _translate = QtCore.QCoreApplication.translate
        CustomerDialog.setWindowTitle(_translate("CustomerDialog", "Dialog"))
        self.alias_lbl.setText(_translate("CustomerDialog", "Nazwa"))
        self.firm_label.setText(_translate("CustomerDialog", "Firma"))
        self.firstname_lbl.setText(_translate("CustomerDialog", "Imię"))
        self.lastname_lbl.setText(_translate("CustomerDialog", "Nazwisko"))
        self.tax_id_lbl.setText(_translate("CustomerDialog", "NIP/PESEL"))
        self.address_lbl.setText(_translate("CustomerDialog", "Adres"))
        self.postal_code_lbl.setText(_translate("CustomerDialog", "Kod pocztowy"))
        self.city_lbl.setText(_translate("CustomerDialog", "Miasto"))
        self.label.setText(_translate("CustomerDialog", "Domyślna\n"
"płatność"))
        self.cash_radio_btn.setText(_translate("CustomerDialog", "Gotówka"))
        self.bank_transfer_radio_btn.setText(_translate("CustomerDialog", "Przelew"))

