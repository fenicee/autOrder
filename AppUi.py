# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AppUi.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 551, 95))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.accesskeyLabel = QLabel(self.formLayoutWidget)
        self.accesskeyLabel.setObjectName(u"accesskeyLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.accesskeyLabel)

        self.acccesskeyLineEdit = QLineEdit(self.formLayoutWidget)
        self.acccesskeyLineEdit.setObjectName(u"acccesskeyLineEdit")
        self.acccesskeyLineEdit.setEnabled(True)
        self.acccesskeyLineEdit.setReadOnly(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.acccesskeyLineEdit)

        self.secretkeyLabel = QLabel(self.formLayoutWidget)
        self.secretkeyLabel.setObjectName(u"secretkeyLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.secretkeyLabel)

        self.secretkeyLineEdit = QLineEdit(self.formLayoutWidget)
        self.secretkeyLineEdit.setObjectName(u"secretkeyLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.secretkeyLineEdit)

        self.akskvalidatebtn = QPushButton(self.formLayoutWidget)
        self.akskvalidatebtn.setObjectName(u"akskvalidatebtn")
        self.akskvalidatebtn.setAutoDefault(False)
        self.akskvalidatebtn.setFlat(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.akskvalidatebtn)

        self.locKeybtn = QPushButton(self.formLayoutWidget)
        self.locKeybtn.setObjectName(u"locKeybtn")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.locKeybtn)

        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(0, 80, 551, 691))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.infoAreaLabel = QLabel(self.formLayoutWidget_2)
        self.infoAreaLabel.setObjectName(u"infoAreaLabel")
        self.infoAreaLabel.setLayoutDirection(Qt.LeftToRight)
        self.infoAreaLabel.setAutoFillBackground(False)
        self.infoAreaLabel.setStyleSheet(u"font: 20pt \"\u534e\u6587\u6977\u4f53\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.infoAreaLabel.setTextFormat(Qt.MarkdownText)
        self.infoAreaLabel.setScaledContents(False)
        self.infoAreaLabel.setAlignment(Qt.AlignCenter)
        self.infoAreaLabel.setWordWrap(False)

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.infoAreaLabel)

        self.textEditArea = QTextEdit(self.formLayoutWidget_2)
        self.textEditArea.setObjectName(u"textEditArea")

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.textEditArea)

        self.formLayoutWidget_3 = QWidget(self.centralwidget)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(560, 0, 721, 44))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.regionChoselabel = QLabel(self.formLayoutWidget_3)
        self.regionChoselabel.setObjectName(u"regionChoselabel")
        self.regionChoselabel.setLayoutDirection(Qt.LeftToRight)
        self.regionChoselabel.setStyleSheet(u"font: 22pt \"\u65b9\u6b63\u59da\u4f53\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.regionChoselabel.setTextFormat(Qt.AutoText)
        self.regionChoselabel.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.regionChoselabel)

        self.formLayoutWidget_4 = QWidget(self.centralwidget)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(560, 30, 241, 121))
        self.formLayout_5 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.CNorth = QLabel(self.formLayoutWidget_4)
        self.CNorth.setObjectName(u"CNorth")
        self.CNorth.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"font: 700 16pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 0, 0);")
        self.CNorth.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(0, QFormLayout.SpanningRole, self.CNorth)

        self.huhehaoteRegionLabel = QLabel(self.formLayoutWidget_4)
        self.huhehaoteRegionLabel.setObjectName(u"huhehaoteRegionLabel")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.huhehaoteRegionLabel)

        self.huhehaoteRegionCheckBox = QCheckBox(self.formLayoutWidget_4)
        self.huhehaoteRegionCheckBox.setObjectName(u"huhehaoteRegionCheckBox")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.huhehaoteRegionCheckBox)

        self.beijingRegionLabel = QLabel(self.formLayoutWidget_4)
        self.beijingRegionLabel.setObjectName(u"beijingRegionLabel")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.beijingRegionLabel)

        self.beijingRegionCheckBox = QCheckBox(self.formLayoutWidget_4)
        self.beijingRegionCheckBox.setObjectName(u"beijingRegionCheckBox")
        self.beijingRegionCheckBox.setEnabled(True)
        self.beijingRegionCheckBox.setCheckable(True)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.beijingRegionCheckBox)

        self.formLayoutWidget_5 = QWidget(self.centralwidget)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(800, 30, 241, 121))
        self.formLayout_6 = QFormLayout(self.formLayoutWidget_5)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.CNmid = QLabel(self.formLayoutWidget_5)
        self.CNmid.setObjectName(u"CNmid")
        self.CNmid.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"font: 700 16pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 0);")
        self.CNmid.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(0, QFormLayout.SpanningRole, self.CNmid)

        self.zhengzhouRegionLabel = QLabel(self.formLayoutWidget_5)
        self.zhengzhouRegionLabel.setObjectName(u"zhengzhouRegionLabel")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.zhengzhouRegionLabel)

        self.zhengzhouRegionCheckBox = QCheckBox(self.formLayoutWidget_5)
        self.zhengzhouRegionCheckBox.setObjectName(u"zhengzhouRegionCheckBox")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.zhengzhouRegionCheckBox)

        self.changshaRegionLabel = QLabel(self.formLayoutWidget_5)
        self.changshaRegionLabel.setObjectName(u"changshaRegionLabel")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.changshaRegionLabel)

        self.changshaRegionCheckBox = QCheckBox(self.formLayoutWidget_5)
        self.changshaRegionCheckBox.setObjectName(u"changshaRegionCheckBox")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.changshaRegionCheckBox)

        self.formLayoutWidget_6 = QWidget(self.centralwidget)
        self.formLayoutWidget_6.setObjectName(u"formLayoutWidget_6")
        self.formLayoutWidget_6.setGeometry(QRect(1040, 30, 241, 145))
        self.formLayout_7 = QFormLayout(self.formLayoutWidget_6)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.CNeast = QLabel(self.formLayoutWidget_6)
        self.CNeast.setObjectName(u"CNeast")
        self.CNeast.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"font: 700 16pt \"Microsoft YaHei UI\";\n"
