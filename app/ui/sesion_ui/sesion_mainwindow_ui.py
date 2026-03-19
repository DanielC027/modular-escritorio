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
import sys
import os

# Asegurar que la raíz del proyecto está en sys.path
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

from recursos import recursos_rc


class Ui_SesionMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(827, 942)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "/* Fondo general */\n"
            "QWidget {\n"
            "    background-color: #1e1e2f;\n"
            "    color: #f0f0f0;\n"
            '    font-family: "Segoe UI", Arial, sans-serif;\n'
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
            "}"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet("QGroupBox{border: 1px solid #3f4662;\n" "}")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setGeometry(QRect(160, 150, 461, 611))
        self.contrasena_lineEdit = QLineEdit(self.groupBox_2)
        self.contrasena_lineEdit.setObjectName("contrasena_lineEdit")
        self.contrasena_lineEdit.setGeometry(QRect(110, 300, 261, 31))
        self.contrasena_lineEdit.setMaxLength(30)
        self.contrasena_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.contrasena_lineEdit.setClearButtonEnabled(False)
        self.usuario_lineEdit = QLineEdit(self.groupBox_2)
        self.usuario_lineEdit.setObjectName("usuario_lineEdit")
        self.usuario_lineEdit.setGeometry(QRect(110, 210, 261, 31))
        self.iniciar_pushButton = QPushButton(self.groupBox_2)
        self.iniciar_pushButton.setObjectName("iniciar_pushButton")
        self.iniciar_pushButton.setGeometry(QRect(140, 420, 171, 71))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(60, 60, 361, 51))
        font = QFont()
        font.setFamilies(["Segoe UI"])
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n" "    font-size: 32px;\n" " }")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(80, 210, 21, 21))
        self.label_2.setPixmap(QPixmap(":/iconos/iconos/inicio_sesion/user.svg"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(80, 300, 21, 21))
        self.label_3.setPixmap(QPixmap(":/iconos/iconos/inicio_sesion/password.svg"))
        self.label_3.setScaledContents(True)
        self.registrarse_pushButton = QPushButton(self.groupBox_2)
        self.registrarse_pushButton.setObjectName("registrarse_pushButton")
        self.registrarse_pushButton.setGeometry(QRect(290, 570, 161, 31))
        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(40, 150, 381, 1))
        self.line.setStyleSheet(
            "QFrame {\n"
            "    border: none;\n"
            "    background-color: #3f4662;\n"
            "    max-height: 1px;\n"
            "}"
        )
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(40, 380, 381, 1))
        self.line_2.setStyleSheet(
            "QFrame {\n"
            "    border: none;\n"
            "    background-color: #3f4662;\n"
            "    max-height: 1px;\n"
            "}"
        )
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName("label_27")
        self.label_27.setGeometry(QRect(370, 40, 101, 91))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(
            "QWidget {\n"
            "    background-color: transparent;\n"
            "}\n"
            " QLabel {\n"
            "    font-size: 32px;\n"
            "margin-top:15px;\n"
            "}"
        )
        self.label_27.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName("label_28")
        self.label_28.setGeometry(QRect(280, 40, 101, 91))
        font1 = QFont()
        font1.setFamilies(["Segoe UI"])
        font1.setBold(False)
        font1.setItalic(True)
        self.label_28.setFont(font1)
        self.label_28.setStyleSheet(
            "QWidget {\n"
            "    background-color: transparent;\n"
            "}\n"
            "QLabel {\n"
            "    font-size: 68px;\n"
            "}"
        )
        self.label_28.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(470, 860, 321, 16))

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
        self.label_27.setText(
            QCoreApplication.translate("MainWindow", "rypt\u00f3s", None)
        )
        self.label_28.setText(QCoreApplication.translate("MainWindow", "K", None))
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u00a9 2026 KRYPT\u00d3S. Todos los derechos reservados.",
                None,
            )
        )

    # retranslateUi
