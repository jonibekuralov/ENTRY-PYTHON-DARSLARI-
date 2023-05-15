# Entrybot's Python code

import Entry

	kom_son = 0
	foy_son = 0
	jami = 0

	def when_start():
		kom_son = random.randint(0, 50)
		while True:
			Entry.input(("Ichimda 0 dan 50gacha o'ylagan sonni toping." + "Eng kam urinishdagi kishi g'olibdir."))
			foy_son = Entry.answer()
			jami += 1
			if (foy_son == kom_son):
				Entry.print((("Bingo! " + jami) + " marta ichida topdingiz!"))
			else:
				if (foy_son < kom_son):
					Entry.print((foy_son + "dan yuqori."))
				else:
					Entry.print((foy_son + "dan past."))