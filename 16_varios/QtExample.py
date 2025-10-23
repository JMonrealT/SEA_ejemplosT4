import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class GridButtons(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        
        # Matriz de botones 10x5
        for i in range(10):
            for j in range(5):
                button = QPushButton(f'Botón {i},{j}')
                button.clicked.connect(self.buttonClicked)
                grid.addWidget(button, i, j)
        
        self.setWindowTitle('Rejilla de Botones')
        self.setGeometry(100, 100, 600, 400)
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        print(f'Botón {sender.text()} ha sido pulsado')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridButtons()
    sys.exit(app.exec_())