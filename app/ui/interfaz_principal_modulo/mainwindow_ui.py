# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_ui.ui'
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
    QDateEdit,
    QDateTimeEdit,
    QFrame,
    QGraphicsView,
    QGridLayout,
    QGroupBox,
    QHeaderView,
    QLabel,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QTabWidget,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1489, 969)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(20, 70, 1441, 841))
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.label_25 = QLabel(self.tab)
        self.label_25.setObjectName("label_25")
        self.label_25.setGeometry(QRect(410, 60, 661, 61))
        font = QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setGeometry(QRect(170, 150, 1121, 511))
        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName("label_26")
        self.label_26.setGeometry(QRect(50, 80, 1031, 301))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_26.setFont(font1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Escritos_Escritos_treeWidget = QTreeWidget(self.tab_2)
        __qtreewidgetitem = QTreeWidgetItem(self.Escritos_Escritos_treeWidget)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.Escritos_Escritos_treeWidget)
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        self.Escritos_Escritos_treeWidget.setObjectName("Escritos_Escritos_treeWidget")
        self.Escritos_Escritos_treeWidget.setGeometry(QRect(9, 9, 256, 761))
        self.Escritos_Nuevo_pushButton = QPushButton(self.tab_2)
        self.Escritos_Nuevo_pushButton.setObjectName("Escritos_Nuevo_pushButton")
        self.Escritos_Nuevo_pushButton.setGeometry(QRect(270, 20, 75, 24))
        self.Escritos_Guardar_pushButton = QPushButton(self.tab_2)
        self.Escritos_Guardar_pushButton.setObjectName("Escritos_Guardar_pushButton")
        self.Escritos_Guardar_pushButton.setGeometry(QRect(350, 20, 75, 24))
        self.Escritos_Escrito_textEdit = QTextEdit(self.tab_2)
        self.Escritos_Escrito_textEdit.setObjectName("Escritos_Escrito_textEdit")
        self.Escritos_Escrito_textEdit.setGeometry(QRect(270, 50, 1031, 721))
        self.Escritos_Eliminar_pushButton = QPushButton(self.tab_2)
        self.Escritos_Eliminar_pushButton.setObjectName("Escritos_Eliminar_pushButton")
        self.Escritos_Eliminar_pushButton.setGeometry(QRect(430, 20, 75, 24))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.Graficas_Anio_radioButton = QRadioButton(self.tab_5)
        self.Graficas_Anio_radioButton.setObjectName("Graficas_Anio_radioButton")
        self.Graficas_Anio_radioButton.setGeometry(QRect(580, 670, 92, 20))
        self.Graficas_Fecha_dateEdit = QDateEdit(self.tab_5)
        self.Graficas_Fecha_dateEdit.setObjectName("Graficas_Fecha_dateEdit")
        self.Graficas_Fecha_dateEdit.setGeometry(QRect(180, 140, 113, 24))
        self.Graficas_Fecha_dateEdit.setCurrentSection(QDateTimeEdit.Section.DaySection)
        self.Graficas_Fecha_dateEdit.setCalendarPopup(True)
        self.Graficas_Fecha_dateEdit.setDate(QDate(2026, 2, 6))
        self.label = QLabel(self.tab_5)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(130, 140, 41, 21))
        self.Graficas_Grafica_graphicsView = QGraphicsView(self.tab_5)
        self.Graficas_Grafica_graphicsView.setObjectName(
            "Graficas_Grafica_graphicsView"
        )
        self.Graficas_Grafica_graphicsView.setGeometry(QRect(440, 20, 761, 621))
        self.Graficas_Mes_radioButton = QRadioButton(self.tab_5)
        self.Graficas_Mes_radioButton.setObjectName("Graficas_Mes_radioButton")
        self.Graficas_Mes_radioButton.setGeometry(QRect(710, 670, 61, 20))
        self.Graficas_Semana_radioButton = QRadioButton(self.tab_5)
        self.Graficas_Semana_radioButton.setObjectName("Graficas_Semana_radioButton")
        self.Graficas_Semana_radioButton.setGeometry(QRect(820, 670, 92, 20))
        self.Graficas_Dia_radioButton = QRadioButton(self.tab_5)
        self.Graficas_Dia_radioButton.setObjectName("Graficas_Dia_radioButton")
        self.Graficas_Dia_radioButton.setGeometry(QRect(950, 670, 92, 20))
        self.Graficas_Dia_radioButton.setChecked(True)
        self.label_8 = QLabel(self.tab_5)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(110, 100, 61, 16))
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout = QGridLayout(self.tab_8)
        self.gridLayout.setObjectName("gridLayout")
        self.Configuracion_Cambiar_Contrasena = QLabel(self.tab_8)
        self.Configuracion_Cambiar_Contrasena.setObjectName(
            "Configuracion_Cambiar_Contrasena"
        )
        self.Configuracion_Cambiar_Contrasena.setFont(font)
        self.Configuracion_Cambiar_Contrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.Configuracion_Cambiar_Contrasena, 0, 0, 1, 1)

        self.line_4 = QFrame(self.tab_8)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 1)

        self.Configuracion_Crear_Cuenta_Web = QLabel(self.tab_8)
        self.Configuracion_Crear_Cuenta_Web.setObjectName(
            "Configuracion_Crear_Cuenta_Web"
        )
        self.Configuracion_Crear_Cuenta_Web.setFont(font)
        self.Configuracion_Crear_Cuenta_Web.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.Configuracion_Crear_Cuenta_Web, 2, 0, 1, 1)

        self.line = QFrame(self.tab_8)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)

        self.Configuracion_Eliminar_Cuenta_Web = QLabel(self.tab_8)
        self.Configuracion_Eliminar_Cuenta_Web.setObjectName(
            "Configuracion_Eliminar_Cuenta_Web"
        )
        self.Configuracion_Eliminar_Cuenta_Web.setFont(font)
        self.Configuracion_Eliminar_Cuenta_Web.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.gridLayout.addWidget(self.Configuracion_Eliminar_Cuenta_Web, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tab_8, "")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(1180, 930, 271, 16))
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName("label_27")
        self.label_27.setGeometry(QRect(1180, 20, 171, 61))
        font2 = QFont()
        font2.setPointSize(43)
        self.label_27.setFont(font2)
        self.label_27.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )
        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName("label_28")
        self.label_28.setGeometry(QRect(1110, 10, 101, 91))
        font3 = QFont()
        font3.setFamilies(["Segoe Script"])
        font3.setPointSize(60)
        font3.setBold(False)
        font3.setItalic(True)
        self.label_28.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label_25.setText(
            QCoreApplication.translate("MainWindow", "EL DIARIO", None)
        )
        self.groupBox_3.setTitle("")
        self.label_26.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Llevar un diario es una pr\u00e1ctica poderosa para la salud mental porque permite expresar libremente pensamientos, emociones y experiencias sin temor al juicio externo. \n"
                "Es un espacio \u00edntimo donde las palabras se convierten en un desahogo y, al mismo tiempo, en una herramienta para comprendernos mejor.\n"
                "\n"
                "La privacidad de lo que se escribe es fundamental: al saber que nadie m\u00e1s acceder\u00e1 a esas p\u00e1ginas, se abre un espacio de libertad mental en el que podemos ser aut\u00e9nticos, \n"
                "vulnerables y sinceros con nosotros mismos. Ese resguardo privado es lo que convierte al diario en un refugio personal y en un recurso esencial para el bienestar emocional.\n"
                "",
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "INICIO", None),
        )
        ___qtreewidgetitem = self.Escritos_Escritos_treeWidget.headerItem()
        ___qtreewidgetitem.setText(
            0, QCoreApplication.translate("MainWindow", "ESCRITOS", None)
        )

        __sortingEnabled = self.Escritos_Escritos_treeWidget.isSortingEnabled()
        self.Escritos_Escritos_treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.Escritos_Escritos_treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(
            0, QCoreApplication.translate("MainWindow", "2025", None)
        )
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(
            0, QCoreApplication.translate("MainWindow", "DIC", None)
        )
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(
            0, QCoreApplication.translate("MainWindow", "29/12/2025", None)
        )
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(
            0, QCoreApplication.translate("MainWindow", "30/12/2025", None)
        )
        ___qtreewidgetitem5 = ___qtreewidgetitem2.child(2)
        ___qtreewidgetitem5.setText(
            0, QCoreApplication.translate("MainWindow", "31/12/2025", None)
        )
        ___qtreewidgetitem6 = self.Escritos_Escritos_treeWidget.topLevelItem(1)
        ___qtreewidgetitem6.setText(
            0, QCoreApplication.translate("MainWindow", "2026", None)
        )
        ___qtreewidgetitem7 = ___qtreewidgetitem6.child(0)
        ___qtreewidgetitem7.setText(
            0, QCoreApplication.translate("MainWindow", "ENE", None)
        )
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(
            0, QCoreApplication.translate("MainWindow", "21/01/2025", None)
        )
        ___qtreewidgetitem9 = ___qtreewidgetitem6.child(1)
        ___qtreewidgetitem9.setText(
            0, QCoreApplication.translate("MainWindow", "FEB", None)
        )
        ___qtreewidgetitem10 = ___qtreewidgetitem9.child(0)
        ___qtreewidgetitem10.setText(
            0, QCoreApplication.translate("MainWindow", "05/02/2026", None)
        )
        ___qtreewidgetitem11 = ___qtreewidgetitem9.child(1)
        ___qtreewidgetitem11.setText(
            0, QCoreApplication.translate("MainWindow", "06/02/2026", None)
        )
        self.Escritos_Escritos_treeWidget.setSortingEnabled(__sortingEnabled)

        self.Escritos_Nuevo_pushButton.setText(
            QCoreApplication.translate("MainWindow", "Nuevo", None)
        )
        self.Escritos_Guardar_pushButton.setText(
            QCoreApplication.translate("MainWindow", "Guardar", None)
        )
        self.Escritos_Eliminar_pushButton.setText(
            QCoreApplication.translate("MainWindow", "Eliminar", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "ESCRITOS", None),
        )
        self.Graficas_Anio_radioButton.setText(
            QCoreApplication.translate("MainWindow", "A\u00d1O", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", "Fecha:", None))
        self.Graficas_Mes_radioButton.setText(
            QCoreApplication.translate("MainWindow", "MES", None)
        )
        self.Graficas_Semana_radioButton.setText(
            QCoreApplication.translate("MainWindow", "SEMANA", None)
        )
        self.Graficas_Dia_radioButton.setText(
            QCoreApplication.translate("MainWindow", "D\u00cdA", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", "Selecci\u00f3n:", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_5),
            QCoreApplication.translate("MainWindow", "GRAFICAS", None),
        )
        self.Configuracion_Cambiar_Contrasena.setText(
            QCoreApplication.translate("MainWindow", "Cambiar contrase\u00f1a", None)
        )
        self.Configuracion_Crear_Cuenta_Web.setText(
            QCoreApplication.translate("MainWindow", "Crear cuenta web", None)
        )
        self.Configuracion_Eliminar_Cuenta_Web.setText(
            QCoreApplication.translate("MainWindow", "Eliminar cuenta web", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_8),
            QCoreApplication.translate("MainWindow", "CONFIGURACI\u00d3N", None),
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u00a9 2026 KRYPT\u00d3S. Todos los derechos reservados.",
                None,
            )
        )
        self.label_27.setText(
            QCoreApplication.translate("MainWindow", "rypt\u00f3s", None)
        )
        self.label_28.setText(QCoreApplication.translate("MainWindow", "K", None))

    # retranslateUi
