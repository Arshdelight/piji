import string, json, re, os
from glob import glob
from ..view.main_window import MainWindow
from ..view.little_widgets import ParaMessageBox

class PijiUnits:
    def __init__(self, parent: MainWindow = None):
        self.list = []
        self.uas = None
        self.history = []
        self.actions = []
        if parent != None:
            self.parent = parent
            self.imgData_path = parent.imgData_path
            self.ij = parent.ij
            self.uas = parent.uas
            # self.pus = parent.pus
    
    def add(self,pu:'PijiUnit'):
        self.list.append(pu)

    def setupuas(self, uas:'UnitAction'):
        self.uas = uas
        self.getuas()

    def getuas(self):
        if self.uas:
            if isinstance(self.uas, UnitActions):
                for ua in self.uas:
                    def dynamic_func(self, ua=ua, **_paras):
                        func_name, paras = ua(mainwindow = self.parent, **_paras)
                        exec(ua.code)
                        history = {
                            'func_name': func_name,
                            'paras': paras
                        }
                        return history
                    setattr(self, ua.func_name, dynamic_func.__get__(self))
                return True
        return False
    
    def getua(self, func_name:str):
        for ua in self.uas:
            if ua.func_name == func_name:
                def dynamic_func(self, ua=ua, **_paras):
                        func_name, paras = ua(mainwindow = self.parent, **_paras)
                        exec(ua.code)
                        history = {
                            'func_name': func_name,
                            'paras': paras
                        }
                        return history
                setattr(self, ua.func_name, dynamic_func.__get__(self))
                return True
        return False
    
    def CreateQueue(self, parent):
        # parent是DataInterface
        self.images = parent.shadow_images
        self.image_names = parent.shadow_image_names
        self.rois_zips = parent.shadow_rois_zips
        self.rois_zip_names = parent.shadow_rois_zip_names
        self.list.clear()
        self.AutoAdd()
        self.AutoInit()

    def LoadQueue(self, dir):
        self.list.clear()
        # 遍历子目录
        for subdir in os.listdir(dir):
            subdir_path = os.path.join(dir, subdir)
            # 读取子目录名称
            image_name = subdir
            # 查找子目录中与子目录名称相同的图片
            image = None
            for ext in ['*.png', '*.jpg', '*.jpeg', '*.tiff', '*.tif']:  # 假设图片后缀为这些
                matches = glob(os.path.join(subdir_path, f'{image_name}{ext}'))
                if matches:
                    image = matches[0]  # 假设只有一个符合条件的图片
                    break
            if not image:
                continue  # 如果没有找到对应图片，跳过该子目录

            # 查找与子目录名称匹配的zip文件
            expected_rois_zip_name = image_name + '_rois'
            rois_zip = os.path.join(subdir_path, expected_rois_zip_name+'.zip')

             # 检查 zip 文件是否存在
            if os.path.exists(rois_zip):
                # 添加到 list
                self.AddUnit(image, image_name, rois_zip)
            else:
                self.AddUnit(image, image_name)

            # 查找所有zip文件 赋值路径给self.文件名
            zip_files = glob(os.path.join(subdir_path, '*rois.zip'))
            
            for zip_file in zip_files:
                filename = os.path.splitext(os.path.basename(zip_file))[0]
                setattr(self.list[-1], filename+'_zip', zip_file.replace('\\','/'))

            # 查找所有前缀为 "parabus" 的 txt 文件
            txt_files = glob(os.path.join(subdir_path, 'parabus*.txt'))
            # 按时间戳排序，确保顺序正确
            txt_files.sort()

            for txt in txt_files:
                with open(txt, 'r', encoding='utf-8') as file:  # 确保使用 UTF-8 编码
                    try:
                        content = file.read()
                        parabus = json.loads(content)
                    except json.JSONDecodeError as e:
                        # print(f"JSON 解析错误: {e}，文件名: {txt}")
                        continue  # 跳过这个文件，继续处理下一个文件s
                    
                    # 将解析后的 JSON 数据赋值到对象属性中
                    for key, value in parabus.items():
                        setattr(self.list[-1], key, value)  

            # 查找目录中所有其它图片的路径和名称
            # 查找目录中所有其它图片的路径和名称
            other_images = []
            for ext in ['*.png', '*.jpg', '*.jpeg', '*.tiff', '*.tif']:
                other_images.extend(glob(os.path.join(subdir_path, ext)))

            # 去掉与主图片相同的图片
            other_images = [img for img in other_images if img != image]

            # 将每个其它图片的路径和名称赋值到最后一个新加的 pu unit
            for other_image_path in other_images:
                other_image_name = other_image_name = os.path.splitext(os.path.basename(other_image_path))[0]
                # 将图片名称和路径作为属性添加到最后一个 pu unit
                setattr(self.list[-1], other_image_name, other_image_path)
                # print(f'Setting other image: {other_image_name} = {other_image_path}') # 测试用
        self.AutoInit()     
    
    def AutoAdd(self):
        for image_index, image_name in enumerate(self.image_names):
            # rois_name要符合命名规则
            expected_rois_zip_name = image_name + '_rois'
            if expected_rois_zip_name in self.rois_zip_names:
                rois_index = self.rois_zip_names.index(expected_rois_zip_name)
                rois_zip = self.rois_zips[rois_index]
            else:
                rois_zip = None
            self.AddUnit(self.images[image_index], image_name, rois_zip)

    def AutoInit(self):
        for pu in self.list:
            try:
                flag = getattr(pu,'initflag')
                if flag == 'True':
                    continue
                else:
                    pu.imginfoinit()
            except:
                pu.imginfoinit()

    def AutoSet(self):
        for pu in self.list:
            pu.getuas()

    def AddUnit(self, image, name, rois_zip=None):
        pu = PijiUnit(self.parent, image, name, rois_zip)
        self.list.append(pu)

    def AddHistory(self, history):
        self.history.append(history)
    
