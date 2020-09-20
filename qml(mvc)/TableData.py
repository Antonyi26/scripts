# This Python file uses the following encoding: utf-8
#from PyQt5 import QtWidgets

class TableData:

  def __init__(self, rows, columns):
    self.table = [[None for j in range(columns)] for i in range(rows)]

  def rows(self):
    return len(self.table)

  def columns(self):
    if self.rows():
      return len(self.table[0])
    return 0

  def getData(self, row, column):
    return self.table[row][column]

  def setData(self, row, column, d):
    #print(self.table[row][column])
    if self.table[row][column]is None:
      self.table[row][column] = {}
    self.table[row][column].update(d)
    #print(self.table[row][column])
    return True
