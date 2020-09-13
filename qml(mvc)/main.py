# from PyQt5.QtCore import QCoreApplication, Qt, QUrl
# from PyQt5.QtGui import QGuiApplication
# from PyQt5.QtQuick import QQuickView
# #from PyQt5.QtQml import QQmlEngine


# QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
# QCoreApplication.setOrganizationName("...")

# app = QGuiApplication([])

# view = QQuickView()
# view.engine().quit.connect(QCoreApplication.quit)
# view.setSource(QUrl("view.qml"))
# if view.status() == QQuickView.Error:
#   exit(-1)
# view.setResizeMode(QQuickView.SizeRootObjectToView)
# view.show()

# app.exec_()

#################################################

from sys import exit
from PyQt5.QtCore import Qt, QAbstractListModel, QModelIndex
# from PyQt5.QtGui import QGuiApplication
# from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication, QWidget, QListView, QVBoxLayout, QComboBox

# QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
# app = QGuiApplication([])
app = QApplication([])

Roles = {
  # "text": 256,
  "text": Qt.DisplayRole,
  "color": 257,
  "borderRadius": 258
}

class MyStringListModel(QAbstractListModel):
  def __init__(self, data=[], parent=None):
    QAbstractListModel.__init__(self, parent)
    self.__data = data
    
  def rowCount(self, modelIndex=QModelIndex()):
    return len(self.__data)
  
  def columnCount(self, modelIndex=QModelIndex()):
    return 1
  
  def setData(self, modelIndex, value, role=Qt.DisplayRole):
    row = modelIndex.row()
    if row > len(self.__data) or row < 0:
      return False
    if row == len(self.__data):
      self.__data.append({})

    if isinstance(value, str):
      self.__data[row]["text"] = value
    else:
      self.__data[row] = value
      
    print(self.__data)
    return True

  
  def data(self, modelIndex, role=Qt.DisplayRole):
    value = None
    d = self.roleNames()
    try:
      row = modelIndex.row()
      value = self.__data[row][d[role]]
    finally:
      return value
  
  def flags(self, modelIndex):
    return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled
    
  def roleNames(self):
    d = {v: k for k, v in Roles.items()}
    return d
  
  def setList(self, lst):
    self.__data.clear()
    for i, obj in enumerate(lst):
      modelIndex = self.createIndex(i, 0)
      self.setData(modelIndex, obj)


    # for i, obj in enumerate(lst):
    #   modelIndex = self.createIndex(i, 0)
    #   for j in list(obj.keys()):
    #     self.setData(modelIndex, obj[j], Roles[j])


lst = [
  {"text": "one", "color": "tomato", "borderRadius": 20},
  {"text": "two", "color": "lightblue", "borderRadius": 8}
]

model = MyStringListModel()
model.setList(lst)

# engine = QQmlApplicationEngine()
# engine.rootContext().setContextProperty("myModel", model)
# engine.load("view.qml")
# if len(engine.rootObjects()) == 0:
#   print("Error. No root objects")
#   exit()

w = QWidget()
w.setWindowTitle("Hello World !!!")
w.resize(320, 240)

view = QListView()
view.setModel(model)

comboBox = QComboBox()
comboBox.setModel(model)

layout = QVBoxLayout()
layout.addWidget(comboBox)
layout.addWidget(view)

w.setLayout(layout)

w.show()

app.exec()
