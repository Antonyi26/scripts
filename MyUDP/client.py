from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QUdpSocket, QHostAddress

client = None

if __name__ == "__main__":
  app = QApplication([])
  
  client = QUdpSocket()
  while True:
    print()
    data = input("data: ")
    data = data.encode("utf-8")
    client.writeDatagram(data, QHostAddress.LocalHost, 1234)
  
  app.exec()