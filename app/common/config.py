# coding:utf-8
import sys
from enum import Enum

from PySide6.QtCore import QLocale
from qfluentwidgets import (qconfig, QConfig, ConfigItem, OptionsConfigItem, BoolValidator,
                            OptionsValidator, Theme, FolderValidator, ConfigSerializer, ColorConfigItem)

from .setting import CONFIG_FILE # 通过这个设置了本地配置文件的存放地址

class Language(Enum):
    """ Language enumeration """

    CHINESE_SIMPLIFIED = QLocale(QLocale.Chinese, QLocale.China)
    CHINESE_TRADITIONAL = QLocale(QLocale.Chinese, QLocale.HongKong)
    ENGLISH = QLocale(QLocale.English)
    AUTO = QLocale()


class LanguageSerializer(ConfigSerializer):
    """ Language serializer """

    def serialize(self, language):
        return language.value.name() if language != Language.AUTO else "Auto"

    def deserialize(self, value: str):
        return Language(QLocale(value)) if value != "Auto" else Language.AUTO


def isWin11():
    return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000

# 这里可以定义一些默认配置
class Config(QConfig):
    """ Config of application """

    # TODO: ADD YOUR CONFIG GROUP HERE

    # StartWindow
    imagej_memory = ConfigItem("StartWindow","imagej_memory", 8)
    imagej_path = ConfigItem("StartWindow", "imagej_path","D:/Software/Analysis/Fiji", FolderValidator())
    java_path = ConfigItem("StartWindow","java_path", "D:/Software/Programming/jdk22", FolderValidator())


    # MainWindow
    micaEnabled = ConfigItem("MainWindow", "MicaEnabled", isWin11(), BoolValidator())
    dpiScale = OptionsConfigItem(
        "MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]), restart=True)
    language = OptionsConfigItem(
        "MainWindow", "Language", Language.AUTO, OptionsValidator(Language), LanguageSerializer(), restart=True)
    # color = ColorConfigItem("MainWindow", "ThemeColor", "#009faa")

    # SoftwareUpdate
    checkUpdateAtStartUp = ConfigItem("Update", "CheckUpdateAtStartUp", True, BoolValidator())


cfg = Config()
cfg.themeMode.value = Theme.AUTO
# 这里是为了读取本地配置,qconfig是一个实例，这个地址会被赋给cfg.file,如果找不到文件，json就会被设置为空
qconfig.load(str(CONFIG_FILE.absolute()), cfg)