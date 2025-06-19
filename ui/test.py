import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel,
                             QPushButton, QHBoxLayout, QComboBox, QStackedWidget)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EduOS - Educational Operating System Simulator")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        title = QLabel("EduOS")
        title.setFont(QFont("Arial", 24))
        title.setStyleSheet("color: #2e86de;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        nav_layout = QHBoxLayout()
        self.scheduler_btn = QPushButton("⚙️ Process Scheduling")
        self.memory_btn = QPushButton("💾 Memory")
        self.fs_btn = QPushButton("📁 File System")
        self.terminal_btn = QPushButton("🖥️ Terminal")

        for btn in [self.scheduler_btn, self.memory_btn, self.fs_btn, self.terminal_btn]:
            btn.setStyleSheet("padding: 10px; font-size: 16px;")
            nav_layout.addWidget(btn)

        layout.addLayout(nav_layout)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.welcome_screen())

        layout.addWidget(self.stack)
        self.setLayout(layout)

        self.scheduler_btn.clicked.connect(self.load_scheduler)
        self.memory_btn.clicked.connect(self.load_memory)
        self.fs_btn.clicked.connect(self.load_filesystem)
        self.terminal_btn.clicked.connect(self.load_terminal)

    def welcome_screen(self):
        welcome = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Welcome to EduOS!\nSelect a module to begin simulation.")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 16))
        layout.addWidget(label)
        welcome.setLayout(layout)
        return welcome

    def load_scheduler(self):
        self.stack.setCurrentIndex(0)  # Placeholder for future widget

    def load_memory(self):
        self.stack.setCurrentIndex(0)  # Placeholder for future widget

    def load_filesystem(self):
        self.stack.setCurrentIndex(0)  # Placeholder for future widget

    def load_terminal(self):
        self.stack.setCurrentIndex(0)  # Placeholder for future widget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

