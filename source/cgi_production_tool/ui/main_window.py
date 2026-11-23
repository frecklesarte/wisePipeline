# License
# Copyright

import sys

from PySide6.QtCore import QSize
#from PySide6.QtCore import QBuffer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set variables for the application, Title, Size, foo..
        self.setWindowTitle("CGI_Production_Structure")       
        
        # Set the control widgets for the Application
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)


app = QApplication(sys.argv)


window = MainWindow()
window.show()


app.exec()
