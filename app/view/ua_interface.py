# coding: utf-8
# Standard Lib
# Third Party Lib
from PySide6.QtCore import Qt, Slot, QMetaObject, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QAbstractItemView, QSizePolicy, QSpacerItem, QGridLayout
from qfluentwidgets import Action, RoundMenu, MessageBox, ComboBox, BodyLabel, ListWidget, PushButton, DropDownPushButton, PixmapLabel, SimpleCardWidget
from qfluentwidgets import FluentIcon as FIF
# Local Lib
from ..core.piji_widget import pijiWidget
from .little_widgets import show_teaching_tip

class UaInterface(pijiWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        
        # Para
        self.initPara()

        self.init_action_dict()

        # Ui
        self.setupUi(self)   
        
        # Link slot
        self.list_action.currentItemChanged.connect(self.on_list_action_currentItemChanged)
        self.list_program.itemChanged.connect(self.on_list_program_itemChanged)

    def initPara(self):
        self.selected_action = None
        self.alias_array = []
        self.func_name_array = []
        self.selected_image = None
        self.selected_image_name = None
        self.all_flag = False

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

        # Manual Definnition
        self.combobox_type.addItems(['Program', 'Image', 'ROI', 'Excel', 'Template', 'Other'])
        self.init_list_action()
        self.label_selected_action_flasher()

        # 定义Action
        self.run_action = Action(FIF.PLAY,'运行')
        self.view_action = Action(FIF.VIEW, '查看代码')
        self.delete_action = Action(FIF.DELETE,'删除')
        self.new_action = Action(FIF.ADD,"新建")

        self.execute_action = Action(FIF.PLAY,"从列表运行")
        self.clear_action = Action(FIF.DELETE,'清空列表')
        self.create_action = Action(FIF.ADD,"从列表新建")

        # 链接Action槽函数
        self.run_action.triggered.connect(self.run_action_trigger)
        self.view_action.triggered.connect(self.view_action_trigger)
        self.delete_action.triggered.connect(self.delete_action_trigger)
        self.new_action.triggered.connect(self.new_action_trigger)

        self.execute_action.triggered.connect(self.execute_action_trigger)
        self.clear_action.triggered.connect(self.clear_action_trigger)
        self.create_action.triggered.connect(self.create_action_trigger)

        # 使用Actions创建Menu并赋予dropdownpushbutton类
        self.action_menu = RoundMenu()
        self.action_menu.addActions([self.run_action, self.view_action, self.delete_action, self.new_action])
        self.dropdownbutton_action.setMenu(self.action_menu)

        self.program_menu = RoundMenu()
        self.program_menu.addActions([self.execute_action, self.clear_action, self.create_action])
        self.dropdownbutton_program.setMenu(self.program_menu)

        self.queue_menu = RoundMenu()

        self.dropdownbutton_queue.setText(self.tr("Select image for process"))
        self.label_selected_image.setText(self.tr("Selected image:"))
        self.lavel_preview.setText(self.tr("Image Preview"))
        self.label_type.setText(self.tr("Type:"))
        self.label_channels.setText(self.tr("Channels:"))
        self.label_size.setText(self.tr("Size:"))
        self.label_slices.setText(self.tr("Slices:"))
        self.label_frames.setText(self.tr("Frames:"))
        self.label_selected_action.setText(self.tr("Selected action:"))
        self.dropdownbutton_program.setText(self.tr("From Program List"))
        self.dropdownbutton_action.setText(self.tr("From Action List"))
        self.button_save.setText(self.tr("Save Changes to Action List"))     

        QMetaObject.connectSlotsByName(ua_interface)      

    def init_action_dict(self):
        self.action_dict = {}
        self.re_action_dict = {}
        for _, dict in self.uas.json.items():
            alias = dict['alias']
            func_name = dict['func_name']
            self.action_dict[alias] = func_name
            self.re_action_dict[func_name] = alias

    def init_list_action(self):
        self.list_action.clear()
        action_type = self.combobox_type.currentText()

        for _, dict in self.uas.json.items():
            if dict['type'] == action_type:
                alias = dict['alias']
                self.list_action.addItem(alias)
            
            if action_type == 'Other':
                if dict['type'] not in ['Program', 'Image','ROI','Excel','Template','testrun']:
                    alias = dict['alias']
                    self.list_action.addItem(alias)
    
    @Slot()
    def on_combobox_type_currentIndexChanged(self):
        self.init_list_action()

    @Slot()
    def on_list_action_currentItemChanged(self):
        if self.list_action.currentItem() == None:
            self.selected_action = None
        else:
            self.selected_action = self.list_action.currentItem().text()
        self.label_selected_action_flasher()

    @Slot()
    def clear_action_trigger(self):
        w = MessageBox('提示',f'确认要清空Program列表吗?',self)
        if w.exec():
            self.list_program.clear()
            self.on_list_program_itemChanged()
    
    def run_action_with_alias(self, pu, alias, formal=True):
        func_name = self.action_dict[alias]
        # 更新pu
        pu.getua(func_name)
        history = getattr(pu, func_name)()
        if formal:
            pu.AddHistory(history)
            return history
        
    def run_action_with_alias_pus(self, pus, alias, formal=True):
        func_name = self.action_dict[alias]

        if len(pus.list)==0:
            # 更新pu
            pus.getua(func_name)
            history = getattr(pu, func_name)()
            if formal:
                pus.AddHistory(history)
                return history
        for idx, pu in enumerate(pus.list):
            # 更新pu
            pu.getua(func_name)

            if idx == 0:
                history = getattr(pu, func_name)()
                paras = history['paras']
            else:
                history = getattr(pu, func_name)(**paras)
            if formal:
                pu.AddHistory(history)
                

    @Slot()
    def run_action_trigger(self):
        if self.selected_action == None:
            show_teaching_tip(self,self.label_selected_action, 1, self.tr('No action is selected'))
            return
        alias = self.selected_action

        if self.selected_image_name == None:
            show_teaching_tip(self,self.label_selected_image, 1, self.tr('No image is selected'))
            return

        if self.all_flag == True:
            self.run_action_with_alias_pus(self.pus, alias)
        else:
            for pu in self.pus.list:
                # path是唯一的
                if pu.image == self.selected_image:
                    self.run_action_with_alias(pu, alias)

    @Slot()
    def view_action_trigger(self):
        if self.selected_action == None:
            show_teaching_tip(self,self.label_selected_action,1,self.tr('No action is selected'))
            return
        alias = self.selected_action
        func_name = self.action_dict[alias]
        type = self.uas.json[func_name]['type']
        code_template = self.uas.json[func_name]['code_template']

        # 带着参数换页面
        self.parent.scriptInterface.lineedit_alias.setText(alias)
        self.parent.scriptInterface.lineedit_funcname.setText(func_name)
        self.parent.scriptInterface.textedit_code_template.setPlainText(code_template)

        index = self.parent.scriptInterface.combobox_type.findText(type)
        if index >= 0:
            self.parent.scriptInterface.combobox_type.setCurrentIndex(index)
        else:
            self.parent.scriptInterface.combobox_type.setCurrentIndex(self.parent.scriptInterface.custom_index)
            self.parent.scriptInterface.combobox_type.setText(type)
            # 完事了要检查一下参数
            self.parent.scriptInterface.checkcontent()
        
        self.parent.switchTo(self.parent.scriptInterface)

        # # 这里后期要加一个检验
        # self.list_program.clear()
        # self.list_program.addItems(alias_list)

    @Slot()
    def execute_action_trigger(self):
        if self.list_program.count() == 0:
            show_teaching_tip(self,self.list_program, 1, self.tr('No action in program list'))
            return
        alias = self.selected_action

        if self.selected_image_name == 'None':
            show_teaching_tip(self,self.label_selected_image, 1, self.tr('No image is selected'))
            return

        if self.all_flag == True:
            # 或许需要修改
            for pu in self.pus.list:
                for alias in self.alias_array:
                    self.run_action_with_alias(pu, alias)
        else:
            for pu in self.pus.list:
                # path是唯一的
                if pu.image == self.selected_image:
                    for alias in self.alias_array:
                        self.run_action_with_alias(pu, alias)

    @Slot()
    def on_list_program_itemChanged(self):
        self.alias_array = [self.list_program.item(index).text() for index in range(self.list_program.count())]
        self.func_name_array = [self.action_dict[alias] for alias in self.alias_array]

    @Slot()
    def create_action_trigger(self):
        self.parent.scriptInterface.lineedit_alias.clear()
        self.parent.scriptInterface.lineedit_funcname.clear()
        code_template = 'ij = self.ij'
        for func_name in self.func_name_array:
            code_template += f'\nself.{func_name}()'
        self.parent.scriptInterface.textedit_code_template.setPlainText(code_template)

        # 重置 combobox_type 到默认值
        self.parent.scriptInterface.combobox_type.setCurrentIndex(0)
        
        # 检查一下参数
        self.parent.scriptInterface.checkcontent()
        self.parent.switchTo(self.parent.scriptInterface)
    
    @Slot()
    def on_button_save_clicked(self):
        change = self.uas.getchange()
        content = f"""变更如下
        增添：{change['added']}
        移除：{change['removed']}
        修改：{change['modified']}
        确认要更新操作列表吗？
        """
        w = MessageBox('提示',content,self.parent)
        if w.exec():
            if self.uas.save(self.parent.uas_json_path):
                self.pus.AutoSet()
                show_teaching_tip(self,self.button_save,3,self.tr('Action list is updated successfully'))
            else:
                show_teaching_tip(self,self.button_saven,1,self.tr('Something wrong when updating the action list'))

    @Slot()
    def delete_action_trigger(self):
        if self.selected_action == None:
            show_teaching_tip(self,self.label_selected_action,1,'未选中任何操作')
            return
        w = MessageBox('提示',f'确认要删除操作\"{self.selected_action}\"吗？',self)
        if w.exec():
            self.uas.remove(self.action_dict[self.selected_action])
            self.action_flasher()

    @Slot()
    def new_action_trigger(self):
        # 清空脚本页面
        self.parent.scriptInterface.lineedit_alias.clear()
        self.parent.scriptInterface.lineedit_funcname.clear()
        self.parent.scriptInterface.textedit_code_template.clear()

        # 重置 combobox_type 到默认值
        self.parent.scriptInterface.combobox_type.setCurrentIndex(0)
        
        # 检查一下参数
        self.parent.scriptInterface.checkcontent()
        self.parent.switchTo(self.parent.scriptInterface)

    @Slot()
    def select_image_action_trigger(self):
         # Sender返回触发此动作的发送者
        action = self.sender()
        pu = action.data()
        self.selected_image = pu.image
        self.selected_image_name = pu.name
        self.all_flag = False

        # 更新选定图像的标签
        self.label_selected_image_flasher()
        # 更新图像信息
        self.label_type.setText(self.tr('Type:') + f' {pu.typename}')
        self.label_channels.setText(self.tr('Channels:') + f' {pu.channels}')
        self.label_frames.setText(self.tr('Frames:') + f' {pu.frames}')
        self.label_slices.setText(self.tr('Slices:') + f' {pu.slices}')
        self.label_size.setText(self.tr('Size:') + f' {pu.width}*{pu.height}')

        pixmap = QPixmap(pu.preview)
        pixmap = pixmap.scaled(self.image_preview.size(), Qt.KeepAspectRatio)
        self.image_preview.setPixmap(pixmap)

    @Slot()
    def select_all_image_action_trigger(self):
         # Sender返回触发此动作的发送者
        action = self.sender()
        name, image = action.data()
        self.selected_image = image
        self.selected_image_name = name
        self.all_flag = True

        # 更新选定图像的标签
        self.label_selected_image_flasher()
        # 更新图像信息
        pu = self.pus.list[0] # 暂时用第一张
        self.label_type.setText(self.tr('Type:') + f' {pu.typename}')
        self.label_channels.setText(self.tr('Channels:') + f' {pu.channels}')
        self.label_frames.setText(self.tr('Frames:') + f' {pu.frames}')
        self.label_slices.setText(self.tr('Slices:') + f' {pu.slices}')
        self.label_size.setText(self.tr('Size:') + f' {pu.width}*{pu.height}')

        pixmap = QPixmap(pu.preview)
        pixmap = pixmap.scaled(self.image_preview.size(), Qt.KeepAspectRatio)
        self.image_preview.setPixmap(pixmap)

    def queue_flasher(self):
        # 清空queue菜单
        self.queue_menu.clear()
        
        # 建立queue菜单
        all = self.tr('All')
        all_action = Action(FIF.BOOK_SHELF, all)
        all_action.setData([all, None])
        all_action.triggered.connect(self.select_all_image_action_trigger)
        self.queue_menu.addAction(all_action)

        for pu in self.pus.list:
            name = pu.name
            setattr(self, 'action_forimg_' + name, Action(FIF.PHOTO, name))
            action = getattr(self,'action_forimg_' + name)
            action.setData(pu)
            action.triggered.connect(self.select_image_action_trigger)
            self.queue_menu.addAction(action)

            # 对pu进行初始化
            # self.run_action_with_alias(pu, '图像信息初始化',formal=False)
            # pu.imginfoinit() # imginfoinit是预设的一个ua

        self.dropdownbutton_queue.setMenu(self.queue_menu)

    def label_selected_image_flasher(self):
        self.label_selected_image.setText(self.tr('Selected image:')+f' {self.selected_image_name}')

    def label_selected_action_flasher(self):
        self.label_selected_action.setText(self.tr('Selected action:')+f' {self.selected_action}')

    def action_flasher(self):
        self.init_action_dict()
        self.init_list_action()