"color: rgb(55, 255, 0);")
        self.CNeast.setAlignment(Qt.AlignCenter)

        self.formLayout_7.setWidget(0, QFormLayout.SpanningRole, self.CNeast)

        self.suzhouRegionLabel = QLabel(self.formLayoutWidget_6)
        self.suzhouRegionLabel.setObjectName(u"suzhouRegionLabel")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.suzhouRegionLabel)

        self.suzhouRegionCheckBox = QCheckBox(self.formLayoutWidget_6)
        self.suzhouRegionCheckBox.setObjectName(u"suzhouRegionCheckBox")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.suzhouRegionCheckBox)

        self.jinanRegionLabel = QLabel(self.formLayoutWidget_6)
        self.jinanRegionLabel.setObjectName(u"jinanRegionLabel")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.jinanRegionLabel)

        self.jinanRegionCheckBox = QCheckBox(self.formLayoutWidget_6)
        self.jinanRegionCheckBox.setObjectName(u"jinanRegionCheckBox")

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.jinanRegionCheckBox)

        self.shanghaiRegionLabel = QLabel(self.formLayoutWidget_6)
        self.shanghaiRegionLabel.setObjectName(u"shanghaiRegionLabel")

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.shanghaiRegionLabel)

        self.shanghaiRegionCheckBox = QCheckBox(self.formLayoutWidget_6)
        self.shanghaiRegionCheckBox.setObjectName(u"shanghaiRegionCheckBox")

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.shanghaiRegionCheckBox)

        self.hangzhouRegionLabel = QLabel(self.formLayoutWidget_6)
        self.hangzhouRegionLabel.setObjectName(u"hangzhouRegionLabel")

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.hangzhouRegionLabel)

        self.hangzhouRegionCheckBox = QCheckBox(self.formLayoutWidget_6)
        self.hangzhouRegionCheckBox.setObjectName(u"hangzhouRegionCheckBox")

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.hangzhouRegionCheckBox)

        self.formLayoutWidget_7 = QWidget(self.centralwidget)
        self.formLayoutWidget_7.setObjectName(u"formLayoutWidget_7")
        self.formLayoutWidget_7.setGeometry(QRect(560, 150, 241, 121))
        self.formLayout_8 = QFormLayout(self.formLayoutWidget_7)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_8.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.CNsouthwest = QLabel(self.formLayoutWidget_7)
        self.CNsouthwest.setObjectName(u"CNsouthwest")
        self.CNsouthwest.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"font: 700 16pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 255, 238);")
        self.CNsouthwest.setAlignment(Qt.AlignCenter)

        self.formLayout_8.setWidget(0, QFormLayout.SpanningRole, self.CNsouthwest)

        self.guiyangRegionLabel = QLabel(self.formLayoutWidget_7)
        self.guiyangRegionLabel.setObjectName(u"guiyangRegionLabel")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.guiyangRegionLabel)

        self.guiyangRegionCheckBox = QCheckBox(self.formLayoutWidget_7)
        self.guiyangRegionCheckBox.setObjectName(u"guiyangRegionCheckBox")

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.guiyangRegionCheckBox)

        self.chengduRegionLabel = QLabel(self.formLayoutWidget_7)
        self.chengduRegionLabel.setObjectName(u"chengduRegionLabel")

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.chengduRegionLabel)

        self.chengduRegionCheckBox = QCheckBox(self.formLayoutWidget_7)
        self.chengduRegionCheckBox.setObjectName(u"chengduRegionCheckBox")

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.chengduRegionCheckBox)

        self.chongqingRegionLabel = QLabel(self.formLayoutWidget_7)
        self.chongqingRegionLabel.setObjectName(u"chongqingRegionLabel")

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.chongqingRegionLabel)

        self.chongqingRegionCheckBox = QCheckBox(self.formLayoutWidget_7)
        self.chongqingRegionCheckBox.setObjectName(u"chongqingRegionCheckBox")

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.chongqingRegionCheckBox)

        self.formLayoutWidget_8 = QWidget(self.centralwidget)
        self.formLayoutWidget_8.setObjectName(u"formLayoutWidget_8")
        self.formLayoutWidget_8.setGeometry(QRect(800, 150, 241, 121))
        self.formLayout_9 = QFormLayout(self.formLayoutWidget_8)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.CNsouth = QLabel(self.formLayoutWidget_8)
        self.CNsouth.setObjectName(u"CNsouth")
        self.CNsouth.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(21, 0, 255);\n"
