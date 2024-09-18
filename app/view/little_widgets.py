from PySide6.QtCore import Slot
from qfluentwidgets import MessageBoxBase, SubtitleLabel, LineEdit, TeachingTip, InfoBarIcon, TeachingTipTailPosition, MessageBox

import keyword
    
def show_teaching_tip(self,_target:object,_icon_type:int,_content:str):
    # ERROR INFORMATION SUCCESS WARNING
    _icon = None
    _title = None
    if _icon_type == 1:
        _icon = InfoBarIcon.ERROR
        _title = self.tr('Error')
    elif _icon_type == 2:
        _icon = InfoBarIcon.INFORMATION
        _title = self.tr('Info')
    elif _icon_type == 3:
        _icon = InfoBarIcon.SUCCESS
        _title = self.tr('Success')
    elif _icon_type == 4:
        _icon = InfoBarIcon.WARNING
        _title = self.tr('Warning')

    TeachingTip.create(
            target=_target,
            icon=_icon,
            title=_title,
            content=_content,
            isClosable=True,
            tailPosition=TeachingTipTailPosition.BOTTOM,
            duration=1000,
            parent=self
        )
    
class ParaMessageBox(MessageBoxBase):
    """ Custom message box """
    def __init__(self, parent=None):
        super().__init__(parent)
        # change the text of button
        self.yesButton.setText(self.tr('Confirm'))
        self.cancelButton.setText(self.tr('Cancel'))
        self.widget.setMinimumWidth(350)

    def askpara(self, paraname:str, paraalias:str = None):
        label = SubtitleLabel(paraname+': ', self)
        lineedit = LineEdit(self)
        lineedit.setPlaceholderText(paraalias)
        setattr(self, paraname+'_label', label)
        setattr(self, paraname+'_lineedit', lineedit)

        self.viewLayout.addWidget(label)
        self.viewLayout.addWidget(lineedit)