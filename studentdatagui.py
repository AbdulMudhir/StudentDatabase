# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentdatabasement.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from studentsql import StudentDatabase
from PyQt5.QtSql import QSqlTableModel


class Ui_MainWindow(object):
    def __init__(self):
        self.student_database = StudentDatabase("student_database.db")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(554, 627)
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
        self.student_database_management_system = QtWidgets.QLabel(self.frame)
        self.student_database_management_system.setGeometry(QtCore.QRect(90, 0, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.student_database_management_system.setFont(font)
        self.student_database_management_system.setObjectName("student_database_management_system")
        self.buttom_frame = QtWidgets.QFrame(self.frame)
        self.buttom_frame.setGeometry(QtCore.QRect(10, 560, 511, 41))
        self.buttom_frame.setStyleSheet("background:orange")
        self.buttom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttom_frame.setObjectName("buttom_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttom_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.print_button = QtWidgets.QPushButton(self.buttom_frame)
        self.print_button.setMinimumSize(QtCore.QSize(0, 25))
        self.print_button.setStyleSheet("background-color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 5px;\n"
                                        "border-color: black;\n"
                                        "padding: 0px;")
        self.print_button.setObjectName("print_button")
        self.horizontalLayout.addWidget(self.print_button)
        self.add_student = QtWidgets.QPushButton(self.buttom_frame)
        self.add_student.setMinimumSize(QtCore.QSize(0, 25))
        self.add_student.setStyleSheet("background-color: white;\n"
                                       "border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 5px;\n"
                                       "border-color: black;\n"
                                       "padding: 0px;")
        self.add_student.setObjectName("add_student")
        self.horizontalLayout.addWidget(self.add_student)
        self.find_student = QtWidgets.QPushButton(self.buttom_frame)
        self.find_student.setMinimumSize(QtCore.QSize(0, 25))
        self.find_student.setStyleSheet("background-color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 5px;\n"
                                        "border-color: black;\n"
                                        "padding: 0px;")
        self.find_student.setObjectName("find_student")
        self.horizontalLayout.addWidget(self.find_student)
        self.update_students = QtWidgets.QPushButton(self.buttom_frame)
        self.update_students.setMinimumSize(QtCore.QSize(0, 25))
        self.update_students.setStyleSheet("background-color: white;\n"
                                           "border-style: outset;\n"
                                           "border-width: 2px;\n"
                                           "border-radius: 5px;\n"
                                           "border-color: black;\n"
                                           "padding: 0px;")
        self.update_students.setObjectName("update_students")
        self.horizontalLayout.addWidget(self.update_students)
        self.table_widgets_frame = QtWidgets.QFrame(self.frame)
        self.table_widgets_frame.setGeometry(QtCore.QRect(10, 360, 511, 191))
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 491, 171))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.table_view = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.table_view.setStyleSheet("background-color:white;\n"
                                      "border-style: outset;\n"
                                      "border-width: 1px;\n"
                                      "border-radius: 5px;\n"
                                      "border-color: black;\n"
                                      "padding: 0px;")
        self.table_view.setObjectName("table_view")
        self.table_view.setColumnCount(0)
        self.table_view.setRowCount(0)
        self.gridLayout_4.addWidget(self.table_view, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.database_input_frames = QtWidgets.QFrame(self.frame)
        self.database_input_frames.setGeometry(QtCore.QRect(10, 50, 511, 301))
        self.database_input_frames.setStyleSheet("background-color: rgb(255, 174, 10);\n"
                                                 "border-style: outset;\n"
                                                 "border-width: 1px;\n"
                                                 "border-radius: 15px;\n"
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
        self.student_info_frame.setStyleSheet("background:orange")
        self.student_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_info_frame.setObjectName("student_info_frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.student_info_frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.student_id_label = QtWidgets.QLabel(self.student_info_frame)
        self.student_id_label.setObjectName("student_id_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.student_id_label)
        self.student_id_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.student_id_input.setStyleSheet("background:white;\n"
                                            "border-style: outset;\n"
                                            "border-width: 1px;\n"
                                            "border-radius: 0px;\n"
                                            "border-color: black;\n"
                                            "padding: 1px;")
        self.student_id_input.setObjectName("student_id_input")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.student_id_input)
        self.firstname_label = QtWidgets.QLabel(self.student_info_frame)
        self.firstname_label.setObjectName("firstname_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.firstname_label)
        self.firstname_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.firstname_input.setStyleSheet("background:white;\n"
                                           "border-style: outset;\n"
                                           "border-width: 1px;\n"
                                           "border-radius: 0px;\n"
                                           "border-color: black;\n"
                                           "padding: 1px;")
        self.firstname_input.setObjectName("firstname_input")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firstname_input)
        self.surname_label = QtWidgets.QLabel(self.student_info_frame)
        self.surname_label.setObjectName("surname_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.surname_label)
        self.surname_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.surname_input.setStyleSheet("background:white;\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 0px;\n"
                                         "border-color: black;\n"
                                         "padding: 1px;")
        self.surname_input.setObjectName("surname_input")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.surname_input)
        self.gender_label = QtWidgets.QLabel(self.student_info_frame)
        self.gender_label.setObjectName("gender_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.gender_label)
        self.gender_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.gender_input.setStyleSheet("background:white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 0px;\n"
                                        "border-color: black;\n"
                                        "padding: 1px;")
        self.gender_input.setObjectName("gender_input")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.gender_input)
        self.age_label = QtWidgets.QLabel(self.student_info_frame)
        self.age_label.setObjectName("age_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.age_label)
        self.age__input = QtWidgets.QLineEdit(self.student_info_frame)
        self.age__input.setStyleSheet("background:white;\n"
                                      "border-style: outset;\n"
                                      "border-width: 1px;\n"
                                      "border-radius: 0px;\n"
                                      "border-color: black;\n"
                                      "padding: 1px;")
        self.age__input.setObjectName("age__input")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.age__input)
        self.address_label = QtWidgets.QLabel(self.student_info_frame)
        self.address_label.setObjectName("address_label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.address_label)
        self.address_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.address_input.setStyleSheet("background:white;\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 0px;\n"
                                         "border-color: black;\n"
                                         "padding: 1px;")
        self.address_input.setObjectName("address_input")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.address_input)
        self.postcode_label = QtWidgets.QLabel(self.student_info_frame)
        self.postcode_label.setObjectName("postcode_label")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.postcode_label)
        self.postcode_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.postcode_input.setStyleSheet("background:white;\n"
                                          "border-style: outset;\n"
                                          "border-width: 1px;\n"
                                          "border-radius: 0px;\n"
                                          "border-color: black;\n"
                                          "padding: 1px;")
        self.postcode_input.setObjectName("postcode_input")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.postcode_input)
        self.mobile_label = QtWidgets.QLabel(self.student_info_frame)
        self.mobile_label.setObjectName("mobile_label")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.mobile_label)
        self.mobile_input = QtWidgets.QLineEdit(self.student_info_frame)
        self.mobile_input.setStyleSheet("background:white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 0px;\n"
                                        "border-color: black;\n"
                                        "padding: 1px;")
        self.mobile_input.setObjectName("mobile_input")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.mobile_input)
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
        self.subject_label = QtWidgets.QLabel(self.subjects_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.subject_label.setFont(font)
        self.subject_label.setStyleSheet("border-style: outset;\n"
                                         "border-radius: 0px;\n"
                                         "border-width: 0px;\n"
                                         "border-color: black;\n"
                                         "padding: 0px;")
        self.subject_label.setObjectName("subject_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.subject_label)
        self.score_label = QtWidgets.QLabel(self.subjects_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.score_label.setFont(font)
        self.score_label.setStyleSheet("border-style: outset;\n"
                                       "border-radius: 0px;\n"
                                       "border-width: 0px;\n"
                                       "border-color: black;\n"
                                       "padding: 0px;")
        self.score_label.setObjectName("score_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.score_label)
        self.chemistry_label = QtWidgets.QLabel(self.subjects_frame)
        self.chemistry_label.setObjectName("chemistry_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.chemistry_label)
        self.chemistry_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.chemistry_input.setStyleSheet("background:white;\n"
                                           "border-style: outset;\n"
                                           "border-width: 1px;\n"
                                           "border-radius: 0px;\n"
                                           "border-color: black;\n"
                                           "padding: 1px;")
        self.chemistry_input.setObjectName("chemistry_input")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chemistry_input)
        self.computing_label = QtWidgets.QLabel(self.subjects_frame)
        self.computing_label.setObjectName("computing_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.computing_label)
        self.computing_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.computing_input.setStyleSheet("background:white;\n"
                                           "border-style: outset;\n"
                                           "border-width: 1px;\n"
                                           "border-radius: 0px;\n"
                                           "border-color: black;\n"
                                           "padding: 1px;")
        self.computing_input.setObjectName("computing_input")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.computing_input)
        self.english_label = QtWidgets.QLabel(self.subjects_frame)
        self.english_label.setObjectName("english_label")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.english_label)
        self.english_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.english_input.setStyleSheet("background:white;\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 0px;\n"
                                         "border-color: black;\n"
                                         "padding: 1px;")
        self.english_input.setObjectName("english_input")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.english_input)
        self.physics_label = QtWidgets.QLabel(self.subjects_frame)
        self.physics_label.setObjectName("physics_label")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.physics_label)
        self.physics_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.physics_input.setStyleSheet("background:white;\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 0px;\n"
                                         "border-color: black;\n"
                                         "padding: 1px;")
        self.physics_input.setObjectName("physics_input")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.physics_input)
        self.biology_label = QtWidgets.QLabel(self.subjects_frame)
        self.biology_label.setObjectName("biology_label")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.biology_label)
        self.biology_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.biology_input.setStyleSheet("background:white;\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 0px;\n"
                                         "border-color: black;\n"
                                         "padding: 1px;")
        self.biology_input.setObjectName("biology_input")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.biology_input)
        self.business_label = QtWidgets.QLabel(self.subjects_frame)
        self.business_label.setObjectName("business_label")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.business_label)
        self.business_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.business_input.setStyleSheet("background:white;\n"
                                          "border-style: outset;\n"
                                          "border-width: 1px;\n"
                                          "border-radius: 0px;\n"
                                          "border-color: black;\n"
                                          "padding: 1px;")
        self.business_input.setObjectName("business_input")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.business_input)
        self.math_label = QtWidgets.QLabel(self.subjects_frame)
        self.math_label.setObjectName("math_label")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.math_label)
        self.math_input = QtWidgets.QLineEdit(self.subjects_frame)
        self.math_input.setStyleSheet("background:white;\n"
                                      "border-style: outset;\n"
                                      "border-width: 1px;\n"
                                      "border-radius: 0px;\n"
                                      "border-color: black;\n"
                                      "padding: 1px;")
        self.math_input.setObjectName("math_input")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.math_input)
        self.math_label_2 = QtWidgets.QLabel(self.subjects_frame)
        self.math_label_2.setWordWrap(True)
        self.math_label_2.setObjectName("math_label_2")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.math_label_2)
        self.math_input_2 = QtWidgets.QLineEdit(self.subjects_frame)
        self.math_input_2.setStyleSheet("background:white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 0px;\n"
                                        "border-color: black;\n"
                                        "padding: 1px;")
        self.math_input_2.setObjectName("math_input_2")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.math_input_2)
        self.horizontalLayout_2.addWidget(self.subjects_frame)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setup_table()
        self.configure_buttons()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.student_database_management_system.setText(_translate("MainWindow", "Student Database Management System"))
        self.print_button.setText(_translate("MainWindow", "Print Student Info"))
        self.add_student.setText(_translate("MainWindow", "Add Student"))
        self.find_student.setText(_translate("MainWindow", "Find Student"))
        self.update_students.setText(_translate("MainWindow", "Update Student"))
        self.student_id_label.setText(_translate("MainWindow", "Student ID"))
        self.firstname_label.setText(_translate("MainWindow", "Firstname"))
        self.surname_label.setText(_translate("MainWindow", "Surname"))
        self.gender_label.setText(_translate("MainWindow", "Gender"))
        self.age_label.setText(_translate("MainWindow", "Age"))
        self.address_label.setText(_translate("MainWindow", "Address"))
        self.postcode_label.setText(_translate("MainWindow", "Postcode"))
        self.mobile_label.setText(_translate("MainWindow", "Mobile"))
        self.subject_label.setText(_translate("MainWindow", "Subjects"))
        self.score_label.setText(_translate("MainWindow", "Score"))
        self.chemistry_label.setText(_translate("MainWindow", "Chemistry"))
        self.computing_label.setText(_translate("MainWindow", "Computing"))
        self.english_label.setText(_translate("MainWindow", "English"))
        self.physics_label.setText(_translate("MainWindow", "Physics"))
        self.biology_label.setText(_translate("MainWindow", "Biology"))
        self.business_label.setText(_translate("MainWindow", "Business"))
        self.math_label.setText(_translate("MainWindow", "Maths"))
        self.math_label_2.setText(_translate("MainWindow", "Additional Maths"))

    def setup_table(self):
        database = self.student_database.get_columns()

        column_names = []
        for column_number, column_name, *_ in database:
            self.table_view.insertColumn(column_number)
            column_names.append(column_name)

        self.table_view.setHorizontalHeaderLabels(column_names)

        database = self.student_database.get_database()

        # loop through the users in the database
        for row, student_info in enumerate(database):
            self.table_view.insertRow(row)
            # loop through each user for the columns
            for column, info in enumerate(student_info):
                # convert the info into a widget item to place on table
                info_item = QtWidgets.QTableWidgetItem(info)
                # place the info on the table
                self.table_view.setItem(row, column, info_item)

    def configure_buttons(self):
        self.add_student.clicked.connect(self.add_student_to_data_base)

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

            new_row = self.table_view.rowCount()
            create_row = self.table_view.insertRow(new_row)

            # loop through each user for the columns
            for column, info in enumerate(student_info.values()):
                # convert the info into a widget item to place on table
                info_item = QtWidgets.QTableWidgetItem(info)
                # place the info on the table
                self.table_view.setItem(new_row, column, info_item)


def update_table(self):
    database = self.student_database.get_database()

    for row, student_info in enumerate(database, start=1):
        for info in student_info:
            info = QtWidgets.QTableWidgetItem([info])
            self.table_view.setItem(row, 0, info)

        # student_id = student_info[0]
        # student_f_name = student_info[1]
        # student_l_name = student_info[2]
        # student_gender = student_info[3]
        # student_age = student_info[4]
        # student_address = student_info[5]
        # student_postcode = student_info[6]
        # student_mobile = student_info[7]
        # student_chemistry = student_info[8]
        # student_computing = student_info[9]
        # student_english = student_info[10]
        # student_physics = student_info[11]
        # student_biology = student_info[12]
        # student_business = student_info[13]
        # student_maths = student_info[14]
        # student_add_math = student_info[15]


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
