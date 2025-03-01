# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_columnQOrOvW.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(240, 600)
        LeftColumn.setMinimumSize(QSize(0, 40))
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_btn_1 = QFrame(self.menu_1)
        self.frame_btn_1.setObjectName(u"frame_btn_1")
        self.frame_btn_1.setMinimumSize(QSize(0, 40))
        self.frame_btn_1.setMaximumSize(QSize(16777215, 40))
        self.frame_btn_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_btn_1.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_1_layout_ = QVBoxLayout(self.frame_btn_1)
        self.btn_1_layout_.setSpacing(0)
        self.btn_1_layout_.setObjectName(u"btn_1_layout_")
        self.btn_1_layout_.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_btn_1)

        self.frame_btn_2 = QFrame(self.menu_1)
        self.frame_btn_2.setObjectName(u"frame_btn_2")
        self.frame_btn_2.setMinimumSize(QSize(0, 40))
        self.frame_btn_2.setMaximumSize(QSize(16777215, 40))
        self.frame_btn_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_btn_2.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_2_layout_ = QVBoxLayout(self.frame_btn_2)
        self.btn_2_layout_.setSpacing(0)
        self.btn_2_layout_.setObjectName(u"btn_2_layout_")
        self.btn_2_layout_.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_btn_2)

        self.frame_2 = QFrame(self.menu_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_btn_3 = QFrame(self.menu_1)
        self.frame_btn_3.setObjectName(u"frame_btn_3")
        self.frame_btn_3.setEnabled(True)
        self.frame_btn_3.setMinimumSize(QSize(0, 40))
        self.frame_btn_3.setMaximumSize(QSize(16777215, 40))
        self.frame_btn_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_btn_3.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_3_layout_ = QVBoxLayout(self.frame_btn_3)
        self.btn_3_layout_.setSpacing(0)
        self.btn_3_layout_.setObjectName(u"btn_3_layout_")
        self.btn_3_layout_.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_btn_3)

        self.frame_btn_4 = QFrame(self.menu_1)
        self.frame_btn_4.setObjectName(u"frame_btn_4")
        self.frame_btn_4.setMaximumSize(QSize(16777215, 40))
        self.frame_btn_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_btn_4.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_4_layout_ = QVBoxLayout(self.frame_btn_4)
        self.btn_4_layout_.setSpacing(0)
        self.btn_4_layout_.setObjectName(u"btn_4_layout_")
        self.btn_4_layout_.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_btn_4)

        self.frame = QFrame(self.menu_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.result_text_layout = QVBoxLayout()
        self.result_text_layout.setSpacing(0)
        self.result_text_layout.setObjectName(u"result_text_layout")

        self.verticalLayout.addLayout(self.result_text_layout)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.btn_4_widget = QWidget(self.menu_2)
        self.btn_4_widget.setObjectName(u"btn_4_widget")
        self.btn_4_widget.setMinimumSize(QSize(0, 40))
        self.btn_4_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_4_layout = QVBoxLayout(self.btn_4_widget)
        self.btn_4_layout.setSpacing(0)
        self.btn_4_layout.setObjectName(u"btn_4_layout")
        self.btn_4_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_4_widget)

        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.menu_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font-size: 9pt")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("LeftColumn", u"Menu 2 - Left Menu", None))
        self.label_3.setText(QCoreApplication.translate("LeftColumn", u"This is just an example menu.\n"
"Add Qt Widgets or your custom widgets here.", None))
    # retranslateUi

