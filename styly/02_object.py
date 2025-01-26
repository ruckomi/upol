# 1a
import micro_widget as mw
from pomw import * 

label1 = Label().set_text("Jméno: ")
entry1 = Entry().move(0, 20)

label2 = Label().set_text("Příjmení: ").move(0, 60)
entry2 = Entry().move(0, 80)

w1 = Window()

group = Group().set_items([label1, entry1, label2, entry2])
w1.set_widget(group)

# 1b - enriched with procedure "create_label_entry" for repetitive steps
from pomw import *

def create_label_entry(label_text, x, y):
    label = Label().set_text(label_text).move(x, y)
    entry = Entry().move(x, y + 20)
    return label, entry

#creating a main window
window = Window()

# creating required content
label1, entry1 = create_label_entry("Jméno:", 0, 0)
label2, entry2 = create_label_entry("Příjmení:", 0, 60)

# grouping and visualisation of content
group = Group().set_items([label1, entry1, label2, entry2])
window.set_widget(group)

# 2 
from pomw import *

def make_counter():
    label = Label().set_text("0")
    button = Button().set_text("+").move(0, 30)

    def increment(button):
        current_value = int(label.get_text())
        label.set_text(str(current_value + 1))

    button.set_click_handler(increment)

    # potřebuju, aby mi z toho vylezlo duo label-button, tzn. seskupím
    counter_group = Group().set_items([label, button])
    return counter_group



