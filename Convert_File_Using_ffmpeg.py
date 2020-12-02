import sys
import subprocess
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QGridLayout, QPushButton,
                             QLineEdit, QSizePolicy,
                             QHBoxLayout, QVBoxLayout,
                             QFileDialog, QMessageBox)

""" Outras Variaveis. """
ext = ['mp3', 'wav', 'aac', 'ogg', 'mpeg', 'mp4', 'mkv', '3gp', 'avi', 'mov', 'wmv', 'webm']

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        """ Configurações da Janela Principal. """
        self.setWindowTitle('Conversor')
        self.setGeometry(600, 200, 600, 300)
        self.setAcceptDrops(True)
        self.grid_layout = QGridLayout()

        """ Layout vertical/horizontal """
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        """ Layout vertical/horizontal 2 """
        self.hbox2 = QHBoxLayout()
        self.vbox2 = QVBoxLayout()

        """ parte de espaçamento esquerdo. """
        self.spacing_vertical    = QVBoxLayout()
        self.spacing_horizontal  = QVBoxLayout()

        """ Cria Layout Grade e chama os itens da JP"""
        self.setLayout(self.grid_layout)
        self.Content()

    """ Itens da janela principal. """
    def Content(self):

        """ Variaveis da janela principal aqui. """
        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.drop = QtWidgets.QComboBox()
        self.dir_save = ""

        self.drop.addItems(ext)

        self.button_converter = QPushButton(text='Converter')
        self.button_file = QPushButton(text='Escolher arquivo')
        self.button_dir = QPushButton(text='Escolher diretorio onde salvar')

        self.button_converter.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        """ Parte Lateral Esquerda. """
        self.grid_layout.addLayout(self.vbox2, 0, 0)
        self.vbox2.addWidget(self.button_file)
        self.vbox2.addWidget(self.button_dir)
        self.vbox2.addWidget(QtWidgets.QLabel('Escolha o formato: '))
        self.vbox2.addSpacerItem(Qt.QSpacerItem(0, 5))

        """ Parte 1 - Main """
        self.grid_layout.addLayout(self.vbox, 0, 1)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.line2)
        self.vbox.addWidget(self.drop)

        """ Parte 2 """
        self.grid_layout.addLayout(self.spacing_horizontal, 0, 2)
        self.spacing_horizontal.addSpacerItem(Qt.QSpacerItem(30, 0))

        """ Parte 3"""
        self.grid_layout.addLayout(self.hbox, 1, 1)
        self.hbox.addWidget(self.button_converter)
        self.line1.setEnabled(False)
        self.line2.setEnabled(False)

        """ Chama as Funções de FileName, Find_Dir e Converter. """
        self.button_file.clicked.connect(self.FileName)
        self.button_dir.clicked.connect(self.Find_Dir)
        self.button_converter.clicked.connect(self.Converter)

    #Funções aqui.
    def FileName(self):
        self.pushfile = str(QFileDialog.getOpenFileName())
        self.filename = "".join(self.pushfile.split("'")[1:]).split(",")[0]
        self.file = "".join(self.filename.split("/")[-1:]).split(".")[0]
        self.file_type = "".join(self.filename).split(".")[-1]

        """ Condicional para caso não for compativel com a conversão. """
        for x in ext:
            if x == self.file_type:
                self.CSim = 'Sim'
                break
            else:
                self.CSim = 'Não'
                pass
        
        """ Condicional para colocar nome e definir na conversão. """
        if(self.CSim != 'Sim'):
            self.msg = QMessageBox.question(self, 'Arquivo não suportado', 'O arquivo não pode ser convertido pois não tem'
                ' suporte em nosso codec, quer escolher outro arquivo?',  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if self.msg  == QMessageBox.Yes :
                self.FileName()
            else:
                self.filename = 'None'
                self.line1.setText('Arquivo não suportado!')
        else:
            self.line1.setText(self.filename)

    def Find_Dir(self):
        self.dir_save = str(QFileDialog.getExistingDirectory())
        self.dir_save = self.dir_save if self.dir_save.endswith('/') else self.dir_save + '/'
        self.line2.setText(self.dir_save)

    def Converter(self):
        if self.filename == 'None':
            self.msg2 = QMessageBox.question(self, 'Arquivo não suportado', 'O arquivo não pode ser convertido pois não tem'
                ' suporte em nosso codec, quer escolher outro arquivo?',  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if self.msg2 == QMessageBox.Yes:
                self.pushfile = str(QFileDialog.getOpenFileName())
        elif self.dir_save == "" or self.dir_save == "/":
            QMessageBox.warning(self, "Pasta vazia", "A pasta não foi definida por favor escolha um local para salva o arquivo.")

        else:
            subprocess.run(['ffmpeg', '-i', str(self.filename), str(self.dir_save+self.file+"."+self.drop.currentText())])
            QMessageBox.information(self, "Done", "O arquivo Acabou de ser convertido")
        


""" Inicia o Programa. """
if __name__ == '__main__':
    app  = QApplication(sys.argv)
    init = MainWindow()
    init.show()
    sys.exit(app.exec_())
