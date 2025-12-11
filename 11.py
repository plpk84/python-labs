import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ChernyshevPavelAndreevich")
        self.geometry("600x400")
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.create_calculator_tab()
        self.create_checkbox_tab()
        self.create_text_tab()
        
    def create_calculator_tab(self):
        calc_frame = ttk.Frame(self.notebook)
        self.notebook.add(calc_frame, text="Калькулятор")
        
        self.num1 = tk.StringVar(value="0")
        self.num2 = tk.StringVar(value="0")
        self.operation = tk.StringVar(value="+")
        self.result = tk.StringVar(value="Результат: ")
        
        ttk.Entry(calc_frame, textvariable=self.num1).grid(row=0, column=0, padx=5, pady=5)
        
        operations = ["+", "-", "*", "/"]
        op_combo = ttk.Combobox(calc_frame, textvariable=self.operation, values=operations, state="readonly")
        op_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Entry(calc_frame, textvariable=self.num2).grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Button(calc_frame, text="=", command=self.calculate).grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(calc_frame, textvariable=self.result).grid(row=1, column=0, columnspan=4, pady=10)
        
    def calculate(self):
        try:
            n1 = float(self.num1.get()) if self.num1.get() else 0
            n2 = float(self.num2.get()) if self.num2.get() else 0
            op = self.operation.get()
            
            if op == "+":
                res = n1 + n2
            elif op == "-":
                res = n1 - n2
            elif op == "*":
                res = n1 * n2
            elif op == "/":
                if n2 == 0:
                    raise ZeroDivisionError
                res = n1 / n2
                
            if res == int(res):
                res = int(res)
            self.result.set(f"Результат: {res}")
        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль!")
        except Exception as e:
            messagebox.showerror("Ошибка", "Некорректный ввод!")
            
    def create_checkbox_tab(self):
        check_frame = ttk.Frame(self.notebook)
        self.notebook.add(check_frame, text="Чекбоксы")
        
        self.cb_vars = []
        check_texts = ["1", "2", "3"]
        
        for i, text in enumerate(check_texts):
            var = tk.BooleanVar()
            self.cb_vars.append(var)
            ttk.Checkbutton(check_frame, text=text, variable=var).pack(pady=5)
            
        ttk.Button(check_frame, text="Показать выбор", command=self.show_selection).pack(pady=10)
        
    def show_selection(self):
        selected = []
        texts = ["1", "2", "3"]
        
        for i, var in enumerate(self.cb_vars):
            if var.get():
                selected.append(texts[i])
                
        if selected:
            messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selected)}")
        else:
            messagebox.showwarning("Предупреждение", "Ничего не выбрано!")
            
    def create_text_tab(self):
        text_frame = ttk.Frame(self.notebook)
        self.notebook.add(text_frame, text="Текст")
        
        menu_frame = ttk.Frame(text_frame)
        menu_frame.pack(fill='x', pady=5)
        
        ttk.Button(menu_frame, text="Загрузить файл", command=self.load_file).pack(side='left', padx=5)
        
        self.text_area = tk.Text(text_frame, wrap='word')
        scrollbar = ttk.Scrollbar(text_frame, orient='vertical', command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=scrollbar.set)
        
        self.text_area.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, content)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {str(e)}")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()