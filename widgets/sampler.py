# Form implementation generated from reading ui file 'sampler.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Sampler(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(351, 447)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setMaximum(180)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout.addWidget(self.horizontalSlider_2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setMaximum(300)
        self.horizontalSlider.setProperty("value", 75)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.comboBox_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Steps"))
        self.label_2.setText(_translate("Form", "Scale"))
        self.label_3.setText(_translate("Form", "Sampler"))
        self.comboBox.setItemText(0, _translate("Form", "ddim"))
        self.comboBox.setItemText(1, _translate("Form", "plms"))
        self.comboBox.setItemText(2, _translate("Form", "klms"))
        self.comboBox.setItemText(3, _translate("Form", "dpm2"))
        self.comboBox.setItemText(4, _translate("Form", "dpm2_ancestral"))
        self.comboBox.setItemText(5, _translate("Form", "heun"))
        self.comboBox.setItemText(6, _translate("Form", "euler"))
        self.comboBox.setItemText(7, _translate("Form", "euler_ancestral"))
        self.label_4.setText(_translate("Form", "Sample Mode"))
        self.comboBox_2.setItemText(0, _translate("Form", "bicubic"))
        self.comboBox_2.setItemText(1, _translate("Form", "bilinear"))
        self.comboBox_2.setItemText(2, _translate("Form", "nearest"))
        self.label_5.setText(_translate("Form", "Seed"))
        self.label_6.setText(_translate("Form", "Seed Behavior"))
        self.comboBox_3.setItemText(0, _translate("Form", "iter"))
        self.comboBox_3.setItemText(1, _translate("Form", "fixed"))
        self.comboBox_3.setItemText(2, _translate("Form", "random"))