"font: 700 16pt \"Microsoft YaHei UI\";")
        self.CNsouth.setAlignment(Qt.AlignCenter)

        self.formLayout_9.setWidget(0, QFormLayout.SpanningRole, self.CNsouth)

        self.guangzhouRegionLabel = QLabel(self.formLayoutWidget_8)
        self.guangzhouRegionLabel.setObjectName(u"guangzhouRegionLabel")

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.guangzhouRegionLabel)

        self.guangzhouRegionCheckBox = QCheckBox(self.formLayoutWidget_8)
        self.guangzhouRegionCheckBox.setObjectName(u"guangzhouRegionCheckBox")

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.guangzhouRegionCheckBox)

        self.formLayoutWidget_9 = QWidget(self.centralwidget)
        self.formLayoutWidget_9.setObjectName(u"formLayoutWidget_9")
        self.formLayoutWidget_9.setGeometry(QRect(1040, 150, 241, 121))
        self.formLayout_10 = QFormLayout(self.formLayoutWidget_9)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.CNnorthwest = QLabel(self.formLayoutWidget_9)
        self.CNnorthwest.setObjectName(u"CNnorthwest")
        self.CNnorthwest.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"font: 700 16pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 0, 230);")
        self.CNnorthwest.setAlignment(Qt.AlignCenter)

        self.formLayout_10.setWidget(0, QFormLayout.SpanningRole, self.CNnorthwest)

        self.xianRegionLabel = QLabel(self.formLayoutWidget_9)
        self.xianRegionLabel.setObjectName(u"xianRegionLabel")

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.xianRegionLabel)

        self.xianRegionCheckBox = QCheckBox(self.formLayoutWidget_9)
        self.xianRegionCheckBox.setObjectName(u"xianRegionCheckBox")

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.xianRegionCheckBox)

        self.formLayoutWidget_10 = QWidget(self.centralwidget)
        self.formLayoutWidget_10.setObjectName(u"formLayoutWidget_10")
        self.formLayoutWidget_10.setGeometry(QRect(560, 270, 481, 272))
        self.formLayout_11 = QFormLayout(self.formLayoutWidget_10)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_11.setContentsMargins(0, 0, 0, 0)
        self.billingTypeLabel = QLabel(self.formLayoutWidget_10)
        self.billingTypeLabel.setObjectName(u"billingTypeLabel")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.billingTypeLabel)

        self.billingTypeComboBox = QComboBox(self.formLayoutWidget_10)
        self.billingTypeComboBox.addItem("")
        self.billingTypeComboBox.addItem("")
        self.billingTypeComboBox.addItem("")
        self.billingTypeComboBox.setObjectName(u"billingTypeComboBox")

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.billingTypeComboBox)

        self.durationLabel = QLabel(self.formLayoutWidget_10)
        self.durationLabel.setObjectName(u"durationLabel")

        self.formLayout_11.setWidget(1, QFormLayout.LabelRole, self.durationLabel)

        self.durationSpinBox = QSpinBox(self.formLayoutWidget_10)
        self.durationSpinBox.setObjectName(u"durationSpinBox")
        self.durationSpinBox.setMaximum(12)

        self.formLayout_11.setWidget(1, QFormLayout.FieldRole, self.durationSpinBox)

        self.specsNameLabel = QLabel(self.formLayoutWidget_10)
        self.specsNameLabel.setObjectName(u"specsNameLabel")

        self.formLayout_11.setWidget(3, QFormLayout.LabelRole, self.specsNameLabel)

        self.specsNameLineEdit = QLineEdit(self.formLayoutWidget_10)
        self.specsNameLineEdit.setObjectName(u"specsNameLineEdit")

        self.formLayout_11.setWidget(3, QFormLayout.FieldRole, self.specsNameLineEdit)

        self.quantitySpinBox = QSpinBox(self.formLayoutWidget_10)
        self.quantitySpinBox.setObjectName(u"quantitySpinBox")
        self.quantitySpinBox.setMaximum(10)

        self.formLayout_11.setWidget(2, QFormLayout.FieldRole, self.quantitySpinBox)

        self.quantityLabel = QLabel(self.formLayoutWidget_10)
        self.quantityLabel.setObjectName(u"quantityLabel")

        self.formLayout_11.setWidget(2, QFormLayout.LabelRole, self.quantityLabel)

        self.vmTypeComboBox = QComboBox(self.formLayoutWidget_10)
        self.vmTypeComboBox.addItem("")
        self.vmTypeComboBox.addItem("")
        self.vmTypeComboBox.setObjectName(u"vmTypeComboBox")

        self.formLayout_11.setWidget(4, QFormLayout.FieldRole, self.vmTypeComboBox)

        self.vmTypeLabel = QLabel(self.formLayoutWidget_10)
        self.vmTypeLabel.setObjectName(u"vmTypeLabel")

        self.formLayout_11.setWidget(4, QFormLayout.LabelRole, self.vmTypeLabel)

        self.cpuSpinBox = QSpinBox(self.formLayoutWidget_10)
        self.cpuSpinBox.setObjectName(u"cpuSpinBox")

        self.formLayout_11.setWidget(5, QFormLayout.FieldRole, self.cpuSpinBox)

        self.cpuLabel = QLabel(self.formLayoutWidget_10)
        self.cpuLabel.setObjectName(u"cpuLabel")

        self.formLayout_11.setWidget(5, QFormLayout.LabelRole, self.cpuLabel)

        self.ramSpinBox = QSpinBox(self.formLayoutWidget_10)
        self.ramSpinBox.setObjectName(u"ramSpinBox")

        self.formLayout_11.setWidget(6, QFormLayout.FieldRole, self.ramSpinBox)

        self.ramLabel = QLabel(self.formLayoutWidget_10)
        self.ramLabel.setObjectName(u"ramLabel")

        self.formLayout_11.setWidget(6, QFormLayout.LabelRole, self.ramLabel)

        self.bootVolumeSizeLineEdit = QLineEdit(self.formLayoutWidget_10)
        self.bootVolumeSizeLineEdit.setObjectName(u"bootVolumeSizeLineEdit")

        self.formLayout_11.setWidget(7, QFormLayout.FieldRole, self.bootVolumeSizeLineEdit)

        self.bootVolumeSizeLabel = QLabel(self.formLayoutWidget_10)
        self.bootVolumeSizeLabel.setObjectName(u"bootVolumeSizeLabel")

        self.formLayout_11.setWidget(7, QFormLayout.LabelRole, self.bootVolumeSizeLabel)

        self.bootVolumeTypeComboBox = QComboBox(self.formLayoutWidget_10)
        self.bootVolumeTypeComboBox.addItem("")
        self.bootVolumeTypeComboBox.addItem("")
        self.bootVolumeTypeComboBox.setObjectName(u"bootVolumeTypeComboBox")

        self.formLayout_11.setWidget(8, QFormLayout.FieldRole, self.bootVolumeTypeComboBox)

        self.bootVolumeTypeLabel = QLabel(self.formLayoutWidget_10)
        self.bootVolumeTypeLabel.setObjectName(u"bootVolumeTypeLabel")

        self.formLayout_11.setWidget(8, QFormLayout.LabelRole, self.bootVolumeTypeLabel)

        self.queryPriceBtn = QPushButton(self.formLayoutWidget_10)
        self.queryPriceBtn.setObjectName(u"queryPriceBtn")
        self.queryPriceBtn.setCheckable(False)

        self.formLayout_11.setWidget(9, QFormLayout.FieldRole, self.queryPriceBtn)

        self.queryPriceCheckbtn = QPushButton(self.formLayoutWidget_10)
        self.queryPriceCheckbtn.setObjectName(u"queryPriceCheckbtn")

        self.formLayout_11.setWidget(9, QFormLayout.LabelRole, self.queryPriceCheckbtn)

        self.formLayoutWidget_11 = QWidget(self.centralwidget)
        self.formLayoutWidget_11.setObjectName(u"formLayoutWidget_11")
        self.formLayoutWidget_11.setGeometry(QRect(560, 550, 481, 221))
        self.formLayout_12 = QFormLayout(self.formLayoutWidget_11)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.formLayout_12.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_12.setContentsMargins(0, 0, 0, 0)
        self.isIpEnableLabel = QLabel(self.formLayoutWidget_11)
        self.isIpEnableLabel.setObjectName(u"isIpEnableLabel")

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.isIpEnableLabel)

        self.bandwidthChargeModeLabel = QLabel(self.formLayoutWidget_11)
        self.bandwidthChargeModeLabel.setObjectName(u"bandwidthChargeModeLabel")

        self.formLayout_12.setWidget(1, QFormLayout.LabelRole, self.bandwidthChargeModeLabel)

        self.bandwidthChargeModeComboBox = QComboBox(self.formLayoutWidget_11)
        self.bandwidthChargeModeComboBox.addItem("")
        self.bandwidthChargeModeComboBox.addItem("")
        self.bandwidthChargeModeComboBox.setObjectName(u"bandwidthChargeModeComboBox")
        self.bandwidthChargeModeComboBox.setEnabled(False)
        self.bandwidthChargeModeComboBox.setEditable(False)

        self.formLayout_12.setWidget(1, QFormLayout.FieldRole, self.bandwidthChargeModeComboBox)

        self.bandwidthSizeLabel = QLabel(self.formLayoutWidget_11)
        self.bandwidthSizeLabel.setObjectName(u"bandwidthSizeLabel")

        self.formLayout_12.setWidget(2, QFormLayout.LabelRole, self.bandwidthSizeLabel)

        self.bandwidthSizeSpinBox = QSpinBox(self.formLayoutWidget_11)
        self.bandwidthSizeSpinBox.setObjectName(u"bandwidthSizeSpinBox")
        self.bandwidthSizeSpinBox.setEnabled(False)

        self.formLayout_12.setWidget(2, QFormLayout.FieldRole, self.bandwidthSizeSpinBox)

        self.ecsNameLabel = QLabel(self.formLayoutWidget_11)
        self.ecsNameLabel.setObjectName(u"ecsNameLabel")

        self.formLayout_12.setWidget(3, QFormLayout.LabelRole, self.ecsNameLabel)

        self.ecsNameLineEdit = QLineEdit(self.formLayoutWidget_11)
        self.ecsNameLineEdit.setObjectName(u"ecsNameLineEdit")

        self.formLayout_12.setWidget(3, QFormLayout.FieldRole, self.ecsNameLineEdit)

        self.ecspasswordLabel = QLabel(self.formLayoutWidget_11)
        self.ecspasswordLabel.setObjectName(u"ecspasswordLabel")

        self.formLayout_12.setWidget(4, QFormLayout.LabelRole, self.ecspasswordLabel)

        self.ecspasswordLineEdit = QLineEdit(self.formLayoutWidget_11)
        self.ecspasswordLineEdit.setObjectName(u"ecspasswordLineEdit")

        self.formLayout_12.setWidget(4, QFormLayout.FieldRole, self.ecspasswordLineEdit)

        self.imageNameLabel = QLabel(self.formLayoutWidget_11)
        self.imageNameLabel.setObjectName(u"imageNameLabel")

        self.formLayout_12.setWidget(5, QFormLayout.LabelRole, self.imageNameLabel)

        self.imageNameComboBox = QComboBox(self.formLayoutWidget_11)
        self.imageNameComboBox.addItem("")
        self.imageNameComboBox.addItem("")
        self.imageNameComboBox.addItem("")
        self.imageNameComboBox.addItem("")
        self.imageNameComboBox.addItem("")
        self.imageNameComboBox.addItem("")
        self.imageNameComboBox.addItem("")
        self.imageNameComboBox.addItem("")
        self.imageNameComboBox.addItem("")
        self.imageNameComboBox.addItem("")
        self.imageNameComboBox.addItem("")
        self.imageNameComboBox.setObjectName(u"imageNameComboBox")

        self.formLayout_12.setWidget(5, QFormLayout.FieldRole, self.imageNameComboBox)

        self.isIpEnableCheckBox = QCheckBox(self.formLayoutWidget_11)
        self.isIpEnableCheckBox.setObjectName(u"isIpEnableCheckBox")
        self.isIpEnableCheckBox.setChecked(False)

        self.formLayout_12.setWidget(0, QFormLayout.FieldRole, self.isIpEnableCheckBox)

        self.orderbtn = QPushButton(self.formLayoutWidget_11)
        self.orderbtn.setObjectName(u"orderbtn")

        self.formLayout_12.setWidget(6, QFormLayout.FieldRole, self.orderbtn)

        self.orderCheckbtn = QPushButton(self.formLayoutWidget_11)
        self.orderCheckbtn.setObjectName(u"orderCheckbtn")

        self.formLayout_12.setWidget(6, QFormLayout.LabelRole, self.orderCheckbtn)

        self.formLayoutWidget_12 = QWidget(self.centralwidget)
        self.formLayoutWidget_12.setObjectName(u"formLayoutWidget_12")
        self.formLayoutWidget_12.setGeometry(QRect(1040, 270, 241, 501))
        self.formLayout_13 = QFormLayout(self.formLayoutWidget_12)
        self.formLayout_13.setObjectName(u"formLayout_13")
        self.formLayout_13.setContentsMargins(0, 0, 0, 0)
        self.queryExistVmbtn = QPushButton(self.formLayoutWidget_12)
        self.queryExistVmbtn.setObjectName(u"queryExistVmbtn")

        self.formLayout_13.setWidget(0, QFormLayout.FieldRole, self.queryExistVmbtn)

        self.textEditQueryVM = QTextEdit(self.formLayoutWidget_12)
        self.textEditQueryVM.setObjectName(u"textEditQueryVM")
        self.textEditQueryVM.setEnabled(True)

        self.formLayout_13.setWidget(1, QFormLayout.FieldRole, self.textEditQueryVM)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.akskvalidatebtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.accesskeyLabel.setText(QCoreApplication.translate("MainWindow", u"Accesskey", None))
        self.secretkeyLabel.setText(QCoreApplication.translate("MainWindow", u"Secretkey", None))
        self.akskvalidatebtn.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1AccesskeySecretkey", None))
        self.locKeybtn.setText(QCoreApplication.translate("MainWindow", u"\u9501\u5b9a/\u89e3\u9501Key", None))
        self.infoAreaLabel.setText(QCoreApplication.translate("MainWindow", u"\u6d88\u606f\u533a\u57df", None))
        self.textEditArea.setMarkdown("")
        self.textEditArea.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.regionChoselabel.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u9700\u8981\u8ba2\u8d2d\u7684\u8282\u70b9", None))
        self.CNorth.setText(QCoreApplication.translate("MainWindow", u"\u534e\u5317\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.huhehaoteRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u534e\u5317-\u547c\u548c\u6d69\u7279", None))
        self.beijingRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u534e\u5317-\u5317\u4eac3", None))
