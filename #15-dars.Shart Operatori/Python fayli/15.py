# Entrybot's Python code

import Entry

son = 0

def when_start():
    Entry.print("Kiritilgan sonni Juft yoki Toq ekanligini tekshiruvchi dastur!")
    Entry.input("Sonni kiriting: ")
    son = Entry.answer()
    if ((son % 2) == 0):
        Entry.print("Juft son")
    else:
        Entry.print("Toq son")