# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentdatabasement.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import QMessageBox
from studentsql import StudentDatabase
from database_thread import StudentFinderThread
from threading import Thread


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.student_database = StudentDatabase("student_database.db")
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMaximumHeight(1100)
        MainWindow.setMaximumWidth(1500)
        MainWindow.resize(1000, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1533, 1139))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background:white")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.student_database_management_system = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.student_database_management_system.setFont(font)
        self.student_database_management_system.setStyleSheet("background-color:orange;\n"
                                                              "border-style: outset;\n"
                                                              "border-width: 1px;\n"
                                                              "border-radius: 5px;\n"
                                                              "border-color: black;\n"
                                                              "padding: 4px;")
        self.student_database_management_system.setScaledContents(True)
        self.student_database_management_system.setAlignment(QtCore.Qt.AlignCenter)
        self.student_database_management_system.setObjectName("student_database_management_system")
        self.gridLayout_5.addWidget(self.student_database_management_system, 0, 0, 1, 1)
        self.database_input_frames = QtWidgets.QFrame(self.frame)
        self.database_input_frames.setStyleSheet("background-color:orange;\n"
                                                 "border-style: outset;\n"
                                                 "border-width: 1px;\n"
                                                 "border-radius: 5px;\n"
                                                 "border-color: black;\n"
                                                 "padding: 4px;")
        self.database_input_frames.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.database_input_frames.setFrameShadow(QtWidgets.QFrame.Raised)
        self.database_input_frames.setObjectName("database_input_frames")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.database_input_frames)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.student_info_frame = QtWidgets.QFrame(self.database_input_frames)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student_info_frame.sizePolicy().hasHeightForWidth())
        self.student_info_frame.setSizePolicy(sizePolicy)
        self.student_info_frame.setStyleSheet("background-color:orange;\n"
                                              "border-style: outset;\n"
                                              "border-width: 1px;\n"
                                              "border-radius: 5px;\n"
                                              "border-color: black;\n"
                                              "padding: 4px;")
        self.student_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_info_frame.setObjectName("student_info_frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.student_info_frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.student_id_label = QtWidgets.QLabel(self.student_info_frame)
        self.student_id_label.setStyleSheet("background-color:orange;\n"
                                            "border-style: outset;\n"
                                            "border-width: 0px;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: black;\n"
                                            "padding: 4px;")
        self.student_id_label.setObjectName("student_id_label")
        self.gridLayout_7.addWidget(self.student_id_label, 0, 0, 1, 1)
        self.student_id_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.student_id_input.setStyleSheet("background:white;\n"
                                            "border-style: outset;\n"
                                            "border-width: 1px;\n"
                                            "border-radius: 0px;\n"
                                            "border-color: black;\n"
                                            "padding: 1px;")
        self.student_id_input.setObjectName("student_id_input")
        self.gridLayout_7.addWidget(self.student_id_input, 0, 1, 1, 1)
        self.firstname_label = QtWidgets.QLabel(self.student_info_frame)
        self.firstname_label.setStyleSheet("background-color:orange;\n"
                                           "border-style: outset;\n"
                                           "border-width: 0px;\n"
                                           "border-radius: 5px;\n"
                                           "border-color: black;\n"
                                           "padding: 4px;")
        self.firstname_label.setObjectName("firstname_label")
        self.gridLayout_7.addWidget(self.firstname_label, 1, 0, 1, 1)
        self.firstname_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.firstname_input.setStyleSheet("background:white;\n"
                                           "border-style: outset;\n"
                                           "border-width: 1px;\n"
                                           "border-radius: 0px;\n"
                                           "border-color: black;\n"
                                           "padding: 1px;")
        self.firstname_input.setObjectName("firstname_input")
        self.gridLayout_7.addWidget(self.firstname_input, 1, 1, 1, 1)
        self.surname_label = QtWidgets.QLabel(self.student_info_frame)
        self.surname_label.setStyleSheet("background-color:orange;\n"
                                         "border-style: outset;\n"
                                         "border-width: 0px;\n"
                                         "border-radius: 5px;\n"
                                         "border-color: black;\n"
                                         "padding: 4px;")
        self.surname_label.setObjectName("surname_label")
        self.gridLayout_7.addWidget(self.surname_label, 2, 0, 1, 1)
        self.surname_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.surname_input.setStyleSheet("background:white;\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 0px;\n"
                                         "border-color: black;\n"
                                         "padding: 1px;")
        self.surname_input.setObjectName("surname_input")
        self.gridLayout_7.addWidget(self.surname_input, 2, 1, 1, 1)
        self.gender_label = QtWidgets.QLabel(self.student_info_frame)
        self.gender_label.setStyleSheet("background-color:orange;\n"
                                        "border-style: outset;\n"
                                        "border-width: 0px;\n"
                                        "border-radius: 5px;\n"
                                        "border-color: black;\n"
                                        "padding: 4px;")
        self.gender_label.setObjectName("gender_label")
        self.gridLayout_7.addWidget(self.gender_label, 3, 0, 1, 1)
        self.gender_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.gender_input.setStyleSheet("background:white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 0px;\n"
                                        "border-color: black;\n"
                                        "padding: 1px;")
        self.gender_input.setObjectName("gender_input")
        self.gridLayout_7.addWidget(self.gender_input, 3, 1, 1, 1)
        self.age_label = QtWidgets.QLabel(self.student_info_frame)
        self.age_label.setStyleSheet("background-color:orange;\n"
                                     "border-style: outset;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 5px;\n"
                                     "border-color: black;\n"
                                     "padding: 4px;")
        self.age_label.setObjectName("age_label")
        self.gridLayout_7.addWidget(self.age_label, 4, 0, 1, 1)
        self.age__input = QtWidgets.QLineEdit(self.student_info_frame)
        self.age__input.setStyleSheet("background:white;\n"
                                      "border-style: outset;\n"
                                      "border-width: 1px;\n"
                                      "border-radius: 0px;\n"
                                      "border-color: black;\n"
                                      "padding: 1px;")
        self.age__input.setObjectName("age__input")
        self.gridLayout_7.addWidget(self.age__input, 4, 1, 1, 1)
        self.address_label = QtWidgets.QLabel(self.student_info_frame)
        self.address_label.setStyleSheet("background-color:orange;\n"
                                         "border-style: outset;\n"
                                         "border-width: 0px;\n"
                                         "border-radius: 5px;\n"
                                         "border-color: black;\n"
                                         "padding: 4px;")
        self.address_label.setObjectName("address_label")
        self.gridLayout_7.addWidget(self.address_label, 5, 0, 1, 1)
        self.address_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.address_input.setStyleSheet("background:white;\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 0px;\n"
                                         "border-color: black;\n"
                                         "padding: 1px;")
        self.address_input.setObjectName("address_input")
        self.gridLayout_7.addWidget(self.address_input, 5, 1, 1, 1)
        self.postcode_label = QtWidgets.QLabel(self.student_info_frame)
        self.postcode_label.setStyleSheet("background-color:orange;\n"
                                          "border-style: outset;\n"
                                          "border-width: 0px;\n"
                                          "border-radius: 5px;\n"
                                          "border-color: black;\n"
                                          "padding: 4px;")
        self.postcode_label.setObjectName("postcode_label")
        self.gridLayout_7.addWidget(self.postcode_label, 6, 0, 1, 1)
        self.postcode_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.postcode_input.setStyleSheet("background:white;\n"
                                          "border-style: outset;\n"
                                          "border-width: 1px;\n"
                                          "border-radius: 0px;\n"
                                          "border-color: black;\n"
                                          "padding: 1px;")
        self.postcode_input.setObjectName("postcode_input")
        self.gridLayout_7.addWidget(self.postcode_input, 6, 1, 1, 1)
        self.mobile_label = QtWidgets.QLabel(self.student_info_frame)
        self.mobile_label.setStyleSheet("background-color:orange;\n"
                                        "border-style: outset;\n"
                                        "border-width: 0px;\n"
                                        "border-radius: 5px;\n"
                                        "border-color: black;\n"
                                        "padding: 4px;")
        self.mobile_label.setObjectName("mobile_label")
        self.gridLayout_7.addWidget(self.mobile_label, 7, 0, 1, 1)
        self.mobile_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.mobile_input.setStyleSheet("background:white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 0px;\n"
                                        "border-color: black;\n"
                                        "padding: 1px;")
        self.mobile_input.setObjectName("mobile_input")
        self.gridLayout_7.addWidget(self.mobile_input, 7, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.student_info_frame)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.subjects_frame = QtWidgets.QFrame(self.database_input_frames)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subjects_frame.sizePolicy().hasHeightForWidth())
        self.subjects_frame.setSizePolicy(sizePolicy)
        self.subjects_frame.setStyleSheet("background:orange")
        self.subjects_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.subjects_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.subjects_frame.setObjectName("subjects_frame")
        self.formLayout_3 = QtWidgets.QFormLayout(self.subjects_frame)
        self.formLayout_3.setObjectName("formLayout_3")
        self.chemistry_label = QtWidgets.QLabel(self.subjects_frame)
        self.chemistry_label.setStyleSheet("background-color:orange;\n"
                                           "border-style: outset;\n"
                                           "border-width: 0px;\n"
                                           "border-radius: 5px;\n"
                                           "border-color: black;\n"
                                           "padding: 4px;")
        self.chemistry_label.setObjectName("chemistry_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.chemistry_label)
        self.chemistry_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.chemistry_input.setStyleSheet("background:white;\n"
                                           "border-style: outset;\n"
                                           "border-width: 1px;\n"
                                           "border-radius: 0px;\n"
                                           "border-color: black;\n"
                                           "padding: 1px;")
        self.chemistry_input.setObjectName("chemistry_input")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chemistry_input)
        self.computing_label = QtWidgets.QLabel(self.subjects_frame)
        self.computing_label.setStyleSheet("background-color:orange;\n"
                                           "border-style: outset;\n"
                                           "border-width: 0px;\n"
                                           "border-radius: 5px;\n"
                                           "border-color: black;\n"
                                           "padding: 4px;")
        self.computing_label.setObjectName("computing_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.computing_label)
        self.computing_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.computing_input.setStyleSheet("background:white;\n"
                                           "border-style: outset;\n"
                                           "border-width: 1px;\n"
                                           "border-radius: 0px;\n"
                                           "border-color: black;\n"
                                           "padding: 1px;")
        self.computing_input.setObjectName("computing_input")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.computing_input)
        self.english_label = QtWidgets.QLabel(self.subjects_frame)
        self.english_label.setStyleSheet("background-color:orange;\n"
                                         "border-style: outset;\n"
                                         "border-width: 0px;\n"
                                         "border-radius: 5px;\n"
                                         "border-color: black;\n"
                                         "padding: 4px;")
        self.english_label.setObjectName("english_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.english_label)
        self.english_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.english_input.setStyleSheet("background:white;\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 0px;\n"
                                         "border-color: black;\n"
                                         "padding: 1px;")
        self.english_input.setObjectName("english_input")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.english_input)
        self.physics_label = QtWidgets.QLabel(self.subjects_frame)
        self.physics_label.setStyleSheet("background-color:orange;\n"
                                         "border-style: outset;\n"
                                         "border-width: 0px;\n"
                                         "border-radius: 5px;\n"
                                         "border-color: black;\n"
                                         "padding: 4px;")
        self.physics_label.setObjectName("physics_label")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.physics_label)
        self.physics_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.physics_input.setStyleSheet("background:white;\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 0px;\n"
                                         "border-color: black;\n"
                                         "padding: 1px;")
        self.physics_input.setObjectName("physics_input")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.physics_input)
        self.biology_label = QtWidgets.QLabel(self.subjects_frame)
        self.biology_label.setStyleSheet("background-color:orange;\n"
                                         "border-style: outset;\n"
                                         "border-width: 0px;\n"
                                         "border-radius: 5px;\n"
                                         "border-color: black;\n"
                                         "padding: 4px;")
        self.biology_label.setObjectName("biology_label")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.biology_label)
        self.biology_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.biology_input.setStyleSheet("background:white;\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 0px;\n"
                                         "border-color: black;\n"
                                         "padding: 1px;")
        self.biology_input.setObjectName("biology_input")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.biology_input)
        self.business_label = QtWidgets.QLabel(self.subjects_frame)
        self.business_label.setStyleSheet("background-color:orange;\n"
                                          "border-style: outset;\n"
                                          "border-width: 0px;\n"
                                          "border-radius: 5px;\n"
                                          "border-color: black;\n"
                                          "padding: 4px;")
        self.business_label.setObjectName("business_label")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.business_label)
        self.business_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.business_input.setStyleSheet("background:white;\n"
                                          "border-style: outset;\n"
                                          "border-width: 1px;\n"
                                          "border-radius: 0px;\n"
                                          "border-color: black;\n"
                                          "padding: 1px;")
        self.business_input.setObjectName("business_input")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.business_input)
        self.math_label = QtWidgets.QLabel(self.subjects_frame)
        self.math_label.setStyleSheet("background-color:orange;\n"
                                      "border-style: outset;\n"
                                      "border-width: 0px;\n"
                                      "border-radius: 5px;\n"
                                      "border-color: black;\n"
                                      "padding: 4px;")
        self.math_label.setObjectName("math_label")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.math_label)
        self.math_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.math_input.setStyleSheet("background:white;\n"
                                      "border-style: outset;\n"
                                      "border-width: 1px;\n"
                                      "border-radius: 0px;\n"
                                      "border-color: black;\n"
                                      "padding: 1px;")
        self.math_input.setObjectName("math_input")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.math_input)
        self.math_label_2 = QtWidgets.QLabel(self.subjects_frame)
        self.math_label_2.setStyleSheet("background-color:orange;\n"
                                        "border-style: outset;\n"
                                        "border-width: 0px;\n"
                                        "border-radius: 5px;\n"
                                        "border-color: black;\n"
                                        "padding: 4px;")
        self.math_label_2.setWordWrap(True)
        self.math_label_2.setObjectName("math_label_2")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.math_label_2)
        self.math_input_2 = QtWidgets.QLineEdit(self.subjects_frame)
        self.math_input_2.setStyleSheet("background:white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 0px;\n"
                                        "border-color: black;\n"
                                        "padding: 1px;")
        self.math_input_2.setObjectName("math_input_2")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.math_input_2)
        self.horizontalLayout_2.addWidget(self.subjects_frame)
        self.gridLayout_5.addWidget(self.database_input_frames, 1, 0, 1, 1)
        self.table_widgets_frame = QtWidgets.QFrame(self.frame)
        self.table_widgets_frame.setStyleSheet("background-color: orange;\n"
                                               "border-style: outset;\n"
                                               "border-width: 1px;\n"
                                               "border-radius: 3px;\n"
                                               "border-color: black;\n"
                                               "padding: 0px;")
        self.table_widgets_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_widgets_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_widgets_frame.setObjectName("table_widgets_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.table_widgets_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.table_widgets_frame)
        self.scrollArea.setStyleSheet("background-color: orange;\n"
                                      "border-style: outset;\n"
                                      "border-width: 0px;\n"
                                      "border-radius: 0px;\n"
                                      "border-color: black;\n"
                                      "padding: 0px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 586, 234))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setStyleSheet("background:white")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.table_widgets_frame, 2, 0, 1, 1)
        self.buttom_frame = QtWidgets.QFrame(self.frame)
        self.buttom_frame.setStyleSheet("background:orange")
        self.buttom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttom_frame.setObjectName("buttom_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.buttom_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.print_button = QtWidgets.QPushButton(self.buttom_frame)
        self.print_button.setMinimumSize(QtCore.QSize(0, 25))
        self.print_button.setStyleSheet("background-color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 5px;\n"
                                        "border-color: black;\n"
                                        "padding: 0px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Human-gnome-dev-printer-new.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_button.setIcon(icon)
        self.print_button.setIconSize(QtCore.QSize(50, 50))
        self.print_button.setObjectName("print_button")
        self.gridLayout_6.addWidget(self.print_button, 0, 0, 1, 1)
        self.add_student = QtWidgets.QPushButton(self.buttom_frame)
        self.add_student.setMinimumSize(QtCore.QSize(0, 25))
        self.add_student.setStyleSheet("background-color: white;\n"
                                       "border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 5px;\n"
                                       "border-color: black;\n"
                                       "padding: 0px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Education,_Studying,_University,_Alumni_-_icon.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.add_student.setIcon(icon1)
        self.add_student.setIconSize(QtCore.QSize(50, 50))
        self.add_student.setObjectName("add_student")
        self.gridLayout_6.addWidget(self.add_student, 0, 1, 1, 1)
        self.find_student = QtWidgets.QPushButton(self.buttom_frame)
        self.find_student.setMinimumSize(QtCore.QSize(0, 25))
        self.find_student.setStyleSheet("background-color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 5px;\n"
                                        "border-color: black;\n"
                                        "padding: 0px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("1046px-Magnifying_glass_icon_mgx2.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_student.setIcon(icon2)
        self.find_student.setIconSize(QtCore.QSize(50, 50))
        self.find_student.setObjectName("find_student")
        self.gridLayout_6.addWidget(self.find_student, 0, 2, 1, 1)
        self.remove_student = QtWidgets.QPushButton(self.buttom_frame)
        self.remove_student.setMinimumSize(QtCore.QSize(0, 25))
        self.remove_student.setStyleSheet("background-color: white;\n"
                                          "border-style: outset;\n"
                                          "border-width: 2px;\n"
                                          "border-radius: 5px;\n"
                                          "border-color: black;\n"
                                          "padding: 0px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("garbage-2091534_960_720.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_student.setIcon(icon3)
        self.remove_student.setIconSize(QtCore.QSize(45, 50))
        self.remove_student.setObjectName("remove_student")
        self.gridLayout_6.addWidget(self.remove_student, 0, 3, 1, 1)
        self.gridLayout_5.addWidget(self.buttom_frame, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setup_table()
        self.configure_buttons()
        self.selectedCells =[]

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.student_database_management_system.setText(_translate("MainWindow", "Student Database Management"))
        self.student_id_label.setText(_translate("MainWindow", "Student ID"))
        self.firstname_label.setText(_translate("MainWindow", "Firstname"))
        self.surname_label.setText(_translate("MainWindow", "Surname"))
        self.gender_label.setText(_translate("MainWindow", "Gender"))
        self.age_label.setText(_translate("MainWindow", "Age"))
        self.address_label.setText(_translate("MainWindow", "Address"))
        self.postcode_label.setText(_translate("MainWindow", "Postcode"))
        self.mobile_label.setText(_translate("MainWindow", "Mobile"))
        self.chemistry_label.setText(_translate("MainWindow", "Chemistry"))
        self.computing_label.setText(_translate("MainWindow", "Computing"))
        self.english_label.setText(_translate("MainWindow", "English"))
        self.physics_label.setText(_translate("MainWindow", "Physics"))
        self.biology_label.setText(_translate("MainWindow", "Biology"))
        self.business_label.setText(_translate("MainWindow", "Business"))
        self.math_label.setText(_translate("MainWindow", "Maths"))
        self.math_label_2.setText(_translate("MainWindow", "Additional Maths"))
        self.print_button.setText(_translate("MainWindow", "Print Student Info"))
        self.add_student.setText(_translate("MainWindow", "Add Student"))
        self.find_student.setText(_translate("MainWindow", "Find Student"))
        self.remove_student.setText(_translate("MainWindow", "Remove Student"))



    def setup_table(self):


        database = self.student_database.get_columns()

        self.column_names = []

        for column_number, column_name, *_ in database:
            self.tableWidget.insertColumn(column_number)
            self.column_names.append(column_name)

        self.tableWidget.setHorizontalHeaderLabels(self.column_names)

        database = self.student_database.get_database()

        self.populate_table(database)

        self.previous_student_id = []



    def display_student(self, row, column, info):
        self.tableWidget.setItem(row, column, info)

    def populate_table(self, dataset):

        self.tableWidget.setRowCount(len(dataset))
        # loop through the users in the database
        for row, student_info in enumerate(dataset):

            # loop through each user for the columns
            for column, info in enumerate(student_info):
                # convert the info into a widget item to place on table
                info_item = QtWidgets.QTableWidgetItem(str(info))
                # place the info on the table
                self.display_student(row, column, info_item)

    def configure_buttons(self):
        self.add_student.clicked.connect(self.add_student_to_data_base)
        self.tableWidget.cellChanged.connect(self.onCellChange)
        self.tableWidget.currentItemChanged.connect(self.on_item_change)
        self.remove_student.clicked.connect(self.remove_a_student)
        self.find_student.clicked.connect(self.find_a_student)
        self.student_id_input.textChanged.connect(self.find_a_student)
        self.tableWidget.cellClicked.connect(self.cell_clicked)



    def cell_clicked(self, row,column):
        print(column)





    def add_student_to_data_base(self):

        # check if the user is already in the to prevent updating the QTable
        student_checker = self.student_database.get_student_data(self.student_id_input.text())

        if len(self.student_id_input.text()) != 0 and student_checker is None:

            student_info = {'student_id': self.student_id_input.text(),
                            'first_name': self.firstname_input.text(),
                            'last_name': self.surname_input.text(),
                            'gender': self.gender_input.text(),
                            'age': self.age__input.text(),
                            'address': self.address_input.text(),
                            'postcode': self.postcode_input.text(),
                            'mobile': self.mobile_input.text(),
                            'chemistry': self.chemistry_input.text(),
                            'computing': self.computing_input.text(),
                            'english': self.english_input.text(),
                            'physics': self.physics_input.text(),
                            'biology': self.biology_input.text(),
                            'business': self.business_input.text(),
                            'maths': self.math_input.text(),
                            'add_math': self.math_input_2.text(),

                            }

            self.student_database.add_student(student_info)
            pop_up_message = QMessageBox.about(self, "Information", f"{self.student_id_input.text()} has been added to the system ")
            self.reset_inputs()



            new_row = self.tableWidget.rowCount()
            create_row = self.tableWidget.insertRow(new_row)

            # loop through each user for the columns
            for column, info in enumerate(student_info.values()):
                # convert the info into a widget item to place on table
                info_item = QtWidgets.QTableWidgetItem(info)
                # place the info on the table
                self.tableWidget.setItem(new_row, column, info_item)
        elif len(self.student_id_input.text()) == 0:
            pop_up_message = QMessageBox.about(self, "Requirements", "Missing Student ID")


    def reset_inputs(self):
        self.student_id_input.clear()
        self.firstname_input.clear()
        self.surname_input.clear()
        self.gender_input.clear()
        self.age__input.clear()
        self.address_input.clear()
        self.postcode_input.clear()
        self.mobile_input.clear()
        self.chemistry_input.clear()
        self.computing_input.clear()
        self.english_input.clear()
        self.physics_input.clear()
        self.biology_input.clear()
        self.business_input.clear()
        self.math_input.clear()
        self.math_input_2.clear()

    def onCellChange(self, row, column):

        updated_value = self.tableWidget.item(row, column).text()
        student_id = self.tableWidget.item(row, 0).text()
        column_name = self.column_names[column]

        self.student_database.update_student(student_id, column_name, updated_value)


    def find_a_student(self):
        student_id = self.student_id_input.text()

        find_item = self.tableWidget.findItems(student_id, Qt.MatchExactly)

        if find_item:
            self.tableWidget.clearSelection()



            selected_cell = find_item[0]

            # scroll to that item in the list
            self.tableWidget.scrollToItem(selected_cell)

            #selected_cell.setBackground(QtGui.QColor(255,128,128))
            selected_cell.setSelected(True)





    def remove_a_student(self):



        user_selected = self.tableWidget.selectedItems()

        if user_selected:

            confirmation_pop_up = QMessageBox.question(self, "Deleting User", "Are you sure you want to delete this student", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if confirmation_pop_up == QMessageBox.Yes:

                if len(user_selected) > 1:

                    for user in user_selected:
                        # try and except will be used to catch for cells that have already been deleted
                        try:
                            user_selected_row = user.row()
                            user_selected_id = self.tableWidget.item(user_selected_row, 0).text()
                            self.student_database.remove_student(user_selected_id)
                            self.tableWidget.removeRow(user_selected_row)
                        except RuntimeError:
                            pass

                else:
                    user_selected_row = user_selected[0].row()
                    # get the user id column for the selected user
                    user_selected_id = self.tableWidget.item(user_selected_row, 0).text()

                    self.student_database.remove_student(user_selected_id)
                    # remove the information from that row
                    self.tableWidget.removeRow(user_selected_row)
                    # loop through each columns and remove the values of the users for that row
        else:
            pop_up_message = QMessageBox.about(self, "Information", " No student has been selected ")


    def on_item_change(self, current, previous):
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
