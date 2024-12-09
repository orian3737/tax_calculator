import tkinter as tk 
class TaxCalculator:
    def __init__(self):
        #Intialize our window
        self.window = tk.Tk()
        self.window.title('Tax Calculator')
        self.window.geometry('280x200')
        self.window.resizable(False, False)
        
        #Intialize our window
        self.padding: dict = {'padx': 20, 'pady': 10}
        
        #Income label and entry
        self.income_label = tk.Label(self.window, text='Income')
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = tk.Entry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)
        
        #Tax label and entry
        self.tax_rate_label = tk.Label(self.window, text='Percent')
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = tk.Entry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)
        
        #Result label and entry
        self.result_label = tk.Label(self.window, text='Tax')
        self.result_label.grid(row=5, column=0, **self.padding)
        self.result_entry = tk.Entry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=5, column=1, **self.padding)
        
        # Calculate button
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate_tax)
        self.calculate_button.grid(row=6, column=1, **self.padding)

    def update_result(self):
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, text)
        
    def calculate_tax(self):
        try:
            income: float = float(self.income.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            self.update_result(f'${income * (tax_rate / 100):,.2f}')
        except ValueError:
            self.update_result('Invalid Response')
        import tkinter as tk 

class TaxCalculator:
    def __init__(self):
        # Initialize our window
        self.window = tk.Tk()
        self.window.title('Tax Calculator')
        self.window.geometry('280x200')
        self.window.resizable(False, False)
        
        # Initialize padding
        self.padding = {'padx': 20, 'pady': 10}
        
        # Income label and entry
        self.income_label = tk.Label(self.window, text='Income')
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = tk.Entry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)
        
        # Tax rate label and entry
        self.tax_rate_label = tk.Label(self.window, text='Percent')
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = tk.Entry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)
        
        # Result label and entry
        self.result_label = tk.Label(self.window, text='Tax')
        self.result_label.grid(row=5, column=0, **self.padding)
        self.result_entry = tk.Entry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=5, column=1, **self.padding)
        
        # Calculate button
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate_tax)
        self.calculate_button.grid(row=6, column=1, **self.padding)

    def update_result(self, text):
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, text)
        
    def calculate_tax(self):
        try:
            income = float(self.income_entry.get())  # Fixed reference to income_entry
            tax_rate = float(self.tax_rate_entry.get())
            tax = income * (tax_rate / 100)
            self.update_result(f'${tax:,.2f}')
        except ValueError:
            self.update_result('Invalid Response')
        
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()
    