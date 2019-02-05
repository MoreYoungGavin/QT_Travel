import sys
import threading
import time

from PyQt5.QtWidgets import QApplication, QDialog

from untitledTPBCM import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
class MyThread(threading.Thread):
    counter = 0
    def __init__(self,w,ProgressBar):
        threading.Thread.__init__(self)
        self.w = w
        self.counter = 0
        self.progreassBar = ProgressBar
    def run(self):
        print("Starting "+ self.name + "\n")
        with threadLock:
            while self.counter <= 100:
                time.sleep(1)
                self.progreassBar.setValue(self.counter)
                self.counter += 10
        print("Exiting " + self.name + "\n")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    thread1 = MyThread(w,w.ui.progressBar)
    thread2 = MyThread(w,w.ui.progressBar_2)
    threadLock = threading.Lock()
    threads = []
    thread1.start()
    thread2.start()
    w.exec()
    threads.append(thread1)
    threads.append(thread2)
    for t in threads:
        t.join()
    sys.exit(app.exec_())