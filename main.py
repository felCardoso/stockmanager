import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_InventoryManager
from models.inventory import Inventory


class InventoryManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_InventoryManager()
        self.ui.setup_ui(self)
        self.inventory = Inventory()
        self.is_dark_theme = False  # Track the current theme

        # Connect signals to slots
        self.ui.add_product_action.triggered.connect(self.open_add_product_dialog)
        self.ui.edit_product_action.triggered.connect(self.open_edit_product_dialog)
        self.ui.toggle_theme_action.triggered.connect(self.toggle_theme)
        self.ui.add_button.clicked.connect(self.open_add_product_dialog)
        self.ui.edit_button.clicked.connect(self.open_edit_product_dialog)

        # Set the default background color
        self.set_background_color("white")

    def set_background_color(self, color):
        if color == "black":
            self.setStyleSheet("background-color: black; color: white;")
        elif color == "white":
            self.setStyleSheet("background-color: white; color: black;")

    def toggle_theme(self):
        if self.is_dark_theme:
            self.set_background_color("white")
        else:
            self.set_background_color("black")
        self.is_dark_theme = not self.is_dark_theme

    def open_add_product_dialog(self):
        # Implement the method to open the add product dialog
        pass

    def open_edit_product_dialog(self):
        # Implement the method to open the edit product dialog
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryManager()
    window.show()
    sys.exit(app.exec_())
