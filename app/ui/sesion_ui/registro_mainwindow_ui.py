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
        self.groupBox_2.setGeometry(QRect(150, 120, 461, 671))
        self.contrasena_1_lineEdit = QLineEdit(self.groupBox_2)
        self.contrasena_1_lineEdit.setObjectName("contrasena_1_lineEdit")
        self.contrasena_1_lineEdit.setGeometry(QRect(110, 300, 261, 31))
        self.contrasena_1_lineEdit.setMaxLength(30)
        self.contrasena_1_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.contrasena_1_lineEdit.setClearButtonEnabled(False)
        self.usuario_lineEdit = QLineEdit(self.groupBox_2)
        self.usuario_lineEdit.setObjectName("usuario_lineEdit")
        self.usuario_lineEdit.setGeometry(QRect(110, 210, 261, 31))
        self.registrar_pushButton = QPushButton(self.groupBox_2)
        self.registrar_pushButton.setObjectName("registrar_pushButton")
        self.registrar_pushButton.setGeometry(QRect(150, 500, 171, 71))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(80, 40, 321, 41))
        font = QFont()
        font.setFamilies(["Segoe UI"])
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n" "    font-size: 32px;\n" " }")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(80, 130, 321, 1))
        self.line.setStyleSheet(
            "QFrame {\n"
            "    border: none;\n"
            "    background-color: #3f4662;\n"
            "    max-height: 1px;\n"
            "}"
        )
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(80, 210, 21, 21))
        self.label_2.setPixmap(
            QPixmap("../../../../recursos/icons/inicio_sesion/user.svg")
        )

        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(80, 300, 21, 21))
        self.label_3.setPixmap(
            QPixmap("../../../../recursos/icons/inicio_sesion/password.svg")
        )
        self.label_3.setScaledContents(True)
        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(80, 460, 321, 1))
        self.line_2.setStyleSheet(
            "QFrame {\n"
            "    border: none;\n"
            "    background-color: #3f4662;\n"
            "    max-height: 1px;\n"
            "}"
        )
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(80, 265, 221, 21))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(80, 355, 201, 21))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(80, 390, 21, 21))
        self.label_6.setPixmap(
            QPixmap("../../../recursos/icons/inicio_sesion/password.svg")
        )
        self.label_6.setScaledContents(True)
        self.contrasena_2_lineEdit = QLineEdit(self.groupBox_2)
        self.contrasena_2_lineEdit.setObjectName("contrasena_2_lineEdit")
        self.contrasena_2_lineEdit.setGeometry(QRect(110, 390, 261, 31))
        self.contrasena_2_lineEdit.setMaxLength(30)
        self.contrasena_2_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.contrasena_2_lineEdit.setClearButtonEnabled(False)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(80, 180, 121, 16))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(130, 150, 221, 21))
        font1 = QFont()
        font1.setFamilies(["Segoe UI"])
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName("label_28")
        self.label_28.setGeometry(QRect(250, 10, 101, 91))
        font2 = QFont()
        font2.setFamilies(["Segoe UI"])
        font2.setBold(False)
        font2.setItalic(True)
        self.label_28.setFont(font2)
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
        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName("label_27")
        self.label_27.setGeometry(QRect(340, 10, 101, 91))
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
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(470, 860, 321, 16))

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
        self.label_28.setText(QCoreApplication.translate("MainWindow", "K", None))
        self.label_27.setText(
            QCoreApplication.translate("MainWindow", "rypt\u00f3s", None)
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u00a9 2026 KRYPT\u00d3S. Todos los derechos reservados.",
                None,
            )
        )

    # retranslateUi
