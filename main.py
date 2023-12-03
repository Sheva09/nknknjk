import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from ui import Ui_MainWindow

import json

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication([])
ex = Widget()

notes = {}

#Добавить заметку
def add_note():
    #Показать окно для создания заметки
    note_name, save = QInputDialog.getText(ex, "Создать заметку", "Ввести заметку")
    # Если нажали save, нету повтора и заметка не пустая
    if save and note_name not in notes and note_name != "":
        notes[note_name] = {
            "текст": "Пусто...",
            "теги": []
        }
        #Добавляем в список
        ex.ui.listWidget.addItem(note_name)


def del_note():
    #Получвкм кол-во выбраных заметок
    if len(ex.ui.listWidget.selectedItems()) > 0:
        #Выбрали заметку
        note = ex.ui.listWidget.selectedItems()[0].text()
        #Удалили заметку
        del notes[note]
        #Очистили список
        ex.ui.listWidget.clear()
        ex.ui.listWidget.addItems(notes)
        with open("notes.json", "r", encoding="utf-8") as file:
            notes = json.load(file)

def save_note():
    if len(ex.ui.listWidget.selectedItems()) > 0:
        note = ex.ui.listWidget.selectedItems()[0].text()
        notes[note] = {
            "текст": ex.ui.textEdit.toPlainText(),
            "теги": []
        }
        with open("notes.json", "w", encoding="utf 8") as file:
            json.dump(notes, file, ensure_ascii=True, indent=4)

def show_note():
    note = ex.ui.listWidget.selectedItems()[0].text()
    ex.ui.textEdit.setText(notes[note]["текст"])
    ex.ui.listWidget_2.clear()
    ex.ui.listWidget_2.addItems(notes[note]["теги"])

with open("notes.json", "r", encoding="utf-8") as file:
    notes = json.load(file)

ex.ui.listWidget.addItems(notes)

ex.ui.listWidget.itemClicked.connect(show_note)
ex.ui.pushButton.clicked.connect(add_note)
ex.ui.pushButton_4.clicked.connect(del_note)
ex.ui.pushButton_3.clicked.connect(save_note)

ex.show()
app.exec_()

























