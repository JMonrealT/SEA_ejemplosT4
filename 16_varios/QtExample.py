from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Mi App")
        self.setGeometry(100, 100, 400, 300)

        widget = QWidget()
        layout = QVBoxLayout()

        self.label = QLabel("Contador: 0")
        self.label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.label)

        boton = QPushButton("Click")
        boton.clicked.connect(self.click)
        layout.addWidget(boton)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def click(self):
        self.contador += 1
        self.label.setText(f"Contador: {self.contador}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())