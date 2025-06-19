import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QStackedWidget, QPushButton, QFrame
)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class EduOSSimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EduOS - Educational Operating System Simulator")
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create top menu bar
        self.create_menu_bar(main_layout)
        
        # Create content area
        self.create_content_area(main_layout)
        
        # Set initial state
        self.stacked_widget.setCurrentIndex(0)

    def create_menu_bar(self, parent_layout):
        """Create the top menu bar with module buttons"""
        menu_frame = QFrame()
        menu_frame.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
                border-bottom: 2px solid #3498db;
            }
            QPushButton {
                background-color: #34495e;
                color: #ecf0f1;
                border: none;
                padding: 10px 15px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #3498db;
            }
        """)
        
        menu_layout = QHBoxLayout(menu_frame)
        menu_layout.setContentsMargins(10, 5, 10, 5)
        
        # Create menu buttons
        modules = [
            ("⚙️ Process Scheduling", "process"),
            ("💾 Memory", "memory"),
            ("📁 File System", "filesystem"),
            ("🖥️ Terminal", "terminal")
        ]
        
        self.menu_buttons = []
        for text, name in modules:
            btn = QPushButton(text)
            btn.setObjectName(name)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFont(QFont("Arial", 12, QFont.Bold))
            btn.clicked.connect(self.switch_module)
            menu_layout.addWidget(btn)
            self.menu_buttons.append(btn)
        
        parent_layout.addWidget(menu_frame)

    def create_content_area(self, parent_layout):
        """Create the content area with stacked widgets"""
        # Create stacked widget for different modules
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setStyleSheet("""
            QWidget {
                background-color: #ecf0f1;
            }
        """)
        
        # Create welcome screen
        self.create_welcome_screen()
        
        # Create placeholder screens for modules
        for i in range(4):
            placeholder = QWidget()
            layout = QVBoxLayout(placeholder)
            label = QLabel(f"Module {i+1} Content Area")
            label.setAlignment(Qt.AlignCenter)
            label.setFont(QFont("Arial", 24, QFont.Bold))
            label.setStyleSheet("color: #7f8c8d;")
            layout.addWidget(label)
            self.stacked_widget.addWidget(placeholder)
        
        parent_layout.addWidget(self.stacked_widget)

    def create_welcome_screen(self):
        """Create the welcome screen with logo and message"""
        welcome_widget = QWidget()
        layout = QVBoxLayout(welcome_widget)
        layout.setAlignment(Qt.AlignCenter)
        
        # Create logo (replace with actual logo path)
        logo_label = QLabel()
        logo_label.setAlignment(Qt.AlignCenter)
        logo_pixmap = QPixmap(300, 200)  # Placeholder - use actual image
        logo_pixmap.fill(Qt.darkGray)  # Placeholder color
        logo_label.setPixmap(logo_pixmap)
        
        # Create welcome text
        welcome_text = QLabel("Welcome to EduOS Simulator")
        welcome_text.setFont(QFont("Arial", 24, QFont.Bold))
        welcome_text.setStyleSheet("color: #2c3e50; margin-bottom: 5px;")
        welcome_text.setAlignment(Qt.AlignCenter)
        
        # Create instruction text
        instruction = QLabel("Select a module to begin simulation")
        instruction.setFont(QFont("Arial", 14))
        instruction.setStyleSheet("color: #7f8c8d;")
        instruction.setAlignment(Qt.AlignCenter)
        
        # Add to layout
        layout.addWidget(logo_label)
        layout.addWidget(welcome_text)
        layout.addWidget(instruction)
        
        self.stacked_widget.addWidget(welcome_widget)

    def switch_module(self):
        """Switch to the selected module"""
        sender = self.sender()
        module_name = sender.objectName()
        
        # Map button names to stack indices
        module_map = {
            "process": 1,
            "memory": 2,
            "filesystem": 3,
            "terminal": 4
        }
        
        if module_name in module_map:
            self.stacked_widget.setCurrentIndex(module_map[module_name])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EduOSSimulator()
    window.show()
    sys.exit(app.exec_())
