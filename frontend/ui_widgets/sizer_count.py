# Form implementation generated from reading ui file 'sizer_count.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_txt2img(object):
    def setupUi(self, txt2img):
        txt2img.setObjectName("txt2img")
        txt2img.resize(545, 289)
        self.gridLayout = QtWidgets.QGridLayout(txt2img)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(txt2img)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.horizontalSlider_4 = QtWidgets.QSlider(txt2img)
        self.horizontalSlider_4.setMaximum(200)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.gridLayout.addWidget(self.horizontalSlider_4, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(txt2img)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalSlider_3 = QtWidgets.QSlider(txt2img)
        self.horizontalSlider_3.setMaximum(2000)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout.addWidget(self.horizontalSlider_3, 5, 0, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(txt2img)
        self.horizontalSlider.setMaximum(2048)
        self.horizontalSlider.setSingleStep(64)
        self.horizontalSlider.setPageStep(64)
        self.horizontalSlider.setProperty("value", 512)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 1, 0, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(txt2img)
        self.horizontalSlider_2.setMaximum(2048)
        self.horizontalSlider_2.setSingleStep(64)
        self.horizontalSlider_2.setPageStep(64)
        self.horizontalSlider_2.setProperty("value", 512)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout.addWidget(self.horizontalSlider_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(txt2img)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(txt2img)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)

        self.retranslateUi(txt2img)
        QtCore.QMetaObject.connectSlotsByName(txt2img)

    def retranslateUi(self, txt2img):
        _translate = QtCore.QCoreApplication.translate
        txt2img.setWindowTitle(_translate("txt2img", "Form"))
        self.label_4.setText(_translate("txt2img", "Height"))
        self.label_3.setText(_translate("txt2img", "Width"))
        self.label.setText(_translate("txt2img", "Batch size"))
        self.label_2.setText(_translate("txt2img", "Samples"))
