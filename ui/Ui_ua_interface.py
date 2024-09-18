# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ua_interface.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QListWidgetItem, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, DropDownPushButton,
    ListWidget, PixmapLabel, PushButton, SimpleCardWidget)

class Ui_ua_interface(object):
    def setupUi(self, ua_interface):
        if not ua_interface.objectName():
            ua_interface.setObjectName(u"ua_interface")
        ua_interface.resize(612, 695)
        self.verticalLayout_5 = QVBoxLayout(ua_interface)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dropdownbutton_queue = DropDownPushButton(ua_interface)
        self.dropdownbutton_queue.setObjectName(u"dropdownbutton_queue")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dropdownbutton_queue.sizePolicy().hasHeightForWidth())
        self.dropdownbutton_queue.setSizePolicy(sizePolicy)
        self.dropdownbutton_queue.setMinimumSize(QSize(256, 0))
        self.dropdownbutton_queue.setMaximumSize(QSize(256, 16777215))

        self.horizontalLayout_3.addWidget(self.dropdownbutton_queue)

        self.label_selected_image = BodyLabel(ua_interface)
        self.label_selected_image.setObjectName(u"label_selected_image")

        self.horizontalLayout_3.addWidget(self.label_selected_image)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.preview_card = SimpleCardWidget(ua_interface)
        self.preview_card.setObjectName(u"preview_card")
        self.horizontalLayout_4 = QHBoxLayout(self.preview_card)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lavel_preview = BodyLabel(self.preview_card)
        self.lavel_preview.setObjectName(u"lavel_preview")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lavel_preview.sizePolicy().hasHeightForWidth())
        self.lavel_preview.setSizePolicy(sizePolicy1)
        self.lavel_preview.setMaximumSize(QSize(16777215, 19))

        self.verticalLayout.addWidget(self.lavel_preview, 0, Qt.AlignHCenter)

        self.image_preview = PixmapLabel(self.preview_card)
        self.image_preview.setObjectName(u"image_preview")
        sizePolicy.setHeightForWidth(self.image_preview.sizePolicy().hasHeightForWidth())
        self.image_preview.setSizePolicy(sizePolicy)
        self.image_preview.setMinimumSize(QSize(256, 256))
        self.image_preview.setMaximumSize(QSize(256, 256))

        self.verticalLayout.addWidget(self.image_preview)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(256, 19, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_5)

        self.label_type = BodyLabel(self.preview_card)
        self.label_type.setObjectName(u"label_type")

        self.verticalLayout_2.addWidget(self.label_type)

        self.label_channels = BodyLabel(self.preview_card)
        self.label_channels.setObjectName(u"label_channels")

        self.verticalLayout_2.addWidget(self.label_channels)

        self.label_size = BodyLabel(self.preview_card)
        self.label_size.setObjectName(u"label_size")

        self.verticalLayout_2.addWidget(self.label_size)

        self.label_slices = BodyLabel(self.preview_card)
        self.label_slices.setObjectName(u"label_slices")

        self.verticalLayout_2.addWidget(self.label_slices)

        self.label_frames = BodyLabel(self.preview_card)
        self.label_frames.setObjectName(u"label_frames")

        self.verticalLayout_2.addWidget(self.label_frames)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_5.addWidget(self.preview_card)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.combobox_type = ComboBox(ua_interface)
        self.combobox_type.setObjectName(u"combobox_type")
        sizePolicy.setHeightForWidth(self.combobox_type.sizePolicy().hasHeightForWidth())
        self.combobox_type.setSizePolicy(sizePolicy)
        self.combobox_type.setMinimumSize(QSize(256, 0))
        self.combobox_type.setMaximumSize(QSize(256, 16777215))

        self.horizontalLayout_2.addWidget(self.combobox_type)

        self.label_selected_action = BodyLabel(ua_interface)
        self.label_selected_action.setObjectName(u"label_selected_action")

        self.horizontalLayout_2.addWidget(self.label_selected_action)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.list_action = ListWidget(ua_interface)
        self.list_action.setObjectName(u"list_action")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.list_action.sizePolicy().hasHeightForWidth())
        self.list_action.setSizePolicy(sizePolicy2)
        self.list_action.setMinimumSize(QSize(0, 150))
        self.list_action.setMaximumSize(QSize(250, 16777215))
        self.list_action.setDragEnabled(True)
        self.list_action.setDragDropMode(QAbstractItemView.DragOnly)

        self.horizontalLayout.addWidget(self.list_action)

        self.list_program = ListWidget(ua_interface)
        self.list_program.setObjectName(u"list_program")
        sizePolicy2.setHeightForWidth(self.list_program.sizePolicy().hasHeightForWidth())
        self.list_program.setSizePolicy(sizePolicy2)
        self.list_program.setMinimumSize(QSize(0, 150))
        self.list_program.setMaximumSize(QSize(250, 16777215))
        self.list_program.setDragEnabled(True)
        self.list_program.setDragDropMode(QAbstractItemView.DragDrop)
        self.list_program.setDefaultDropAction(Qt.MoveAction)

        self.horizontalLayout.addWidget(self.list_program)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.dropdownbutton_program = DropDownPushButton(ua_interface)
        self.dropdownbutton_program.setObjectName(u"dropdownbutton_program")
        sizePolicy1.setHeightForWidth(self.dropdownbutton_program.sizePolicy().hasHeightForWidth())
        self.dropdownbutton_program.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.dropdownbutton_program, 0, 1, 1, 1)

        self.dropdownbutton_action = DropDownPushButton(ua_interface)
        self.dropdownbutton_action.setObjectName(u"dropdownbutton_action")
        sizePolicy1.setHeightForWidth(self.dropdownbutton_action.sizePolicy().hasHeightForWidth())
        self.dropdownbutton_action.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.dropdownbutton_action, 0, 0, 1, 1)

        self.button_save = PushButton(ua_interface)
        self.button_save.setObjectName(u"button_save")
        sizePolicy1.setHeightForWidth(self.button_save.sizePolicy().hasHeightForWidth())
        self.button_save.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.button_save, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.retranslateUi(ua_interface)

        QMetaObject.connectSlotsByName(ua_interface)
    # setupUi

    def retranslateUi(self, ua_interface):
        self.dropdownbutton_queue.setText(QCoreApplication.translate("ua_interface", u"Select image for process", None))
        self.label_selected_image.setText(QCoreApplication.translate("ua_interface", u"Selected image:", None))
        self.lavel_preview.setText(QCoreApplication.translate("ua_interface", u"Image Preview", None))
        self.label_type.setText(QCoreApplication.translate("ua_interface", u"Type:", None))
        self.label_channels.setText(QCoreApplication.translate("ua_interface", u"Channels:", None))
        self.label_size.setText(QCoreApplication.translate("ua_interface", u"Size:", None))
        self.label_slices.setText(QCoreApplication.translate("ua_interface", u"Slices:", None))
        self.label_frames.setText(QCoreApplication.translate("ua_interface", u"Frames:", None))
        self.label_selected_action.setText(QCoreApplication.translate("ua_interface", u"Selected Action:", None))
        self.dropdownbutton_program.setText(QCoreApplication.translate("ua_interface", u"From Program List", None))
        self.dropdownbutton_action.setText(QCoreApplication.translate("ua_interface", u"From Action List", None))
        self.button_save.setText(QCoreApplication.translate("ua_interface", u"Save Changes to Action List", None))
        pass
    # retranslateUi

