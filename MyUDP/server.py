from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QUdpSocket, QHostAddress

server = None

@pyqtSlot()
def readData():
  size = server.pendingDatagramSize()
  data, addr, port = server.readDatagram(size)
  print("------ incoming transmission -------")
  print("Data:", data.decode("utf-8"))
  print("Addr:", addr.toString())
  print("Port:", port)
  print("------------------------------------")

if __name__ == "__main__":
  app = QApplication([])
  
  server = QUdpSocket()
  server.readyRead.connect(readData)
  server.bind(QHostAddress().LocalHost, 1234)
  
  app.exec()