class PijiUnit(PijiUnits):
    def __init__(self, parent: MainWindow, image, name ,rois_zip):
        super().__init__(parent=parent)

        self.pus = parent.pus
        self.image = image
        self.name = name
        self.rois_zip = rois_zip
        # 根据图像路径找根目录
        self.root = os.path.dirname(image).replace('\\','/')
        self.list.append(self)
        # PijiUnit要继承自MainWindow
        if self.uas:
            self.getuas()

class PartialFormatter(string.Formatter):
    def get_value(self, key, args, kwargs):
        if isinstance(key, str):
            return kwargs.get(key, '{' + key + '}')
        else:
            return string.Formatter.get_value(self, key, args, kwargs)
        
class UnitActions(list):
    def __init__(self):
        self.json = {}
        self.origin_json = {}
    
    def add(self, ua:'UnitAction'):
        if ua.func_name in self.json.keys():
            return False
        else:
            self.append(ua)
            self.json[ua.func_name] = ua.to_json()
            return True
    
    def addjson(self, dict):
        ua = UnitAction(**dict)
        self.add(ua)

    def modify(self, dict):
        func_name = dict['func_name']
        for ua in self:
            if ua.func_name == func_name:
                # 更新ua
                ua.modify(dict)
                # 更新uas json
                self.json[func_name] = dict
                return True
        return False

    def remove(self, func_name):
        if func_name in self.json:
            for idx, ua in enumerate(self):
                if func_name == ua.func_name:
                    self.pop(idx)
            self.json.pop(func_name)
            return True
        return False

    def loadjson(self, _json):
        for key, value in _json.items():
            try:
                # 必须要有func_name
                func_name = value['func_name']
            except:
                continue
            code = f"{func_name} = UnitAction(**_json[key])\nself.add({func_name})"
            exec(code)
                
        self.origin_json = self.json.copy()
        return self
    
    def loadpath(self, path):
        with open(path, 'r') as file:
            try:
                _json = json.load(file)
            except:
                _json = {}

        self.loadjson(_json)
        return self
    
    def getchange(self):
        changes = {
                'added':[],
                'removed':[],
                'modified':[]
            }
        for key, value in self.json.items():
            if key not in self.origin_json.keys():
                changes['added'].append(value['alias'])
            elif value != self.origin_json[key]:
                changes['modified'].append(value['alias'])
        for key, value in self.origin_json.items():
            if key not in self.json.keys():
                changes['removed'].append(value['alias'])      
        return changes

    
    def save(self, path):
        try:
            with open(path, 'w') as file:
                json.dump(self.json, file, indent=4)
            self.origin_json = self.json.copy()
            return True
        except:
            return False

