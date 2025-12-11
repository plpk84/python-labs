import tkinter as tk
from tkinter import ttk, messagebox
import json
import urllib.request
import os

# 6 Вариант
class GitHubApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ChernyshevPavelAndreevich")
        self.geometry("500x200")
        
        self.create_widgets()
        
    def create_widgets(self):
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill='both', expand=True)
        
        ttk.Label(main_frame, text="Введите имя репозитория:", font=('Arial', 12)).pack(pady=10)
        
        self.repo_entry = ttk.Entry(main_frame, width=50, font=('Arial', 10))
        self.repo_entry.pack(pady=5)
        self.repo_entry.insert(0, "firehol/blocklist-ipsets")
        
        ttk.Button(main_frame, text="Получить информацию", command=self.get_repo_info).pack(pady=20)
        
        self.status_label = ttk.Label(main_frame, text="", font=('Arial', 10))
        self.status_label.pack()
        
    def get_repo_info(self):
        repo_name = self.repo_entry.get().strip()
        if not repo_name:
            messagebox.showerror("Ошибка", "Введите имя репозитория")
            return
            
        try:
            repo_url = f"https://api.github.com/repos/{repo_name}"
            with urllib.request.urlopen(repo_url) as response:
                repo_data = json.loads(response.read().decode())
            
            owner_url = repo_data['owner']['url']
            with urllib.request.urlopen(owner_url) as response:
                owner_data = json.loads(response.read().decode())
            
            result = {
                'company': owner_data.get('company'),
                'created_at': owner_data.get('created_at'),
                'email': owner_data.get('email'),
                'id': owner_data.get('id'),
                'name': owner_data.get('name') or owner_data.get('login'),
                'url': owner_data.get('url')
            }
            
            script_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(script_dir, 'repository_info.json')
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            
            self.status_label.config(text="Информация сохранена в repository_info.json")
            messagebox.showinfo("Успех", "Данные успешно сохранены в файл repository_info.json")
            
        except urllib.error.HTTPError as e:
            if e.code == 404:
                messagebox.showerror("Ошибка", "Репозиторий не найден")
            else:
                messagebox.showerror("Ошибка", f"Ошибка HTTP: {e.code}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    app = GitHubApp()
    app.mainloop()