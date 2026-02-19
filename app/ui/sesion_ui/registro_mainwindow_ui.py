# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_mainwindow_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QWidget,
)


class Ui_RegistroMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1427, 963)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setGeometry(QRect(150, 70, 461, 671))
        self.contrasena_1_lineEdit = QLineEdit(self.groupBox_2)
        self.contrasena_1_lineEdit.setObjectName("contrasena_1_lineEdit")
        self.contrasena_1_lineEdit.setGeometry(QRect(110, 300, 261, 22))
        self.contrasena_1_lineEdit.setMaxLength(30)
        self.contrasena_1_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.contrasena_1_lineEdit.setClearButtonEnabled(False)
        self.usuario_lineEdit = QLineEdit(self.groupBox_2)
        self.usuario_lineEdit.setObjectName("usuario_lineEdit")
        self.usuario_lineEdit.setGeometry(QRect(110, 210, 261, 22))
        self.registrar_pushButton = QPushButton(self.groupBox_2)
        self.registrar_pushButton.setObjectName("registrar_pushButton")
        self.registrar_pushButton.setGeometry(QRect(140, 500, 171, 71))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(200, 60, 91, 21))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(80, 130, 321, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(80, 210, 21, 21))
        self.label_2.setPixmap(
            QPixmap("../../../recursos/icons/inicio_sesion/user.svg")
        )
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(80, 300, 21, 21))
        self.label_3.setPixmap(
            QPixmap("../../../recursos/icons/inicio_sesion/password.svg")
        )
        self.label_3.setScaledContents(True)
        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(70, 460, 321, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(80, 270, 201, 16))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(80, 360, 181, 16))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(80, 390, 21, 21))
        self.label_6.setPixmap(
            QPixmap("../../../recursos/icons/inicio_sesion/password.svg")
        )
        self.label_6.setScaledContents(True)
        self.contrasena_2_lineEdit = QLineEdit(self.groupBox_2)
        self.contrasena_2_lineEdit.setObjectName("contrasena_2_lineEdit")
        self.contrasena_2_lineEdit.setGeometry(QRect(110, 390, 261, 22))
        self.contrasena_2_lineEdit.setMaxLength(30)
        self.contrasena_2_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.contrasena_2_lineEdit.setClearButtonEnabled(False)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(80, 180, 121, 16))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(150, 150, 181, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle("")
        self.contrasena_1_lineEdit.setInputMask("")
        self.contrasena_1_lineEdit.setText("")
        self.contrasena_1_lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Contrase\u00f1a", None)
        )
        self.usuario_lineEdit.setText("")
        self.usuario_lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Usuario", None)
        )
        self.registrar_pushButton.setText(
            QCoreApplication.translate("MainWindow", "REGISTRAR", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", "REGISTRO", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow", "Contrase\u00f1a Identidad 1 (original)", None
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "MainWindow", "Contrase\u00f1a Identidad 2 (falsa)", None
            )
        )
        self.label_6.setText("")
        self.contrasena_2_lineEdit.setInputMask("")
        self.contrasena_2_lineEdit.setText("")
        self.contrasena_2_lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Contrase\u00f1a", None)
        )
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", "Crea un usuario", None)
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow", "Rellena los siguientes campos.", None
            )
        )

    # retranslateUi
