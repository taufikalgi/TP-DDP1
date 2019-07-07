"""To gain access to the code in another module"""
from tkinter import Tk, Canvas, Label, Entry, Frame, Button, SUNKEN, END
from tkinter import messagebox

"""A Class that contains everything"""
class GUI(Frame):
	#a var to check if the program has been already run before
	global already_run
	already_run = False

	def __init__(self, master):
		Frame.__init__(self, master)
		#change the title of GUI
		master.title("EAN-13 [By Taufik Algi F.]")
		#calling the function
		self.label()
		self.make_canvas()
		#set the canvas size
		self.master.geometry("390x500")
		#dictionary which contains the structure and binary code based on EAN-13
		self.structure = { '0' : 'LLLLLL',
				  '1' : 'LLGLGG',
				  '2' : 'LLGGLG',
				  '3' : 'LLGGGL',
				  '4' : 'LGLLGG',
				  '5' : 'LGGLLG',
				  '6' : 'LGGGLL',
				  '7' : 'LGLGLG',
				  '8' : 'LGLGGL',
				  '9' : 'LGGLGL'
		}

		self.l_code = { '0' : '0001101',
				'1' : '0011001',
				'2' : '0010011',
				'3' : '0111101',
				'4' : '0100011',
				'5' : '0110001',
				'6' : '0101111',
				'7' : '0111011',
				'8' : '0110111',
				'9' : '0001011'
		}

		self.g_code = { '0' : '0100111',
				'1' : '0110011',
				'2' : '0011011',
				'3' : '0100001',
				'4' : '0011101',
				'5' : '0111001',
				'6' : '0000101',
				'7' : '0010001',
				'8' : '0001001',
				'9' : '0010111'
		}

		self.r_code = { '0' : '1110010',
				'1' : '1100110',
				'2' : '1101100',
				'3' : '1000010',
				'4' : '1011100',
				'5' : '1001110',
				'6' : '1010000',
				'7' : '1000100',
				'8' : '1001000',
				'9' : '1110100'
		}
	
	"""This function was made to make the canvas where the barcode will be drawn"""
	def make_canvas(self):
		self.make_canvas = Canvas(self, width = 300, height = 350, relief = SUNKEN, borderwidth = 3)
		self.make_canvas.grid(row = 5, column = 0)
		self.make_canvas.create_text(157, 55, font = ('bold', 15),text = "EAN-13 Barcode:")

	"""This function was made to count the thirtheenth code (checkdigit = (10 - ((odd index) + 3 * (even index) % 10))"""
	def checksum(self):
		odd = 0
		even = 0
		for i in range(0, 12):
			if ((i + 1) % 2 == 1):
				odd += int(self.entry_code.get()[i])
			else:
				even += int(self.entry_code.get()[i])
		self.res_checksum = (odd + even * 3) % 10
		if (self.res_checksum != 0):
			self.res_checksum = 10 - self.res_checksum

	"""This function was made to generate the barcode based on the code given by the user"""
	def barcode(self):
		code = self.entry_code.get() + str(self.res_checksum)
		#checking the stucture based on the dictionary declared
		self.structure_code = self.structure[self.entry_code.get()[0]]
		#initiate the position of the first barcode line
		x1 = 61
		x2 = 61
		y1 = 85
		y2 = 210
		#generate the barcode based on the structure (L/G)
		for i in range(0, 5):
			if i == 0:
				for j in '101':
					if (j == '1'):
						self.make_canvas.create_line(x1, y1, x2, y2 + 10, width = 2, fill = "blue")
						x1 += 2
						x2 += 2
					else:
						self.make_canvas.create_line(x1, y1, x2, y2 + 10, width = 2, fill = "white")
						x1 += 2
						x2 += 2
			elif i == 1:
				for j in range(len(self.structure_code)):
					if self.structure_code[j] == 'L':
						for k in self.l_code[code[j + 1]]:
							if k == '1':
								self.make_canvas.create_line(x1, y1, x2, y2, width = 2, fill = "black")
								x1 += 2
								x2 += 2
							else:
								self.make_canvas.create_line(x1, y1, x2, y2, width = 2, fill = "white")
								x1 += 2
								x2 += 2
					elif self.structure_code[j] == 'G':
						for k in self.g_code[code[j + 1]]:
							if k == '1':
								self.make_canvas.create_line(x1, y1, x2, y2, width = 2, fill = "black")
								x1 += 2
								x2 += 2
							else:
								self.make_canvas.create_line(x1, y1, x2, y2, width = 2, fill = "white")
								x1 += 2
								x2 += 2
			elif i == 2:
				for j in '01010':
					if (j == '1'):
						self.make_canvas.create_line(x1, y1, x2, y2 + 10, width = 2, fill = "blue")
						x1 += 2
						x2 += 2
					else:
						self.make_canvas.create_line(x1, y1, x2, y2 + 10, width = 2, fill = "white")
						x1 += 2
						x2 += 2
			elif i == 3:
				for j in range(7, 13):
					for k in self.r_code[code[j]]:
						if k == '1':
							self.make_canvas.create_line(x1, y1, x2, y2, width = 2, fill = "black")
							x1 += 2
							x2 += 2
						else:
							self.make_canvas.create_line(x1, y1, x2, y2, width = 2, fill = "white")
							x1 += 2
							x2 += 2
			elif i == 4:
				for j in '101':
					if (j == '1'):
						self.make_canvas.create_line(x1, y1, x2, y2 + 10, width = 2, fill = "blue")
						x1 += 2
						x2 += 2
					else:
						self.make_canvas.create_line(x1, y1, x2, y2 + 10, width = 2, fill = "white")
						x1 += 2
						x2 += 2
			self.make_canvas.create_text(157, 270, font = ('bold', 15), text = "Check Digit: " + str(self.res_checksum), fill = "orange")
		#initiate the position of the first code below the barcode
		x = 47
		y = 232
		for i in range(13):
			if i == 0 or i == 6:
				self.make_canvas.create_text(x, y, font = ('bold', 15), text = code[i])
				x += 24
			else:
				self.make_canvas.create_text(x, y, font = ('bold', 15), text = code[i])
				x += 14 
		"""self.make_canvas.create_text(52, 232, font = ('bold', 15), text = code[0])
		self.make_canvas.create_text(110, 232, font = ('bold', 15), text = code[1:7])
		self.make_canvas.create_text(200, 232, font = ('bold', 15), text = code[7:])"""
		#save everything on canvas to eps file and empty the form
		self.make_canvas.postscript(file = self.entry_name.get(), colormode = "color")
		self.entry_name.delete(0, END)
		self.entry_code.delete(0, END)

	"""This function was made to check if the input is not suitable as it should be"""
	def alert(self, event):
		#initiate that the var already_run is a global var
		global already_run
		#checking if the program has already been run before
		if (already_run):
			self.make_canvas.delete("all")
			self.make_canvas.create_text(157, 55, font = ('bold', 15),text = "EAN-13 Barcode:")
		#checking if there is input(s) that's not suitable as it should be
		if (len(self.entry_name.get()) == 0):
			messagebox.showinfo(title = "Input Error", message = "Please input the filename to save the file!")
			return 0
		elif (self.entry_name.get()[-4:] != '.eps'):
			messagebox.showinfo(title = "Input Error", message = "File name should be ended by '.eps'!")
			return 0
		elif (self.entry_code.get().isdigit() == False):
			messagebox.showinfo(title = "Input Error", message = "Only number allowed!")
			self.entry_code.delete(0, END)
			return 0
		elif (len(self.entry_code.get()) != 12):
			messagebox.showinfo(title = "Input Error", message = "Input should consist exactly 12 digits of number!\n")
			return 0
		else:
			self.checksum()
			self.barcode()
		#change the value of already_run to indicate that the program has been run before
		already_run = True

	"""This function was made to makes labels and the entry form, and in the end run the alert func if enter key is pressed"""
	def label(self):
		#make the label and the entry form, and adjust the position
		label_name = Label(self, font = (20), text = "Save barcode to PS file [eg: EAN13.eps]:")
		label_name.grid(row = 0, column = 0)
		label_code = Label(self, font = (20), text = "Enter code (first 12 decimal digits):")
		label_code.grid(row = 2, column = 0)
		self.entry_name = Entry(self, font = (17))
		self.entry_name.grid(row = 1, column = 0)
		self.entry_code = Entry(self, font = (17))
		self.entry_code.grid(row = 3, column = 0)
		self.master.bind('<Return>', self.alert)
		
"""The main body of program"""
def main():
	#initiate root as Tk(), and initiate it as an instance var of GUI class, and initiate it to barcode_gen then pack it
	root = Tk()
	barcode_generator = GUI(root)
	barcode_generator.pack()
	root.mainloop()

if __name__ == '__main__':
	main()