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

import sys, os
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import (
  QApplication,
  QWidget,
  QGraphicsScene,
  QGraphicsView,
  QGraphicsItem,
  QHBoxLayout,
  QVBoxLayout
)
from PyQt5.QtQuickWidgets import QQuickWidget
# from PyQt5.QtGui import QGuiApplication, QColor
from PyQt5.QtQml import QQmlApplicationEngine
import MyScene as ms
# from TableModel import *
# from TableData import *

if __name__ == "__main__":
  os.chdir( os.path.dirname(os.path.abspath(__file__)) )

  #QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
  #app = QGuiApplication([])
  app = QApplication([])

#  engine = QQmlApplicationEngine()
#  engine.rootContext().setContextProperty("myModel", model)
#  engine.load("view.qml")

#  if len(engine.rootObjects()) == 0:
#   print("Error. No root objects")
#   sys.exit()

  sceneWidget = ms.MySceneWidget()
  sceneItemsModel = ms.MySceneListModel(sceneWidget.items())
  sceneWidget.itemListChanged.connect(sceneItemsModel.updateModel)


  qmlWidget = QQuickWidget()
  qmlWidget.rootContext().setContextProperty("mySceneWidget", sceneWidget)
  qmlWidget.rootContext().setContextProperty("mySceneModel", sceneItemsModel)
  qmlWidget.setSource(QUrl("view.qml"))
  qmlWidget.setResizeMode(QQuickWidget.SizeRootObjectToView);

  layout = QHBoxLayout()
  layout.addWidget(sceneWidget)
  layout.addWidget(qmlWidget)

  w = QWidget()
  w.setWindowTitle("Hello World !!!")
  w.resize(640, 480)
  w.setLayout(layout)
  w.show()

  app.exec_()
