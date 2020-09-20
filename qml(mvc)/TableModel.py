# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
#import TableData as td


Text2Role = {
  "display": Qt.DisplayRole,
  "edit": Qt.EditRole,
  "bgColor": Qt.BackgroundRole,
  "textColor": Qt.UserRole
}

Role2Text = {v: k.encode("utf-8") for k,v in Text2Role.items()}


class TableModel(QAbstractTableModel):

  def __init__(self, table):
    QAbstractTableModel.__init__(self)
    self.table = table

  def rowCount(self, index=QModelIndex()):
    return self.table.rows()

  def columnCount(self, index=QModelIndex()):
    return self.table.columns()

  def setData(self, index, value, role=Qt.DisplayRole):
    i = index.row()
    j = index.column()
    d = {role: value}
    return self.table.setData(i, j, d)

  def data(self, index, role=Qt.DisplayRole):
    i = index.row()
    j = index.column()
    try:
      return self.table.getData(i, j)[role]
    except KeyError:
      return None

  def roleNames(self):
    return Role2Text

  def flags(self, index=QModelIndex()):
    return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

  def headerData(self, section, orientation, role=Qt.DisplayRole):
    pass
