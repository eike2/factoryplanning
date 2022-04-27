import sys

from PyQt5.QtWidgets import QApplication

from Satisfactory.database import createConnection
from Satisfactory.gui import Window


def main():
    """Factoryplanning main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection(r"C:\Users\eikew\OneDrive\Dokumente\My Games\Satisfactory\factoryplanning\Satisfactory.db"):
        sys.exit(1)
    # Create the main window if the connection succeeded
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec_())
