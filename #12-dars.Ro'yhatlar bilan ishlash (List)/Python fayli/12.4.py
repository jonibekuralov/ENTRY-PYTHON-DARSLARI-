# Entrybot's Python code

import Entry

names = ["Jonibek", "Javlonbek", "Temurbek", "Uktirbek"]
ages = [10, 17, 30, 18]

def when_start():
    Entry.input("Ismingiz nima?")
    names.insert(1, Entry.answer())
    Entry.input("Yoshingiz necha?")
    ages.insert(1, Entry.answer())