import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero!"

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        
        # Entry field for input/output
        self.entry = tk.Entry(root, width=20, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]
        
        # Create and place buttons
        for (text, row, col) in buttons:
            btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 12),
                           command=lambda t=text: self.button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)
        
    def button_click(self, char):
        if char == '=':
            try:
                # Get the expression from entry
                expression = self.entry.get().strip()
                if not expression:
                    return
                
                # Split into numbers and operation
                for op in ['+', '-', '*', '/']:
                    if op in expression:
                        num1, num2 = expression.split(op)
                        num1 = float(num1.strip())
                        num2 = float(num2.strip())
                        
                        # Perform calculation using match
                        match op:
                            case '+':
                                result = add(num1, num2)
                            case '-':
                                result = subtract(num1, num2)
                            case '*':
                                result = multiply(num1, num2)
                            case '/':
                                result = divide(num1, num2)
                        
                        # Display result
                        self.entry.delete(0, tk.END)
                        self.entry.insert(tk.END, str(result))
                        return
                        
                messagebox.showerror("Error", "Invalid expression!")
            except ValueError:
                messagebox.showerror("Error", "Invalid input! Use numbers.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
                
        elif char == 'C':
            # Clear the entry
            self.entry.delete(0, tk.END)
        else:
            # Append character to entry
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()