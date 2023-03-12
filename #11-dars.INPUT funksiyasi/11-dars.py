# Entrybot's Python code

import Entry

ism = 0

def when_start():
    Entry.input("Ismingiz nima?")
    ism = Entry.answer()
    Entry.input("Yoshingz nechada?")
    ism = Entry.answer()
    Entry.input("Hobbingiz nima?")
    ism = Entry.answer()
    Entry.print(ism)