#if QT_CONFIG(shortcut)
        self.beijingRegionCheckBox.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.CNmid.setText(QCoreApplication.translate("MainWindow", u"\u534e\u4e2d\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.zhengzhouRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u534e\u4e2d-\u90d1\u5dde", None))
        self.changshaRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u534e\u4e2d-\u957f\u6c992", None))
        self.CNeast.setText(QCoreApplication.translate("MainWindow", u"\u534e\u4e1c\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.suzhouRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u534e\u4e1c-\u82cf\u5dde", None))
        self.jinanRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u534e\u4e1c-\u6d4e\u5357", None))
        self.shanghaiRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u534e\u4e1c-\u4e0a\u6d77", None))
        self.hangzhouRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u534e\u4e1c-\u676d\u5dde", None))
        self.CNsouthwest.setText(QCoreApplication.translate("MainWindow", u"\u897f\u5357\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.guiyangRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u897f\u5357-\u8d35\u9633", None))
        self.chengduRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u897f\u5357-\u6210\u90fd", None))
        self.chongqingRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u897f\u5357-\u91cd\u5e86", None))
        self.CNsouth.setText(QCoreApplication.translate("MainWindow", u"\u534e\u5357\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.guangzhouRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u534e\u5357-\u5e7f\u5dde3", None))
        self.guangzhouRegionCheckBox.setText("")
        self.CNnorthwest.setText(QCoreApplication.translate("MainWindow", u"\u897f\u5317\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.xianRegionLabel.setText(QCoreApplication.translate("MainWindow", u"\u897f\u5317-\u897f\u5b89", None))
        self.billingTypeLabel.setText(QCoreApplication.translate("MainWindow", u"\u652f\u4ed8\u65b9\u5f0f", None))
        self.billingTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6309\u6708\u652f\u4ed8\uff08\u5305\u6708\uff09", None))
        self.billingTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6309\u5e74\u652f\u4ed8\uff08\u5305\u5e74\uff09", None))
        self.billingTypeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u6309\u4f7f\u7528\u65f6\u95f4\u652f\u4ed8", None))

        self.durationLabel.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u8d2d\u65f6\u957f", None))
        self.specsNameLabel.setText(QCoreApplication.translate("MainWindow", u"\u89c4\u683c\u540d\u79f0", None))
        self.quantityLabel.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf", None))
        self.vmTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u901a\u7528\u5165\u95e8\u578b", None))
        self.vmTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u901a\u7528\u578b", None))

        self.vmTypeLabel.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u4e3b\u673a\u89c4\u683c\u7c7b\u578b", None))
        self.cpuLabel.setText(QCoreApplication.translate("MainWindow", u"cpu", None))
        self.ramLabel.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5b58", None))
        self.bootVolumeSizeLabel.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u76d8\u5927\u5c0f", None))
        self.bootVolumeTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9ad8\u6027\u80fd\u578b\u786c\u76d8", None))
        self.bootVolumeTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6027\u80fd\u4f18\u5316\u578b", None))

        self.bootVolumeTypeLabel.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u76d8\u7c7b\u578b", None))
        self.queryPriceBtn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u6240\u9009\u8282\u70b9\u662f\u5426\u6709\u8be5\u914d\u7f6e\u5e76\u8be2\u4ef7\uff08\u4e91\u4e3b\u673a+\u786c\u76d8\u4ef7\u683c\uff09", None))
        self.queryPriceCheckbtn.setText(QCoreApplication.translate("MainWindow", u"\u8be2\u4ef7\u524d\u68c0\u67e5", None))
        self.isIpEnableLabel.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u8981\u8ba2\u8d2dIP", None))
        self.bandwidthChargeModeLabel.setText(QCoreApplication.translate("MainWindow", u"\u5e26\u5bbd\u6536\u8d39\u65b9\u5f0f", None))
        self.bandwidthChargeModeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6309\u5e26\u5bbd\u8ba1\u8d39", None))
        self.bandwidthChargeModeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6309\u6d41\u91cf\u8ba1\u8d39", None))

        self.bandwidthSizeLabel.setText(QCoreApplication.translate("MainWindow", u"\u5e26\u5bbd\u5927\u5c0f", None))
        self.ecsNameLabel.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u4e3b\u673a\u540d-\uff08\u6570\u5b57\u81ea\u52a8\u9012\u589e\uff09", None))
        self.ecspasswordLabel.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u4e3b\u673a\u5bc6\u7801", None))
        self.imageNameLabel.setText(QCoreApplication.translate("MainWindow", u"\u955c\u50cf", None))
        self.imageNameComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CentOS 7.9 64\u4f4d", None))
        self.imageNameComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Ubuntu 20.04 64\u4f4d", None))
        self.imageNameComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Red Hat Enterprise Linux8.1 64\u4f4d", None))
        self.imageNameComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Windows Server 2019 DataCenter 64\u4f4d \u4e2d\u6587\u7248", None))
        self.imageNameComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"BC-Linux 8.1 64\u4f4d", None))
        self.imageNameComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"BC-Linux 8.2 64\u4f4d", None))
        self.imageNameComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"CoreOS 2303.4.0 64\u4f4d", None))
        self.imageNameComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Debian 9.11 64\u4f4d", None))
        self.imageNameComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"FreeBSD 12.1 64\u4f4d", None))
        self.imageNameComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"OpenSUSE 42.3 64\u4f4d", None))
        self.imageNameComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"SUSE Linux Enterprise Server 12 SP5 64\u4f4d", None))

        self.orderbtn.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u65e0\u8bef\uff0c\u4e00\u952e\u8ba2\u8d2d\uff01", None))
        self.orderCheckbtn.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u8d2d\u524d\u68c0\u67e5", None))
        self.queryExistVmbtn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u6240\u9009\u8282\u70b9\u5e76\u5bfc\u51fa\u6210excel", None))
        self.textEditQueryVM.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

