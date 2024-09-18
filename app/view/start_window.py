# coding:utf-8
# Standard Lib
import os
import sys
import scyjava
import psutil

# Third Party Lib
from PySide6.QtCore import Qt, QTimer, QRect, Slot, QMetaObject, QSize
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QSizePolicy, QSpacerItem, QGridLayout

from qfluentwidgets import (MSFluentTitleBar, isDarkTheme, InfoBar, InfoBarPosition, PrimaryPushButton, PushButton, ScrollArea,
                            BodyLabel, Slider)

import imagej

# Local Lib
from ..common import resource
from ..common.config import cfg
from .main_window import MainWindow

def isWin11():
    return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000


if isWin11():
    from qframelesswindow import AcrylicWindow as Window
else:
    from qframelesswindow import FramelessWindow as Window

class StartWindow(Window):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # Para
        self.initPara()

        # Ui
        self.setupUi(self)

        # Link Slot
        self.Slider.valueChanged.connect(self.memory_flasher)

    def initPara(self):
        self.loadConfig()
        self.ij = None
        self.mainwindow = None

    def loadConfig(self):
        self.imagej_path = cfg.get(cfg.imagej_path)
        self.java_path = cfg.get(cfg.java_path)
        self.imagej_memory = cfg.get(cfg.imagej_memory)
        
    def setupUi(self,start_window):
        # Designer Defination
        if not start_window.objectName():
            start_window.setObjectName(u"start_window")
        self.verticalLayout = QVBoxLayout(start_window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.button_launch = PrimaryPushButton(start_window)
        self.button_launch.setObjectName(u"button_launch")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_launch.sizePolicy().hasHeightForWidth())
        self.button_launch.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.button_launch)

        self.ScrollArea = ScrollArea(start_window)
        self.ScrollArea.setObjectName(u"ScrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ScrollArea.sizePolicy().hasHeightForWidth())
        self.ScrollArea.setSizePolicy(sizePolicy1)
        self.ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 189, 134))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Slider = Slider(self.scrollAreaWidgetContents)
        self.Slider.setObjectName(u"Slider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Slider.sizePolicy().hasHeightForWidth())
        self.Slider.setSizePolicy(sizePolicy2)
        self.Slider.setMinimumSize(QSize(0, 0))
        self.Slider.setSliderPosition(0)
        self.Slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Slider, 0, 0, 1, 1)

        self.label_imagej_memory = BodyLabel(self.scrollAreaWidgetContents)
        self.label_imagej_memory.setObjectName(u"label_imagej_memory")
        sizePolicy.setHeightForWidth(self.label_imagej_memory.sizePolicy().hasHeightForWidth())
        self.label_imagej_memory.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_imagej_memory, 0, 1, 1, 1)

        self.button_imagej_path = PushButton(self.scrollAreaWidgetContents)
        self.button_imagej_path.setObjectName(u"button_imagej_path")
        sizePolicy2.setHeightForWidth(self.button_imagej_path.sizePolicy().hasHeightForWidth())
        self.button_imagej_path.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_imagej_path, 1, 0, 1, 1)

        self.label_imagej_path = BodyLabel(self.scrollAreaWidgetContents)
        self.label_imagej_path.setObjectName(u"label_imagej_path")
        sizePolicy.setHeightForWidth(self.label_imagej_path.sizePolicy().hasHeightForWidth())
        self.label_imagej_path.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_imagej_path, 1, 1, 1, 1)

        self.button_java_path = PushButton(self.scrollAreaWidgetContents)
        self.button_java_path.setObjectName(u"button_java_path")
        sizePolicy2.setHeightForWidth(self.button_java_path.sizePolicy().hasHeightForWidth())
        self.button_java_path.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_java_path, 2, 0, 1, 1)

        self.label_java_path = BodyLabel(self.scrollAreaWidgetContents)
        self.label_java_path.setObjectName(u"label_java_path")
        sizePolicy.setHeightForWidth(self.label_java_path.sizePolicy().hasHeightForWidth())
        self.label_java_path.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_java_path, 2, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 9)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 9)
        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.ScrollArea)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        # Manual Defination
        self.setFixedSize(380, 260)

        self.setTitleBar(MSFluentTitleBar(self))
        self.titleBar.maxBtn.hide()
        # self.titleBar.setDoubleClickEnabled(False)

        self.titleBar.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px;
                color: black
            }
        """)

        self.setWindowIcon(QIcon(":/app/images/logo.png"))
        self.setWindowTitle('Piji')
        self.titleBar.raise_()

        if isWin11():
            self.windowEffect.setMicaEffect(self.winId(), isDarkTheme())
        else:
            color = QColor(25, 33, 42) if isDarkTheme(
            ) else QColor(240, 244, 249)
            self.setStyleSheet(f"StartWindow{{background: {color.name()}}}")
        
        

        # 设置slider
        total_memory = psutil.virtual_memory().total
        # 将内存转换为 GB 单位
        total_memory_gb = total_memory / (1024 ** 3)
        memory_limit = int(total_memory_gb * 2)
        self.Slider.setMaximum(memory_limit)
        if(self.imagej_memory > memory_limit):
            self.Slider.setValue(memory_limit)
            self.memory_flasher()
        else:
            self.Slider.setValue(self.imagej_memory)

        self.button_launch.setText(self.tr('Launch'))
        self.button_imagej_path.setText(self.tr("Select ImageJ Path"))
        self.button_java_path.setText(self.tr("Select Java Path"))
        self.label_imagej_memory.setText(f'{self.imagej_memory} GB ' + self.tr("memory will be set as maximum usage")) 
        self.label_imagej_path.setText(self.imagej_path)
        self.label_java_path.setText(self.java_path)

        QMetaObject.connectSlotsByName(start_window)

    @Slot()
    def on_button_imagej_path_clicked(self):
        imagej_path = QFileDialog.getExistingDirectory(self, 'Select ImageJ Root Path')

        if imagej_path:
            # Renew the imagej_path in the config file
            cfg.set(cfg.imagej_path, imagej_path)
            # Renew the path shown by label_path
            self.imagej_path = imagej_path
            self.label_imagej_path.setText(self.imagej_path)

    @Slot()
    def on_button_java_path_clicked(self):
        java_path = QFileDialog.getExistingDirectory(self, 'Select java Root Path')

        if java_path:
            # Renew the imagej_path in the config file
            cfg.set(cfg.java_path, java_path)
            # Renew the path shown by label_path
            self.java_path = java_path
            self.label_java_path.setText(self.java_path)

    @Slot()
    def on_button_launch_clicked(self):
        # 配置pyimagej启动相关参数
        os.environ["JAVA_HOME"] = self.java_path
        scyjava.config.add_options(f'-Xmx{self.imagej_memory}g')

        if not self.ij:
                self.ij = imagej.init(self.imagej_path, mode='interactive')
                
        if self.ij:
            InfoBar.success(
                self.tr('Success'),
                self.tr('Lauch Successful'),
                position=InfoBarPosition.TOP,
                parent=self.window()
            )
            # QTimer.singleShot(1000, self._showMainWindow())
            QTimer.singleShot(1000, self, self._showMainWindow())
            # self._showMainWindow()
        else:
            InfoBar.error(
                self.tr('Error'),
                self.tr('Launch Failed'),
                position=InfoBarPosition.TOP,
                duration=1000,
                parent=self.window()
            )

    @Slot()
    def memory_flasher(self):
        self.imagej_memory = self.Slider.value()
        self.label_imagej_memory.setText(f'{self.imagej_memory} GB ' + self.tr("memory will be set as maximum usage")) 
        cfg.set(cfg.imagej_memory, self.imagej_memory)

    def _showMainWindow(self):
        self.close()
        w = MainWindow(self.ij)
        w.show()

        return None

