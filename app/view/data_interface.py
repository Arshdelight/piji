# coding: utf-8
# Standard Lib
import os
import shutil
# Third Party Lib
from PySide6.QtCore import Qt, Slot, QMetaObject, QSize
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QListWidgetItem, QVBoxLayout, QHBoxLayout, QSizePolicy, QGridLayout, QSpacerItem
from qfluentwidgets import PushButton, ListWidget, PrimaryPushButton, SimpleCardWidget
# Local Lib
from ..core.piji_widget import pijiWidget
from .little_widgets import show_teaching_tip

class DataInterface(pijiWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.initPara()

        self.linkSlot()

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

        # Manual Definition
        self.button_select_image.setText(self.tr("Select Image Files"))
        self.button_select_roi.setText(self.tr("Select ROI Zips"))
        self.button_create.setText(self.tr("Generate Analysis Queue"))
        self.button_load.setText(self.tr("Load Existing Queue"))

        QMetaObject.connectSlotsByName(data_interface)
    
    def initPara(self):
        self.images = []
        self.image_names = []
        self.rois_zips = []
        self.rois_zip_names = []

    def linkSlot(self):
        return
    
    @Slot()
    def on_button_select_image_clicked(self):
        # 打开文件对话框选择文件
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Tiff Image (*.tif)")
        if file_dialog.exec():
            self.images = file_dialog.selectedFiles()

            # 分离文件名
            self.image_names = [os.path.splitext(os.path.basename(f))[0] for f in self.images]

            # 打印结果
            # print("Images:", self.images)
            # print("Image names:", self.image_names)
            # print("Postfixes:", self.postfixes)

            # 更新list_image
            self.list_image.clear()
            for name in self.image_names:
                item = QListWidgetItem(name)
                self.list_image.addItem(item)

        return
    
    @Slot()
    def on_button_select_roi_clicked(self):
        # 打开文件对话框选择文件
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Roi Zip (*.zip)")
        if file_dialog.exec():
            self.rois_zips = file_dialog.selectedFiles()

            # 分离文件名
            self.rois_zip_names = [os.path.splitext(os.path.basename(f))[0] for f in self.rois_zips]

            # 打印结果
            # print("Rois zips:", self.rois_zips)
            # print("Rois zip names:", self.rois_zip_names)

            # 更新list_roi
            self.list_roi.clear()
            for name in self.rois_zip_names:
                item = QListWidgetItem(name)
                self.list_roi.addItem(item)
        return
    
    @Slot()
    def on_button_create_clicked(self):
        # 新的路径列表
        self.shadow_images = []
        self.shadow_image_names = self.image_names.copy()
        self.shadow_rois_zips = []
        self.shadow_rois_zip_names = []

        # 获取shadow路径
        imgData_path = self.parent.imgData_path
        # 清空imgData_path目录
        if os.path.exists(imgData_path):
            shutil.rmtree(imgData_path)
        
        # 重新创建imgData_path目录
        os.makedirs(imgData_path)

        # shadow data
        if self.images:
            for index, image in enumerate(self.images):
                # 获取图像名称和路径
                image_name = self.image_names[index]
                destination_folder = os.path.join(imgData_path, image_name)
                # 创建目标文件夹，如果文件夹不存在
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                # 拷贝图像到目标文件夹
                destination_path = os.path.join(destination_folder, os.path.basename(image))
                shutil.copy(image, destination_path)
                self.shadow_images.append(destination_path)

                # 检查有没有提供roi
                expected_rois_zip_name = image_name + '_rois'
                if expected_rois_zip_name in self.rois_zip_names:
                    rois_index = self.rois_zip_names.index(expected_rois_zip_name)
                    rois_zip = self.rois_zips[rois_index]
                    # 拷贝roi到目标文件夹
                    destination_path = os.path.join(destination_folder, os.path.basename(rois_zip))
                    shutil.copy(rois_zip, destination_path)
                    self.shadow_rois_zips.append(destination_path)
                    self.shadow_rois_zip_names.append(expected_rois_zip_name)
        self.pus.CreateQueue(self)
        self.parent.uaInterface.queue_flasher()
        show_teaching_tip(self, self.button_create, 3, self.tr('Analysis queue has confirmed'))
        return
    
    @Slot()
    def on_button_load_clicked(self):
        # 获取imgData路径
        imgData_path = self.parent.imgData_path
        self.pus.LoadQueue(imgData_path)
        self.parent.uaInterface.queue_flasher()
        show_teaching_tip(self, self.button_load, 3, self.tr('Analysis queue has confirmed'))