# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QListWidgetItem,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, ListWidget, PrimaryPushButton, PushButton,
    SimpleCardWidget)

class Ui_data_interface(object):
    def setupUi(self, data_interface):
        if not data_interface.objectName():
            data_interface.setObjectName(u"data_interface")
        data_interface.resize(586, 306)
        self.horizontalLayout = QHBoxLayout(data_interface)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_create = PrimaryPushButton(data_interface)
        self.button_create.setObjectName(u"button_create")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_create.sizePolicy().hasHeightForWidth())
        self.button_create.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.button_create)

        self.button_load = PrimaryPushButton(data_interface)
        self.button_load.setObjectName(u"button_load")
        sizePolicy.setHeightForWidth(self.button_load.sizePolicy().hasHeightForWidth())
        self.button_load.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.button_load)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_select_image = PushButton(data_interface)
        self.button_select_image.setObjectName(u"button_select_image")
        sizePolicy.setHeightForWidth(self.button_select_image.sizePolicy().hasHeightForWidth())
        self.button_select_image.setSizePolicy(sizePolicy)
        self.button_select_image.setMinimumSize(QSize(200, 32))
        self.button_select_image.setMaximumSize(QSize(256, 32))

        self.gridLayout.addWidget(self.button_select_image, 0, 0, 1, 1)

        self.button_select_roi = PushButton(data_interface)
        self.button_select_roi.setObjectName(u"button_select_roi")
        sizePolicy.setHeightForWidth(self.button_select_roi.sizePolicy().hasHeightForWidth())
        self.button_select_roi.setSizePolicy(sizePolicy)
        self.button_select_roi.setMinimumSize(QSize(200, 32))
        self.button_select_roi.setMaximumSize(QSize(256, 32))

        self.gridLayout.addWidget(self.button_select_roi, 0, 1, 1, 1)

        self.image_card = SimpleCardWidget(data_interface)
        self.image_card.setObjectName(u"image_card")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image_card.sizePolicy().hasHeightForWidth())
        self.image_card.setSizePolicy(sizePolicy1)
        self.image_card.setMinimumSize(QSize(256, 0))
        self.image_card.setMaximumSize(QSize(256, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.image_card)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.list_image = ListWidget(self.image_card)
        self.list_image.setObjectName(u"list_image")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.list_image.sizePolicy().hasHeightForWidth())
        self.list_image.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.list_image)


        self.gridLayout.addWidget(self.image_card, 1, 0, 1, 1)

        self.SimpleCardWidget = SimpleCardWidget(data_interface)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
        sizePolicy1.setHeightForWidth(self.SimpleCardWidget.sizePolicy().hasHeightForWidth())
        self.SimpleCardWidget.setSizePolicy(sizePolicy1)
        self.SimpleCardWidget.setMinimumSize(QSize(256, 0))
        self.SimpleCardWidget.setMaximumSize(QSize(256, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.SimpleCardWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.list_roi = ListWidget(self.SimpleCardWidget)
        self.list_roi.setObjectName(u"list_roi")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.list_roi.sizePolicy().hasHeightForWidth())
        self.list_roi.setSizePolicy(sizePolicy3)
        self.list_roi.setMaximumSize(QSize(256, 16777215))

        self.verticalLayout_4.addWidget(self.list_roi)


        self.gridLayout.addWidget(self.SimpleCardWidget, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(data_interface)

        QMetaObject.connectSlotsByName(data_interface)
    # setupUi

    def retranslateUi(self, data_interface):
        self.button_create.setText(QCoreApplication.translate("data_interface", u"Generate Analysis Queue", None))
        self.button_load.setText(QCoreApplication.translate("data_interface", u"Load Existing Queue", None))
        self.button_select_image.setText(QCoreApplication.translate("data_interface", u"Select Image Files", None))
        self.button_select_roi.setText(QCoreApplication.translate("data_interface", u"Select ROI Zips", None))
        pass
    # retranslateUi

