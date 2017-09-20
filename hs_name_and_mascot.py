# Created by: Khoa Le
# Created on September 19 2017
# Created for ICS3U
# This program is the "Highschool names and mascots" with GUI and buttons.

import ui

# This function is for when you press the "MTHS" button, the name of the school and mascot appears.
def mths_touch_up_inside(sender):
	view["high_school_name_answer_label"].text = ("Mother Teresa High School")
	view["mascot_answer_label"].text = ("Titans")

# This function is for when you press the "ST. JHS" button, the name of the school and mascot appears.
def st_jhs_touch_up_inside(sender):
	view["high_school_name_answer_label"].text = ("St. Joseph High School")
	view["mascot_answer_label"].text = ("Jaguars")

# This function is for when you press the "ST. MHS" button, the name of the school ans mascot appears.
def st_mhs_touch_up_inside(sender):
	view["high_school_name_answer_label"].text = ("St. Mark High School")
	view["mascot_answer_label"].text = ("Lions")

view = ui.load_view()
view.present('sheet')
