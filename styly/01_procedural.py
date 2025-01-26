import micro_widget as mw

# 1
def make_counter():
    value = 0
    return ['counter', value]

#def make_counter(value):
 #   return ['counter', value]

def get_counter_value(counter):
  return counter[1]

def inc_counter(counter):
  counter[1] += 1

def set_counter_value(counter, value):
  counter[1] = value

# 2
import micro_widget as mw

def change_button_click_handler(button):
    mw.set_button_text(button, "text 2")

def make_change_button(button):
    button = mw.make_button(window)
    mw.set_button_text(button, "text 1")
    mw.set_button_x(button, 20)
    mw.set_button_x(button, 60)
    mw.set_button_click_handler(button, change_button_click_handler)
    return button

# 3
import micro_widget as mw

def make_integer_entry(window):
    entry = mw.make_entry(window)
    mw.set_entry_change_handler(entry, integer_entry_change_handler)
    return ["integer_entry", entry]

def integer_entry_change_handler(entry):
    # getting text from entry
    text = mw.get_entry_text(entry)
    # text validation - if text is not a number - set empty text
    if not text.isdigit():
        mw.set_entry_text(entry, "")

#5

import micro_widget as mw

def make_resetable_entry(window):
  entry = mw.make_entry(window)
  mw.set_change_handler(entry, change_handler)

def make_reset_button(window):
  button = mw.make_button(window)
  mw.set_button_text(button, "Reset")
  mw.set_button_click_handler(button, click_handler)

def click_handler(button):
  mw.


def change_handler(entry):
  mw

# test A
def make_storage(value1, value2):
    return ["storage", value1, value2]

#def get_storage_value1(storage):
#    return storage[1]

#def get_storage_value2(storage):
#    return storage[2]

def storage_swap(storage):
    storage[1], storage[2] = storage[2], storage[1]
    return storage

# test B
def make_storage(value1, value2):
    return ["storage", value1, value2]

#def get_storage_value1(storage):
 #   return storage[1]

#def get_storage_value2(storage):
#    return storage[2]

def storage_swap(storage):
    return make_storage(storage[2], storage[1])
