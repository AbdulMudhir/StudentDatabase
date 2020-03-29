from PyQt5 import QtCore



class StudentFinderThread(QtCore.QThread):
    new_signal = QtCore.pyqtSignal(int, int, str)

    def __init__(self, function, student_id):
        QtCore.QThread.__init__(self)
        self.function = function
        self.student_id = student_id

    def run(self):
        print(self.function(self.student_id))
        self.quit()

