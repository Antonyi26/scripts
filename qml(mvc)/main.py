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
from PyQt5.QtGui import QGuiApplication, QColor
from PyQt5.QtQml import QQmlApplicationEngine

QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

app = QGuiApplication([])

# class obj:
#   def __init__(self, color, text):
#     self.color = QColor(color)
#     self.text = text

# lst = [
#   obj("red", "one"),
#   obj("green", "two"),
#   obj("lightblue", "three")
# ]

# model.setStringList(lst)

Roles = {
  "text": 256,
  "color": 257
}


defaultElement = {
  Roles["text"]: "undefined",
  Roles["color"]: "gray"
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
    while row >= len(self.__data): 
      self.__data.append(defaultElement.copy())
    self.__data[row][role] = value
  
  def data(self, modelIndex, role=Qt.DisplayRole):
    value = None
    try:
      row = modelIndex.row()
      value = self.__data[row][role]
    finally:
      return value

  def flags(self, modelIndex):
    return Qt.ItemIsSelectable
    
  def roleNames(self):
    d = {}
    for i in Roles.keys():
      d[Roles[i]] = i.encode('utf-8')
    return d
  
  # def index(self, row, column, modelIndex=QModelIndex()):
  #   pass
  
  # def parent(self, modelIndex):
  #   return QModelIndex()

model = MyStringListModel()
modelIndex = model.createIndex(0, 0)
model.setData(modelIndex, "one", Roles["text"])
model.setData(modelIndex, "tomato", Roles["color"])
modelIndex = model.createIndex(2, 0)
model.setData(modelIndex, "two", Roles["text"])
model.setData(modelIndex, "lightblue", Roles["color"])

engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty("myModel", model)
engine.load("view.qml")
if len(engine.rootObjects()) == 0:
  print("Error. No root objects")
  exit()

app.exec()

#################################################

# from PyQt5.QtCore import QApplication
# from PyQt5.QtWidgets import QWidget, QListView, QVBoxLayout, QComboBox
# from PyQt5.QtCore import QStringListModel

# app = QApplication([])

# w = QWidget()
# w.setWindowTitle("Hello World !!!")
# w.resize(320, 240)

# model = QStringListModel()
# strings = ["one", "two", "three"]
# model.setStringList(strings)

# view = QListView()
# view.setModel(model)

# comboBox = QComboBox()
# comboBox.setModel(model)

# layout = QVBoxLayout()
# layout.addWidget(comboBox)
# layout.addWidget(view)

# w.setLayout(layout)

# w.show()

# app.exec_()

#################################################
