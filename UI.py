import tkinter
from tkinter import ttk
from tkinter import *
from ttkbootstrap import Style

import os
import requests

URL = 'http://localhost:5000/api/predict'



class Application(tkinter.Tk):
	def __init__(self):
		super().__init__()
		self.title('Arabic Dialect Identifier')
		self.geometry('800x350')
		self.style = Style('darkly')
		self.home_screen = HomeScreen(self)
		self.home_screen.pack(fill='both', expand='yes')


class HomeScreen(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.predict_button = ttk.Button(self, text='Predict', command=self.predict, takefocus=False)
		self.predict_button.place(x=55,y=150)
		self.entry = ttk.Entry(self, width=90, justify="right")
		self.entry.place(x=200, y=150)
		self.label_prediction = ttk.Label(self, text='', font=('TkDefaultFont', 14, 'bold'))
		self.label_prediction.place(x=285, y=250)
		self.selected_option = tkinter.StringVar(value='Naive Bayes')

		menu_button = ttk.Menubutton(self, textvariable=self.selected_option, style='info.Outline.TMenubutton')
		menu_button.place(x=340, y=70)

        # create the menu and add items to it
		menu = tkinter.Menu(menu_button, tearoff=False)
		menu.add_command(label='Naive Bayes', command=lambda: self.update_option('Naive Bayes'))
		menu.add_command(label='LSTM', command=lambda: self.update_option('LSTM'))

        # set the menu for the menu button
		menu_button.configure(menu=menu)
		

	def update_option(self, option):
		self.selected_option.set(option)


	def predict(self):
		text = self.entry.get()
		# API
		payload = {'text': text, 'model_chosen': self.selected_option.get()}
		response = requests.post(URL, json=payload)
		prediction = response.json()['prediction']
		self.label_prediction.configure(text=f'Predicted Dialect: {prediction}')
		


	
if __name__ == '__main__':
	Application().mainloop()