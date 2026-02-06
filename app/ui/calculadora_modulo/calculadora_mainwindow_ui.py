# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow_calc.ui'
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
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 739)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_siete = QPushButton(self.centralwidget)
        self.pushButton_siete.setObjectName("pushButton_siete")
        self.pushButton_siete.setGeometry(QRect(20, 240, 121, 101))
        self.pushButton_ocho = QPushButton(self.centralwidget)
        self.pushButton_ocho.setObjectName("pushButton_ocho")
        self.pushButton_ocho.setGeometry(QRect(140, 240, 121, 101))
        self.pushButton_nueve = QPushButton(self.centralwidget)
        self.pushButton_nueve.setObjectName("pushButton_nueve")
        self.pushButton_nueve.setGeometry(QRect(260, 240, 121, 101))
        self.pushButton_cuatro = QPushButton(self.centralwidget)
        self.pushButton_cuatro.setObjectName("pushButton_cuatro")
        self.pushButton_cuatro.setGeometry(QRect(20, 340, 121, 101))
        self.pushButton_seis = QPushButton(self.centralwidget)
        self.pushButton_seis.setObjectName("pushButton_seis")
        self.pushButton_seis.setGeometry(QRect(260, 340, 121, 101))
        self.pushButton_cinco = QPushButton(self.centralwidget)
        self.pushButton_cinco.setObjectName("pushButton_cinco")
        self.pushButton_cinco.setGeometry(QRect(140, 340, 121, 101))
        self.pushButton_uno = QPushButton(self.centralwidget)
        self.pushButton_uno.setObjectName("pushButton_uno")
        self.pushButton_uno.setGeometry(QRect(20, 440, 121, 101))
        self.pushButton_tres = QPushButton(self.centralwidget)
        self.pushButton_tres.setObjectName("pushButton_tres")
        self.pushButton_tres.setGeometry(QRect(260, 440, 121, 101))
        self.pushButton_dos = QPushButton(self.centralwidget)
        self.pushButton_dos.setObjectName("pushButton_dos")
        self.pushButton_dos.setGeometry(QRect(140, 440, 121, 101))
        self.pushButton_punto = QPushButton(self.centralwidget)
        self.pushButton_punto.setObjectName("pushButton_punto")
        self.pushButton_punto.setGeometry(QRect(20, 540, 121, 101))
        self.pushButton_cero = QPushButton(self.centralwidget)
        self.pushButton_cero.setObjectName("pushButton_cero")
        self.pushButton_cero.setGeometry(QRect(140, 540, 121, 101))
        self.pushButton_igual = QPushButton(self.centralwidget)
        self.pushButton_igual.setObjectName("pushButton_igual")
        self.pushButton_igual.setGeometry(QRect(260, 540, 121, 101))
        palette = QPalette()
        brush = QBrush(QColor(0, 103, 192, 179))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 228))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        brush2 = QBrush(QColor(0, 129, 235, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush2
        )
        brush3 = QBrush(QColor(255, 255, 255, 9))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush3
        )
        brush4 = QBrush(QColor(0, 125, 227, 128))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush4
        )
        # endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush2
        )
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush3
        )
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush4
        )
        # endif
        brush5 = QBrush(QColor(249, 249, 249, 77))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush5
        )
        brush6 = QBrush(QColor(0, 0, 0, 92))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush6
        )
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush3
        )
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush4
        )
        # endif
        self.pushButton_igual.setPalette(palette)
        self.pushButton_menos = QPushButton(self.centralwidget)
        self.pushButton_menos.setObjectName("pushButton_menos")
        self.pushButton_menos.setGeometry(QRect(380, 340, 91, 101))
        self.pushButton_mas = QPushButton(self.centralwidget)
        self.pushButton_mas.setObjectName("pushButton_mas")
        self.pushButton_mas.setGeometry(QRect(380, 440, 91, 101))
        self.pushButton_multiplicacion = QPushButton(self.centralwidget)
        self.pushButton_multiplicacion.setObjectName("pushButton_multiplicacion")
        self.pushButton_multiplicacion.setGeometry(QRect(380, 240, 91, 101))
        self.pushButton_division = QPushButton(self.centralwidget)
        self.pushButton_division.setObjectName("pushButton_division")
        self.pushButton_division.setGeometry(QRect(260, 170, 121, 71))
        self.pushButton_eliminar_de_operacion = QPushButton(self.centralwidget)
        self.pushButton_eliminar_de_operacion.setObjectName(
            "pushButton_eliminar_de_operacion"
        )
        self.pushButton_eliminar_de_operacion.setGeometry(QRect(20, 170, 121, 71))
        self.pushButton_eliminar_caracter = QPushButton(self.centralwidget)
        self.pushButton_eliminar_caracter.setObjectName("pushButton_eliminar_caracter")
        self.pushButton_eliminar_caracter.setGeometry(QRect(140, 170, 121, 71))
        self.pushButton_eliminar_caracter.setFlat(False)
        self.lineEdit_contenido = QLineEdit(self.centralwidget)
        self.lineEdit_contenido.setObjectName("lineEdit_contenido")
        self.lineEdit_contenido.setGeometry(QRect(20, 50, 451, 111))
        font = QFont()
        font.setPointSize(28)
        self.lineEdit_contenido.setFont(font)
        self.lineEdit_contenido.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.lineEdit_contenido.setReadOnly(True)
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
        self.pushButton_siete.setText(
            QCoreApplication.translate("MainWindow", "7", None)
        )
        self.pushButton_ocho.setText(
            QCoreApplication.translate("MainWindow", "8", None)
        )
        self.pushButton_nueve.setText(
            QCoreApplication.translate("MainWindow", "9", None)
        )
        self.pushButton_cuatro.setText(
            QCoreApplication.translate("MainWindow", "4", None)
        )
        self.pushButton_seis.setText(
            QCoreApplication.translate("MainWindow", "6", None)
        )
        self.pushButton_cinco.setText(
            QCoreApplication.translate("MainWindow", "5", None)
        )
        self.pushButton_uno.setText(QCoreApplication.translate("MainWindow", "1", None))
        self.pushButton_tres.setText(
            QCoreApplication.translate("MainWindow", "3", None)
        )
        self.pushButton_dos.setText(QCoreApplication.translate("MainWindow", "2", None))
        self.pushButton_punto.setText(
            QCoreApplication.translate("MainWindow", ".", None)
        )
        self.pushButton_cero.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.pushButton_igual.setText(
            QCoreApplication.translate("MainWindow", "=", None)
        )
        self.pushButton_menos.setText(
            QCoreApplication.translate("MainWindow", "-", None)
        )
        self.pushButton_mas.setText(QCoreApplication.translate("MainWindow", "+", None))
        self.pushButton_multiplicacion.setText(
            QCoreApplication.translate("MainWindow", "x", None)
        )
        self.pushButton_division.setText(
            QCoreApplication.translate("MainWindow", "/", None)
        )
        self.pushButton_eliminar_de_operacion.setText(
            QCoreApplication.translate("MainWindow", "CE", None)
        )
        self.pushButton_eliminar_caracter.setText(
            QCoreApplication.translate("MainWindow", "DEL", None)
        )
        self.lineEdit_contenido.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )

    # retranslateUi
