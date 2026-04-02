# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_mainwindow_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
from recursos import recursos_rc

class Ui_RegistroMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(655, 942)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"/* Fondo general */\n"
"QWidget {\n"
"    background-color: #1e1e2f;\n"
"    color: #f0f0f0;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #3a3f5a;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #50577a;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2c3147;\n"
"}\n"
"\n"
"/* Inputs */\n"
"QLineEdit, QTextEdit, QPlainTextEdit {\n"
"    background-color: #2a2f45;\n"
"    border: 1px solid #3f4662;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: #2a2f45;\n"
"    border: 1px solid #3f4662;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"/* Scrollbar */\n"
"QScrollBar:vertical {\n"
"    backg"
                        "round: #1e1e2f;\n"
"    width: 10px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #3a3f5a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #50577a;\n"
"}\n"
"\n"
"/* CheckBox */\n"
"QCheckBox {\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #6c8cff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* Tabs */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #3f4662;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #2a2f45;\n"
"    padding: 8px;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #3a3f5a;\n"
"}\n"
"\n"
"/* Tooltips */\n"
"QToolTip {\n"
"    background-color: #3a3f5a;\n"
"    color: #ffffff;\n"
"    border: 1px solid #6c8cff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox{border: 1px solid #3f4662;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        font.setItalic(True)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"QLabel {\n"
"    font-size: 68px;\n"
"}")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_28, 0, 0, 1, 1)

        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"QWidget {\n"
"    background-color: transparent;\n"
"}\n"
" QLabel {\n"
"    font-size: 32px;\n"
"margin-top:15px;\n"
"}")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_27, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
" }")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"    background-color: #3f4662;\n"
"    max-height: 1px;\n"
"}")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.line)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(True)
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.label_8)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.label_7)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/iconos/iconos/inicio_sesion/user.svg"))
        self.label_2.setScaledContents(True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.usuario_lineEdit = QLineEdit(self.groupBox_2)
        self.usuario_lineEdit.setObjectName(u"usuario_lineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.usuario_lineEdit)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.label_4)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.label_10)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/iconos/iconos/inicio_sesion/password.svg"))
        self.label_3.setScaledContents(True)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.contrasena_1_lineEdit = QLineEdit(self.groupBox_2)
        self.contrasena_1_lineEdit.setObjectName(u"contrasena_1_lineEdit")
        self.contrasena_1_lineEdit.setMaxLength(30)
        self.contrasena_1_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.contrasena_1_lineEdit.setClearButtonEnabled(False)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.contrasena_1_lineEdit)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.SpanningRole, self.label_5)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.label_11)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/iconos/iconos/inicio_sesion/password.svg"))
        self.label_6.setScaledContents(True)

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.contrasena_2_lineEdit = QLineEdit(self.groupBox_2)
        self.contrasena_2_lineEdit.setObjectName(u"contrasena_2_lineEdit")
        self.contrasena_2_lineEdit.setMaxLength(30)
        self.contrasena_2_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.contrasena_2_lineEdit.setClearButtonEnabled(False)

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.contrasena_2_lineEdit)

        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"    background-color: #3f4662;\n"
"    max-height: 1px;\n"
"}")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(11, QFormLayout.ItemRole.SpanningRole, self.line_2)

        self.registrar_pushButton = QPushButton(self.groupBox_2)
        self.registrar_pushButton.setObjectName(u"registrar_pushButton")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.FieldRole, self.registrar_pushButton)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"rypt\u00f3s", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"REGISTRO", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rellena los siguientes campos.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Crea un usuario (Solo letras)", None))
        self.label_2.setText("")
        self.usuario_lineEdit.setText("")
        self.usuario_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a Identidad 1 (original)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Minimo: \n"
" 1 digito, 1 mayuscula, 1 minuscula,\n"
" 1 caracter especial, 8 Caracteres en total", None))
        self.label_3.setText("")
        self.contrasena_1_lineEdit.setInputMask("")
        self.contrasena_1_lineEdit.setText("")
        self.contrasena_1_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a Identidad 2 (falsa)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Minimo: \n"
" 1 digito, 1 mayuscula, 1 minuscula,\n"
" 1 caracter especial, 8 Caracteres en total", None))
        self.label_6.setText("")
        self.contrasena_2_lineEdit.setInputMask("")
        self.contrasena_2_lineEdit.setText("")
        self.contrasena_2_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.registrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2026 KRYPT\u00d3S. Todos los derechos reservados.", None))
    # retranslateUi

