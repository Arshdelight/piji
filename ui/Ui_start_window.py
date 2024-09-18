# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, PrimaryPushButton, PushButton, ScrollArea,
    Slider)

class Ui_start_window(object):
    def setupUi(self, start_window):
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


        self.retranslateUi(start_window)

        QMetaObject.connectSlotsByName(start_window)
    # setupUi

    def retranslateUi(self, start_window):
        self.button_launch.setText(QCoreApplication.translate("start_window", u"Launch", None))
        self.label_imagej_memory.setText(QCoreApplication.translate("start_window", u"1", None))
        self.button_imagej_path.setText(QCoreApplication.translate("start_window", u"Select ImageJ Path", None))
        self.label_imagej_path.setText(QCoreApplication.translate("start_window", u"2", None))
        self.button_java_path.setText(QCoreApplication.translate("start_window", u"Select Java Path", None))
        self.label_java_path.setText(QCoreApplication.translate("start_window", u"3", None))
        pass
    # retranslateUi

