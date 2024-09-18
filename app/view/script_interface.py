# coding:utf-8
# Standard Lib
import keyword
# Third Party Lib
from PySide6.QtCore import Slot, QSize, QMetaObject
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QWidgetItem
from qfluentwidgets import BodyLabel, LineEdit, EditableComboBox, TextEdit, PrimaryPushButton, DropDownPushButton, RoundMenu, Action, MessageBox
from qfluentwidgets import FluentIcon as FIF
# Local Lib
from ..core.piji_widget import pijiWidget
from .little_widgets import show_teaching_tip


class ScriptInterface(pijiWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        
        # ui
        self.setupUi(self)

        # 获取方法
        self.action_flasher = parent.uaInterface.action_flasher

        # 链接槽函数
        self.lineedit_alias.textChanged.connect(self.checkcontent)
        self.lineedit_funcname.textChanged.connect(self.checkcontent)
        self.textedit_code_template.textChanged.connect(self.checkcontent)
        self.combobox_type.textChanged.connect(self.checkcontent)
        self.combobox_type.currentIndexChanged.connect(self.custom_type_activater)

    def setupUi(self, script_interface):
        # Designer Definition
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

        # Manual Definitions
        self.textedit_code_template.setTabStopDistance(4 * self.textedit_code_template.fontMetrics().horizontalAdvance(' ')) # 设置textedit中Tab宽度为4个空格的宽度
        self.combobox_type.addItems(['Program','Image','ROI','Excel','Template',self.tr('Custom')])
        self.custom_index = self.combobox_type.findText(self.tr('Custom'))

        self.button_new.setDisabled(True)
        self.button_modify.setDisabled(True)

        # 定义Action
        self.python_action = Action(FIF.COPY,'Python')
        self.macro_action = Action(FIF.COPY, 'Macro')
        # 链接Action槽函数
        self.python_action.triggered.connect(self.python_action_trigger)
        self.macro_action.triggered.connect(self.macro_action_trigger)
        # 使用Actions创建Menu并赋予dropdownpushbutton类
        self.template_menu = RoundMenu()
        #self.template_menu.addActions([self.python_action, self.macro_action])
        self.button_template.setMenu(self.template_menu)
        self.template_menu.addActions([self.python_action, self.macro_action]) # 测试一下，可以先绑定再处理Menu，这一条暂时留着

        self.button_trans.setText(u"{ \u2192 {{")

        self.label_alias.setText(self.tr("Action alias:"))        
        self.label_funcname.setText(self.tr("Action Funcname:"))        
        self.label_action_type.setText(self.tr("Action type:"))        
        self.label_code_template.setText(self.tr("Code template:"))        
        self.button_run.setText(self.tr("Test Run"))        
        self.button_new.setText(self.tr("Create"))        
        self.button_modify.setText(self.tr("Modify"))  
        self.button_save.setText(self.tr("Save"))               
        self.button_template.setText(self.tr("Templalte"))

        QMetaObject.connectSlotsByName(script_interface)

    @Slot()
    def on_button_run_clicked(self):
        # 只需要选择好code_type和填写code_template就可以运行
        func_name = 'testrun'
        alias = 'testrun'
        type = 'testrun'
        code_template = self.textedit_code_template.toPlainText()

        dict = {'func_name':func_name, 'alias':alias, 'type':type, 'code_template':code_template}

        # 先检验
        if self.parent.uaInterface.selected_image_name == None:
            show_teaching_tip(self,self.button_run, 1, self.tr('No image is selected'))
            return

        if not self.uas.modify(dict):
            # 如果配置文件里没有testrun就新建
            self.uas.addjson(dict)

        show_teaching_tip(self, self.button_run, 3, self.tr('Test action initialized'))

        if self.parent.uaInterface.all_flag == True:
            self.parent.uaInterface.run_action_with_alias_pus(self.pus, alias,formal=False)
        else:
            for pu in self.pus.list:
                # path是唯一的
                if pu.image == self.parent.uaInterface.selected_image:
                    self.parent.uaInterface.run_action_with_alias(pu, alias, formal=False)

    @Slot()
    def on_button_new_clicked(self):
        func_name = self.lineedit_funcname.text()
        alias = self.lineedit_alias.text()
        # code_type = self.combobox_code_type.currentText()
        type = self.combobox_type.currentText()
        code_template = self.textedit_code_template.toPlainText()

        dict = {'func_name':func_name, 'alias':alias, 'type':type, 'code_template':code_template}
        try:
            self.uas.addjson(dict)
            self.action_flasher()
            self.checkcontent()
            show_teaching_tip(self, self.button_new, 3, self.tr('Script added successfully'))
        except:
            show_teaching_tip(self, self.button_new, 1, self.tr('Alias is used'))
            
    @Slot()
    def on_button_modify_clicked(self):
        func_name = self.lineedit_funcname.text()
        alias = self.lineedit_alias.text()
        # code_type = self.combobox_code_type.currentText()
        type = self.combobox_type.currentText()
        code_template = self.textedit_code_template.toPlainText()

        dict = {'func_name':func_name, 'alias':alias, 'type':type, 'code_template':code_template}

        if self.uas.modify(dict):
            self.action_flasher()
            self.checkcontent()
            show_teaching_tip(self, self.button_modify, 3, self.tr('Script modified successfully'))
        else:
            show_teaching_tip(self, self.button_modify, 1, self.tr('Funcname isn\'t exist'))

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
                show_teaching_tip(self,self.button_save,1,self.tr('Something wrong when updating the action list'))

    @Slot()
    def on_button_trans_clicked(self):
        code_template = self.textedit_code_template.toPlainText()
        code_template = code_template.replace('{','{{').replace('}','}}')
        self.textedit_code_template.setPlainText(code_template)
        print('Trans completed')

    @Slot()
    def checkcontent(self):
        alias = self.lineedit_alias.text()
        func_name = self.lineedit_funcname.text()
        type = self.combobox_type.currentText()

        code_template = self.textedit_code_template.toPlainText()

        if (alias != None) and (self.is_valid_function_name(func_name)):
            if func_name in self.uas.json.keys():
                self.button_new.setDisabled(True)
                if (
                    self.uas.json[func_name]['code_template'] == code_template
                    and self.uas.json[func_name]['type'] == type
                    and self.uas.json[func_name]['alias'] == alias
                ):
                    self.button_modify.setDisabled(True)
                else:
                    self.button_modify.setDisabled(False)
            else:
                self.button_new.setDisabled(False)
                self.button_modify.setDisabled(True)
        else:
            self.button_modify.setDisabled(True)
            self.button_new.setDisabled(True)

    def is_valid_function_name(self, string):
        # 检查是否是合法的标识符
        if not string.isidentifier():
            return False
        
        # 检查是否是关键字
        if keyword.iskeyword(string):
            return False
        
        return True        
    
    @Slot()
    def python_action_trigger(self):
        try:
            template = self.uas.json['python_template']['code_template']
            self.textedit_code_template.setPlainText(template)
        except:
            print(self.tr("err: Can't find pre-set python template"))
    
    @Slot()
    def macro_action_trigger(self):
        try:
            template = self.uas.json['macro_template']['code_template']
            self.textedit_code_template.setPlainText(template)
        except:
            print(self.tr("err: Can't find pre-set macro template"))
    
    @Slot()
    def custom_type_activater(self, index):
        if index == self.custom_index:
            self.combobox_type.setReadOnly(False)
            if self.combobox_type.text() == self.tr('Custom'):
                self.combobox_type.setText(None)
                self.combobox_type.setPlaceholderText(self.tr('Custom'))
        else:
            self.combobox_type.setReadOnly(True)