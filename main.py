# coding:utf-8
# Standard Lib
import os
import sys

# Third Party Lib
from PySide6.QtCore import Qt, QTranslator
from PySide6.QtWidgets import QApplication

from qfluentwidgets import FluentTranslator, setThemeColor

# Local Lib
from app.common.config import cfg
from app.view.start_window import StartWindow


# Enable Dpi Scale
if cfg.get(cfg.dpiScale) != "Auto":
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

# Create Application
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

# Internationalization
locale = cfg.get(cfg.language).value
translator = FluentTranslator(locale)
galleryTranslator = QTranslator()
galleryTranslator.load(locale, "app", ".", ":/app/i18n")

app.installTranslator(translator)
app.installTranslator(galleryTranslator)

# Create Main Window
# setThemeColor('#80F')

w = StartWindow()
w.show()

app.exec()
