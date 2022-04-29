from PySide6.QtWidgets import \
    QMainWindow, \
    QPushButton, \
    QLabel, \
    QLineEdit, \
    QGridLayout, \
    QWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 300, 600, 400)
        self.setWindowTitle("Satisfactoryplanner")
        self.label = QLabel()
        self.button = QPushButton("Refresh")
        self.button.released.connect(self.calculate_button)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QGridLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def calculate_button(self):
        self.label.setText("clicked")