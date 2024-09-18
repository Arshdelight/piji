# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'script_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, DropDownPushButton, EditableComboBox, LineEdit,
    PrimaryPushButton, PushButton, TextEdit)

class Ui_script_interface(object):
    def setupUi(self, script_interface):
        if not script_interface.objectName():
            script_interface.setObjectName(u"script_interface")
        script_interface.resize(723, 584)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(script_interface.sizePolicy().hasHeightForWidth())
        script_interface.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(script_interface)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_alias = BodyLabel(script_interface)
        self.label_alias.setObjectName(u"label_alias")

        self.verticalLayout.addWidget(self.label_alias)

        self.label_funcname = BodyLabel(script_interface)
        self.label_funcname.setObjectName(u"label_funcname")

        self.verticalLayout.addWidget(self.label_funcname)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineedit_alias = LineEdit(script_interface)
        self.lineedit_alias.setObjectName(u"lineedit_alias")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineedit_alias.sizePolicy().hasHeightForWidth())
        self.lineedit_alias.setSizePolicy(sizePolicy1)
        self.lineedit_alias.setMinimumSize(QSize(125, 33))
        self.lineedit_alias.setMaximumSize(QSize(125, 33))

        self.verticalLayout_2.addWidget(self.lineedit_alias)

        self.lineedit_funcname = LineEdit(script_interface)
        self.lineedit_funcname.setObjectName(u"lineedit_funcname")
        sizePolicy1.setHeightForWidth(self.lineedit_funcname.sizePolicy().hasHeightForWidth())
        self.lineedit_funcname.setSizePolicy(sizePolicy1)
        self.lineedit_funcname.setMinimumSize(QSize(125, 33))
        self.lineedit_funcname.setMaximumSize(QSize(125, 33))

        self.verticalLayout_2.addWidget(self.lineedit_funcname)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_action_type = BodyLabel(script_interface)
        self.label_action_type.setObjectName(u"label_action_type")

        self.verticalLayout_3.addWidget(self.label_action_type)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.combobox_type = EditableComboBox(script_interface)
        self.combobox_type.setObjectName(u"combobox_type")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.combobox_type.sizePolicy().hasHeightForWidth())
        self.combobox_type.setSizePolicy(sizePolicy2)
        self.combobox_type.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.combobox_type)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_code_template = BodyLabel(script_interface)
        self.label_code_template.setObjectName(u"label_code_template")

        self.horizontalLayout_3.addWidget(self.label_code_template)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textedit_code_template = TextEdit(script_interface)
        self.textedit_code_template.setObjectName(u"textedit_code_template")

        self.horizontalLayout.addWidget(self.textedit_code_template)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_4 = QSpacerItem(17, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.button_template = DropDownPushButton(script_interface)
        self.button_template.setObjectName(u"button_template")

        self.verticalLayout_6.addWidget(self.button_template)

        self.button_run = PrimaryPushButton(script_interface)
        self.button_run.setObjectName(u"button_run")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_run.sizePolicy().hasHeightForWidth())
        self.button_run.setSizePolicy(sizePolicy3)

        self.verticalLayout_6.addWidget(self.button_run)

        self.button_new = PrimaryPushButton(script_interface)
        self.button_new.setObjectName(u"button_new")
        sizePolicy3.setHeightForWidth(self.button_new.sizePolicy().hasHeightForWidth())
        self.button_new.setSizePolicy(sizePolicy3)

        self.verticalLayout_6.addWidget(self.button_new)

        self.button_modify = PrimaryPushButton(script_interface)
        self.button_modify.setObjectName(u"button_modify")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.button_modify.sizePolicy().hasHeightForWidth())
        self.button_modify.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.button_modify)

        self.button_save = PrimaryPushButton(script_interface)
        self.button_save.setObjectName(u"button_save")

        self.verticalLayout_6.addWidget(self.button_save)

        self.button_trans = PrimaryPushButton(script_interface)
        self.button_trans.setObjectName(u"button_trans")
        sizePolicy4.setHeightForWidth(self.button_trans.sizePolicy().hasHeightForWidth())
        self.button_trans.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.button_trans)

        self.verticalSpacer_5 = QSpacerItem(17, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(script_interface)

        QMetaObject.connectSlotsByName(script_interface)
    # setupUi

    def retranslateUi(self, script_interface):
        self.label_alias.setText(QCoreApplication.translate("script_interface", u"Action alias:", None))
        self.label_funcname.setText(QCoreApplication.translate("script_interface", u"Action Funcname:", None))
        self.label_action_type.setText(QCoreApplication.translate("script_interface", u"Action type:", None))
        self.label_code_template.setText(QCoreApplication.translate("script_interface", u"Code template:", None))
        self.button_template.setText(QCoreApplication.translate("script_interface", u"Templalte", None))
        self.button_run.setText(QCoreApplication.translate("script_interface", u"Test Run", None))
        self.button_new.setText(QCoreApplication.translate("script_interface", u"Create", None))
        self.button_modify.setText(QCoreApplication.translate("script_interface", u"Modify", None))
        self.button_save.setText(QCoreApplication.translate("script_interface", u"Save", None))
        self.button_trans.setText(QCoreApplication.translate("script_interface", u"{ \u2192 {{", None))
        pass
    # retranslateUi

