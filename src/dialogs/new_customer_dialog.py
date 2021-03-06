from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox, QApplication

from database import data
from dialogs.customer_dialog import CustomersDialog


class NewCustomerDialog(CustomersDialog):
    def __init__(self, session):
        super().__init__(session)

    def _commit_to_database(self):
        # customer existence check
        stmt = self.session.query(data.Customer).filter(data.Customer.alias == self.alias_line_edit.text())
        # https://stackoverflow.com/questions/7646173/sqlalchemy-exists-for-query
        if self.session.query(stmt.exists()).scalar():
            QMessageBox.warning(
                self, "Duplikat",
                "Kontrahent o takiej nazwie już istnieje!"
            )
            return

        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        customer = data.Customer(
            alias=self.alias_line_edit.text(),
            firm_name=self.firm_line_edit.text(),
            last_name=self.lastname_line_edit.text(),
            first_name=self.name_line_edit.text(),
            tax_id=self.taxid_line_edit.text(),
            address=self.address_line_edit.text(),
            postal_code=self.postalcode_line_edit.text(),
            city=self.city_line_edit.text(),
            payment=self.cash_radio_btn.isChecked()
        )

        customer.template = []
        self.session.add(customer)
        self.session.commit()
        QMessageBox.information(
            self, 'Informacja',
            'Kontrahent dodany pomyślnie'
        )
        QApplication.restoreOverrideCursor()