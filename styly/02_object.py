# 1
import micro_widget as mw
from pomw import * 
label1 = Label().set_text("Jméno: ")
entry1 = Entry().move(0, 20)

label2 = Label().set_text("Příjmení: ").move(0, 60)
entry2 = Entry().move(0, 80)

w1 = Window()

group = Group().set_items([label1, entry1, label2, entry2])
w1.set_widget(group)



