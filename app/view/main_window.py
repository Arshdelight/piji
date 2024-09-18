# coding: utf-8
# Standard Lib
import os
# Third Party Lib
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QApplication

from qfluentwidgets import NavigationItemPosition, MSFluentWindow, SplashScreen
from qfluentwidgets import FluentIcon as FIF

# Local Lib
## Subinterfaces
from .setting_interface import SettingInterface
from .data_interface import DataInterface
from .ua_interface import UaInterface
from .script_interface import ScriptInterface
## Common
from ..common.config import cfg
from ..common.icon import Icon
from ..common.signal_bus import signalBus
from ..common import resource

class MainWindow(MSFluentWindow):

    def __init__(self,ij):
        super().__init__()
        self.initWindow()

        # ImgDataPath
        self.imgData_path = os.path.abspath('./ImgData')
        # Acquire ij
        self.ij = ij

        from ..core.core import UnitActions, PijiUnits
        # Substantiate uas
        self.uas_json_path = r'app\core\uas.json'
        self.uas = UnitActions().loadpath(self.uas_json_path)
        # Substantiate pus
        self.pus = PijiUnits(self)

        # TODO: create sub interface
        self.settingInterface = SettingInterface(self)
        self.dataInterface = DataInterface(self)
        self.uaInterface = UaInterface(self)
        self.scriptInterface = ScriptInterface(self)

        self.connectSignalToSlot()

        # Add items to navigation interface
        self.initNavigation()

    def connectSignalToSlot(self):
        signalBus.micaEnableChanged.connect(self.setMicaEffectEnabled)

    def initNavigation(self):
        # TODO: Add subinterfaces
        self.addSubInterface(self.dataInterface, FIF.IMAGE_EXPORT, self.tr('Data'))

        self.addSubInterface(self.uaInterface, FIF.APPLICATION, self.tr('Action'))

        self.addSubInterface(self.scriptInterface, FIF.COMMAND_PROMPT, self.tr('Script'))

        # Add subinterfaces to bottom
        self.addSubInterface(
            self.settingInterface, Icon.SETTINGS, self.tr('Settings'), Icon.SETTINGS_FILLED, NavigationItemPosition.BOTTOM)

        # Vanish the splash screen after initiation of navigation
        self.splashScreen.finish()

    def initWindow(self):
        # Basic setup
        self.resize(700, 800)
        # self.setMinimumWidth(760)
        self.setWindowIcon(QIcon(':/app/images/logo.png'))
        self.setWindowTitle('Piji')

        self.setCustomBackgroundColor(QColor(240, 244, 249), QColor(32, 32, 32))
        self.setMicaEffectEnabled(cfg.get(cfg.micaEnabled))

        # Create splash screen
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        # Place at the center of screen 
        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        self.show()
        QApplication.processEvents()

    # def resizeEvent(self, e):
    #     super().resizeEvent(e)
    #     if hasattr(self, 'splashScreen'):
    #         self.splashScreen.resize(self.size())