class UnitAction:
    def __init__(self, **dict):
        self.func_name = dict['func_name'] # func_name以字典里的为准
        self.alias = dict['alias']
        self.code_template = dict['code_template'] # code_template是绝对不被修改的，和json中一致
        self.type = dict['type']
        self.paras = []
        self.paras_aliasdict = {}
        self.getparas()

        self.formatter = PartialFormatter()

    def getparas(self):
        self.paras.clear()
        code_template = self.code_template
        # 先替换双花括号，防止被错误处理
        protected_template = code_template.replace('{{', '@piji_left_placeholder@').replace('}}', '@piji_right_placeholder@')
        # 使用正则表达式找到所有单花括号中的内容
        raw_paras = re.findall(r'\{([^{}]+)\}', protected_template)

        # 处理每一个匹配项，检查是否包含冒号，分割键和别名
        for item in raw_paras:
            if ':' in item:
                key, alias = item.split(':', 1)  # 仅分割第一个冒号
                self.paras.append(key.strip())
                self.paras_aliasdict[key.strip()] = alias.strip()
                # 替换原模板中的带别名参数为无别名参数
                protected_template = protected_template.replace('{' + item + '}', '{' + key.strip() + '}')
            else:
                self.paras.append(item)
                self.paras_aliasdict[item] = ''
        # 将双花括号占位符替换回去
        self.code_misspara = protected_template.replace('@piji_left_placeholder@', '{{').replace('@piji_right_placeholder@', '}}')

    def modify(self, dict):
        self.func_name = dict['func_name'] # func_name以字典里的为准
        self.alias = dict['alias']
        self.code_template = dict['code_template']
        self.type = dict['type']
        self.getparas()

    def to_json(self):
        # to_json可以实现配置文件的自动更新
        return {
            'func_name': self.func_name,
            'alias': self.alias,
            'type' : self.type,
            'code_template': self.code_template,
        }
    
    def __call__(self, mainwindow, **paras):
        # 去除多余参数，感觉这个会有bug啊
        excess_paras = [para for para in paras if para not in self.paras]
        for para in excess_paras:
            paras.pop(para)
        while 1:
            # 检查缺少哪些paras
            missing_paras = [para for para in self.paras if para not in paras]
            # 变成集合
            missing_paras = list(set(missing_paras))
            if len(missing_paras) == 0:
                break
            w = ParaMessageBox(mainwindow)
            for para in missing_paras:
                w.askpara(para, self.paras_aliasdict[para])
            w.show
            if w.exec():
                for para in missing_paras:
                    text = getattr(w, para+'_lineedit').text()
                    if text:
                        paras[para] = text
            
        self.code = self.formatter.format(self.code_misspara, **paras)
        return self.func_name, paras

if __name__ == '__main__':
    # 以下代码是测试用的
    # init_json = {
    #     'funcname1':{
    #         'func_name': 'funcname1',
    #         'alias': '一号',
    #         'code_template': 'print(\'{greet},{name}\')',
    #         'paras': ['greet', 'name']
    #     },
    #     'funcname2':{
    #         'func_name': 'funcname2',
    #         'alias': '二号',
    #         'code_template': 'print(\'{a} and {b} and {c}\')',
    #         'paras': ['a', 'b'],
    #     }
    # }
    
    path = r'D:\BaiduSyncdisk\Programming\piji4\app\core\unit_action.json'

    # with open(path, 'w') as file:
    #     json.dump(init_json, file, indent=4)

    uas = UnitActions()
    uas.loadpath(path)

    ua_json = {
        'func_name': 'funcname3',
        'alias': '二号',
        'code_template': 'print(\'{aa} and {bb} and \'+ self.cc)',
        'paras': ['a', 'bb'],
    }
    ua = UnitAction(**ua_json)
    uas.add(ua)

    print(uas.json)

    uas.save(path)


    pu = PijiUnit()
    # pu.aa = '我是AA'
    # pu.cc = '我是CC'
    pu.setupuas(uas)

    # pu.funcname3()