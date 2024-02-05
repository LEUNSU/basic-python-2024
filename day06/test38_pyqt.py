# file : test36_pyqt.py
# desc : Qt 디자이너 만든 ui와 연동

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget): 
    def __init__(self) -> None:
        super().__init__() 
        uic.loadUi('./day06/TestApp.ui',self) # QtDesigner에서 만든 ui를 로드
        # 버튼에 대한 시그널처리
        self. btnStart.clicked.connect(self.btnStartClicked)
        self. btnStop.clicked.connect(self.btnStopClicked) # ui파일 내에 있는 위젯 접근은 VSCode상에서 색상으로 표시X

    def btnStartClicked(self):
        print('시작버튼 클릭')
        self.lblStatus.setText('상태 : 동작시작')
        QMessageBox.about(self, '동작', '***시스템이 시작되었습니다')

    def btnStopClicked(self):
        print('종료버튼 클릭')
        self.lblStatus.setText('상태 : 동작중지')
        QMessageBox.about(self, '동작', '***시스템이 종료되었습니다')

    def closeEvent(self, QCloseEvent) -> None: # X버튼 종료 확인
            re = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
            if re == QMessageBox.Yes: # 닫기
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore() 

if __name__ == '__main__':
    loop = QApplication(sys.argv) 
    instance = qtwin_exam()
    instance.show()
    loop.exec_()