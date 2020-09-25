# This Python file uses the following encoding: utf-8
# from PyQt5 import QtCore
import random
from PyQt5.QtCore import QAbstractListModel, QModelIndex, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem

class MySceneConst:
  ObjectName = 0


#=====================================================


class MySceneListModel(QAbstractListModel):
  def __init__(self, itemList):
    QAbstractListModel.__init__(self)
    self.itemList = itemList

  def rowCount(self, index=QModelIndex()):
    return len(self.itemList)

  def data(self, index, role=Qt.DisplayRole):
    i = index.row()
    if i < 0 or i >= self.rowCount():
      return None
    return self.itemList[i].data(MySceneConst.ObjectName)

  def setData(self, index, value, role=Qt.DisplayRole):
    i = index.row()
    self.itemList[i] = value
    return True

  def insertRows(self, row, count, parentInd=QModelIndex()):
    self.beginInsertRows(parentInd, row, row + count - 1)
    for i in range(count):
      self.itemList.append(None)
    self.endInsertRows()
    return True

  def roleNames(self):
    d = {
      Qt.DisplayRole: "display".encode("utf-8")
    }
    return d

  @pyqtSlot(list)
  def updateModel(self, itemList):
    itemList.reverse()
    self.itemList = itemList
    self.modelReset.emit()


#=====================================================


class MySceneWidget(QGraphicsView):

  itemListChanged = pyqtSignal(list)

  def __init__(self):
    QGraphicsView.__init__(self)
    self.setScene(QGraphicsScene())

  @pyqtSlot(str)
  def addItem(self, itemName):
    item = None

    if itemName == "Rectangle":
      item = self.scene().addRect(0, 0, 100, 100)
    elif itemName == "Circle":
      item = self.scene().addEllipse(0, 0, 100, 100)
    else:
      return

    flags = QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable
    item.setFlag(int(flags))
    ind = len(self.items())
    item.setData(MySceneConst.ObjectName, f"{ind}. {itemName}")
    self.itemListChanged.emit(self.items())

