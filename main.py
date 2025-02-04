from tkinter import Tk, Listbox, Entry, Button, Label, END
from datetime import datetime

def add_task(task_list, task_entry, date_entry):
    """إضافة مهمة جديدة إلى القائمة مع التاريخ"""
    task = task_entry.get()
    date = date_entry.get()
    if task and date:
        task_list.insert(END, f"{date}: {task}")
        task_entry.delete(0, END)
        date_entry.delete(0, END)

def remove_task(task_list):
    """إزالة المهمة المحددة من القائمة"""
    try:
        selected_index = task_list.curselection()[0]
        task_list.delete(selected_index)
    except IndexError:
        pass  # لا يوجد عنصر محدد

def mark_done(task_list):
    """وضع علامة (تم) على المهمة المحددة"""
    try:
        selected_index = task_list.curselection()[0]
        task = task_list.get(selected_index)
        task_list.delete(selected_index)
        task_list.insert(END, f"✔ {task}")
    except IndexError:
        pass

# إنشاء النافذة الرئيسية
root = Tk()
root.title("مدير المهام اليومية")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

# عنوان التطبيق
Label(root, text="📅 قائمة المهام اليومية", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

# إدخال التاريخ
Label(root, text="التاريخ (YYYY-MM-DD):", bg="#f0f0f0").pack()
date_entry = Entry(root, width=50)
date_entry.pack()
date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

# إدخال المهمة
Label(root, text="المهمة:", bg="#f0f0f0").pack()
task_entry = Entry(root, width=50)
task_entry.pack()

# قائمة المهام
task_list = Listbox(root, width=50, height=10)
task_list.pack(pady=10)

# أزرار التحكم
Button(root, text="إضافة", command=lambda: add_task(task_list, task_entry, date_entry), bg="#4CAF50", fg="white").pack(pady=2)
Button(root, text="حذف", command=lambda: remove_task(task_list), bg="#F44336", fg="white").pack(pady=2)
Button(root, text="تم", command=lambda: mark_done(task_list), bg="#2196F3", fg="white").pack(pady=2)

# تشغيل التطبيق
root.mainloop()
