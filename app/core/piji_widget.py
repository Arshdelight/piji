from PySide6.QtWidgets import QWidget

class pijiWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.parent = parent
        self.ij = self.parent.ij
        self.uas = self.parent.uas
        self.pus = self.parent.pus