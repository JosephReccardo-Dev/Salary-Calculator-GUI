"""
Program: salaryGUI_JR.py
Author: Joseph Reccardo 7/19/2023

Description:This is a GUI-based program typed in standard python language. This is a weekly wage calculator that takes input for the emplyees hourly wage, and number of hours worked; then computes the two user provided values and returns the employees weekly earnings.

NOTE: The file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
# Other imports go here
import math
from tkinter.font import Font

# Class Header
class SalaryGUI(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		#Call to the easy frame constructor method.
		EasyFrame.__init__(self, title = "Salary Calculator", width = 375, height = 250, background = "Dark khaki")

		#Create and add the components to the window
		"""Adding a header to the GUI frame"""
		self.addLabel(text = "Employee Salary Calculator", row = 0, column = 0, columnspan = 2, sticky = "NSEW", font = Font(family = "Trebuchet MS", size = 18), background = "Dark khaki", foreground = "dark green")

		"""Adding a label and float field for the Emplyee hourly wage"""
		self.addLabel(text = "Employee hourly wage: $", row = 1, column = 0, sticky = "E", font = Font(family = "Trebuchet MS", size = 12), background = "Dark khaki", foreground = "dark green")
		self.hWage = self.addFloatField(value = 0.0, row = 1, column = 1, width = 8, sticky = "W")

		"""Adding a label and float field for the amout of hours worked by the Employee"""
		self.addLabel(text = "Employee billable hours:", row = 2, column = 0, sticky = "E", font = Font(family = "Trebuchet MS", size = 12), background = "Dark khaki", foreground = "dark green")
		self.hWorked = self.addFloatField(value = 0.0, row = 2, column = 1, width = 8, sticky = "W")

		"""Creating a button and giving a varible name for later use"""
		self.cash = self.addButton(text = "Calculate Salary", row = 3, column = 0, columnspan = 2, command = self.cash)
		self.cash["background"] = "forest green"
		self.cash["foreground"] = "honeydew"

		"""Creating the calculated salary output label, and float field"""
		self.addLabel(text = "Emplyee calculated wage: $", row = 4, column = 0, sticky = "E", font = Font(family = "Trebuchet MS", size = 12), background = "Dark khaki", foreground = "dark green")
		self.earned = self.addFloatField(value = "", row = 4, column = 1, sticky = "W", width = 10, state = "readonly", precision = 2)

		"""Creating a Checkbutton to calculate the total the employee will take home"""
		self.takeHome = self.addCheckbutton(text = "The take home value", row = 5, column = 0, sticky = "SW", command = self.takeHome)
		self.takeHome["background"] = "Dark khaki"
		self.takeHome["foreground"] = "blue"

	#Processing phase
	"""Defining cash to get the user input vales, multiply their hourly wage and hours worked and output to the 'total' float field"""
	def cash(self):
		hourly = self.hWage.getNumber()
		worked = self.hWorked.getNumber()
		total = hourly * worked

		self.earned.setNumber(total)

	"""Defining the takeHome Checkbutton"""
	def takeHome(self):

		hourly2 = self.hWage.getNumber()
		worked2 = self.hWorked.getNumber()
		total = hourly2 * worked2
		taxes = total * .22
		newTotal = total - taxes

		if self.takeHome.isChecked():
			self.addLabel(text = "Taxed at 22 percent: $", row = 6, column = 0, sticky = "SE", font = Font(family = "Trebuchet MS", size = 10), background = "Dark khaki", foreground = "dark green")
			self.newValue = self.addFloatField(value = "", row = 6, column = 1, sticky = "SW", precision = 2, width = 8, state = "readonly")

			self.newValue.setNumber(newTotal)

# Global definition of the main() method
def main():
	SalaryGUI().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()