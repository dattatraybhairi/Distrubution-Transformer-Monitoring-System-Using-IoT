import sys

from PyQt5 import QtCore


def update():
    print("hey")


if __name__ == "__main__":

    app = QtCore.QCoreApplication(sys.argv)

    fps = 15
    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.setInterval(1000 / fps)
    timer.start()

    app.exec_()