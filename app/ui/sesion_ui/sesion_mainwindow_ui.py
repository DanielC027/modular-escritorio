# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sesion_mainwindow_ui.ui'
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


class Ui_SesionMainWindow(object):
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
        self.groupBox_2.setGeometry(QRect(150, 70, 461, 611))
        self.contrasena_lineEdit = QLineEdit(self.groupBox_2)
        self.contrasena_lineEdit.setObjectName("contrasena_lineEdit")
        self.contrasena_lineEdit.setGeometry(QRect(110, 300, 261, 22))
        self.contrasena_lineEdit.setMaxLength(30)
        self.contrasena_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.contrasena_lineEdit.setClearButtonEnabled(False)
        self.usuario_lineEdit = QLineEdit(self.groupBox_2)
        self.usuario_lineEdit.setObjectName("usuario_lineEdit")
        self.usuario_lineEdit.setGeometry(QRect(110, 210, 261, 22))
        self.iniciar_pushButton = QPushButton(self.groupBox_2)
        self.iniciar_pushButton.setObjectName("iniciar_pushButton")
        self.iniciar_pushButton.setGeometry(QRect(140, 440, 171, 71))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(160, 60, 161, 21))
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
        self.line_2.setGeometry(QRect(70, 400, 321, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.registrarse_pushButton = QPushButton(self.groupBox_2)
        self.registrarse_pushButton.setObjectName("registrarse_pushButton")
        self.registrarse_pushButton.setGeometry(QRect(290, 580, 161, 21))

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
        self.contrasena_lineEdit.setInputMask("")
        self.contrasena_lineEdit.setText("")
        self.contrasena_lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Contrase\u00f1a", None)
        )
        self.usuario_lineEdit.setText("")
        self.usuario_lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Usuario", None)
        )
        self.iniciar_pushButton.setText(
            QCoreApplication.translate("MainWindow", "INICIAR", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "INICIO DE SESI\u00d3N", None)
        )
        self.label_2.setText("")
        self.label_3.setText("")
        self.registrarse_pushButton.setText(
            QCoreApplication.translate("MainWindow", "REGISTRARSE", None)
        )

    # retranslateUi
