import requests,time
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QButtonGroup

url = "https://kur.doviz.com"
response = requests.get(url)
htmlicerigi = response.content
soup = BeautifulSoup(htmlicerigi, "html.parser")

birim = soup.find_all("span", {"class": "name"})
deger = soup.find_all("span", {"class": "value"})

liste_birim = []
liste_değer = []

button_group_left = QButtonGroup()
button_group_right = QButtonGroup()

def remove_dollar_sign(num):
        return num.replace("$","")

for a in birim:
    liste_birim.append(a.text)

for b in deger:
    deger_text = b.text.replace(",",".")
    deger_text = remove_dollar_sign(deger_text)
    liste_değer.append(deger_text)

liste_değer[5]=str(float(liste_değer[5])*float(liste_değer[1]))
liste_değer[7]=str(float(liste_değer[7])*float(liste_değer[1]))
liste_değer[4]=liste_değer[4].replace(".","",2)

guncel_kur_string = ""

for i, j in zip(liste_birim, liste_değer):
            guncel_kur_string = guncel_kur_string + i + " : " + j + "\n"

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        
        Form.resize(565, 515)
        Form.setFixedSize(565,515)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 430, 541, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.donustur = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.donustur.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.donustur)
        self.temizle = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.temizle.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.temizle)
        self.guncel_kur = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.guncel_kur.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.guncel_kur)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 121, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gramaltin_left = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.gramaltin_left.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.gramaltin_left)
        button_group_left.addButton(self.gramaltin_left)
        self.dolar_left = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.dolar_left.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.dolar_left)
        button_group_left.addButton(self.dolar_left)
        self.euro_left = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.euro_left.setObjectName("radioButton_6")
        self.verticalLayout.addWidget(self.euro_left)
        button_group_left.addButton(self.euro_left)
        self.sterlin_left = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.sterlin_left.setObjectName("radioButton_7")
        self.verticalLayout.addWidget(self.sterlin_left)
        button_group_left.addButton(self.sterlin_left)
        self.bist100_left = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.bist100_left.setObjectName("radioButton_8")
        self.verticalLayout.addWidget(self.bist100_left)
        button_group_left.addButton(self.bist100_left)
        self.bitcoin_left = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.bitcoin_left.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.bitcoin_left)
        button_group_left.addButton(self.bitcoin_left)
        self.gümüs_left = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.gümüs_left.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.gümüs_left)
        button_group_left.addButton(self.gümüs_left)
        self.brent_left = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.brent_left.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.brent_left)
        button_group_left.addButton(self.brent_left)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(430, 20, 121, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gramaltin_right = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.gramaltin_right.setObjectName("radioButton_9")
        self.verticalLayout_2.addWidget(self.gramaltin_right)
        button_group_right.addButton(self.gramaltin_right)
        self.dolar_right = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.dolar_right.setObjectName("radioButton_10")
        self.verticalLayout_2.addWidget(self.dolar_right)
        button_group_right.addButton(self.dolar_right)
        self.euro_right = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.euro_right.setObjectName("radioButton_11")
        self.verticalLayout_2.addWidget(self.euro_right)
        button_group_right.addButton(self.euro_right)
        self.sterlin_right = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.sterlin_right.setObjectName("radioButton_12")
        self.verticalLayout_2.addWidget(self.sterlin_right)
        button_group_right.addButton(self.sterlin_right)
        self.bist100_right = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.bist100_right.setObjectName("radioButton_13")
        self.verticalLayout_2.addWidget(self.bist100_right)
        button_group_right.addButton(self.bist100_right)
        self.bitcoin_right = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.bitcoin_right.setObjectName("radioButton_14")
        self.verticalLayout_2.addWidget(self.bitcoin_right)
        button_group_right.addButton(self.bitcoin_right)
        self.gümüs_right = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.gümüs_right.setObjectName("radioButton_15")
        self.verticalLayout_2.addWidget(self.gümüs_right)
        button_group_right.addButton(self.gümüs_right)
        self.brent_right = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.brent_right.setObjectName("radioButton_16")
        self.verticalLayout_2.addWidget(self.brent_right)
        button_group_right.addButton(self.brent_right)
        self.yazi_alani = QtWidgets.QTextEdit(Form)
        self.yazi_alani.setGeometry(QtCore.QRect(20, 370, 531, 81))
        self.yazi_alani.setObjectName("textEdit")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Doviz Programi"))
        self.donustur.setText(_translate("Form", "Dönüştür"))
        self.temizle.setText(_translate("Form", "Temizle"))
        self.guncel_kur.setText(_translate("Form", "Güncel Kur"))
        self.gramaltin_left.setText(_translate("Form", "GRAM ALTIN"))
        self.dolar_left.setText(_translate("Form", "DOLAR"))
        self.euro_left.setText(_translate("Form", "EURO"))
        self.sterlin_left.setText(_translate("Form", "STERLİN"))
        self.bist100_left.setText(_translate("Form", "BIST 100"))
        self.bitcoin_left.setText(_translate("Form", "BITCOIN"))
        self.gümüs_left.setText(_translate("Form", "GRAM GÜMÜŞ"))
        self.brent_left.setText(_translate("Form", "BRENT"))
        self.gramaltin_right.setText(_translate("Form", "GRAM ALTIN"))
        self.dolar_right.setText(_translate("Form", "DOLAR"))
        self.euro_right.setText(_translate("Form", "EURO"))
        self.sterlin_right.setText(_translate("Form", "STERLİN"))
        self.bist100_right.setText(_translate("Form", "BIST 100"))
        self.bitcoin_right.setText(_translate("Form", "BITCOIN"))
        self.gümüs_right.setText(_translate("Form", "GRAM GÜMÜŞ"))
        self.brent_right.setText(_translate("Form", "BRENT"))

        self.buttons()

    def buttons(self):
        self.temizle.clicked.connect(self.temizle_func)
        self.guncel_kur.clicked.connect(self.guncel_kur_print)
        self.donustur.clicked.connect(self.donustur_fuc)

    def temizle_func(self):
        button_group_left.setExclusive(False)
        button_group_right.setExclusive(False)
        
        self.yazi_alani.clear()
        self.yazi_alani.setPlaceholderText("")
        for i in button_group_left.buttons():
             i.setChecked(False)
        for i in button_group_right.buttons():
             i.setChecked(False)
             
        button_group_left.setExclusive(True)
        button_group_right.setExclusive(True)

    def guncel_kur_print(self):
        self.yazi_alani.setText(guncel_kur_string)
                 
    def donustur_fuc(self):
        if(self.yazi_alani.toPlainText()==guncel_kur_string):
             self.yazi_alani.clear()
             self.yazi_alani.setPlaceholderText("Lutfen donusturmek istediginiz miktari girin :")
        elif (not button_group_left.checkedButton() or not button_group_right.checkedButton()):
             self.yazi_alani.clear()
             self.yazi_alani.setPlaceholderText("Lütfen dönüştürmek istediğiniz para birimlerini seçin")
        else:
            miktar = self.yazi_alani.toPlainText()
            try:
                miktar = float(miktar)
                left_button = button_group_left.checkedButton()
                right_button = button_group_right.checkedButton()

                left_doviz=float(liste_değer[liste_birim.index(left_button.text())])
                right_doviz=float(liste_değer[liste_birim.index(right_button.text())])
                
                sonuc = miktar*(left_doviz/right_doviz)
                self.yazi_alani.setText(str(sonuc))
            except ValueError:
                 self.yazi_alani.clear()
                 self.yazi_alani.setPlaceholderText("Lutfen geçerli bir miktar girin")
                         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


