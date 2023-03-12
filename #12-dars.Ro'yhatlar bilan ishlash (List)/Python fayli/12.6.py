# Entrybot's Python code

import Entry

names = ["Jonibek", "Javlonbek", "Temurbek", "Uktirbek"]
ages = [10, 17, 30, 18]

def when_start():
    Entry.input("Nechinchi ismni ko'rishni xohlaysiz? ")
    Entry.print_for_sec(names[Entry.answer() - 1], 2)