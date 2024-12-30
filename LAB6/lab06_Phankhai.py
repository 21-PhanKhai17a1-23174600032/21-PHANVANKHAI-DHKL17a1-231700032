#  câu 1: Thiết kế giao diện
import tkinter as tk
from tkinter import messagebox

#  câu 2: Kết nối với cơ sở dữ liệu SQLite
import sqlite3

def connect_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

#  câu 3: Xử lý sự kiện
# Thêm sản phẩm
def add_product():
    name = entry_name.get()
    price = entry_price.get()
    if not name or not price:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin sản phẩm.")
        return
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, float(price)))
        conn.commit()
        conn.close()
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        load_products()
        messagebox.showinfo("Thành công", "Đã thêm sản phẩm thành công.")
    except ValueError:
        messagebox.showerror("Lỗi", "Giá sản phẩm phải là số.")

# Xóa sản phẩm
def delete_product():
    selected = listbox_products.curselection()
    if not selected:
        messagebox.showwarning("Chưa chọn sản phẩm", "Vui lòng chọn sản phẩm để xóa.")
        return
    product = listbox_products.get(selected[0])
    product_id = product.split(":")[0]
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    load_products()
    messagebox.showinfo("Thành công", "Đã xóa sản phẩm thành công.")

#  câu 4: Hiển thị và cập nhật dữ liệu
# Tải danh sách sản phẩm
def load_products():
    listbox_products.delete(0, tk.END)
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        listbox_products.insert(tk.END, f"{row[0]}: {row[1]} - {row[2]} VND")

# Giao diện chính
connect_db()
root = tk.Tk()
root.title("Quản lý sản phẩm")

# Widgets
label_name = tk.Label(root, text="Tên sản phẩm:")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_price = tk.Label(root, text="Giá sản phẩm:")
label_price.grid(row=1, column=0, padx=10, pady=10)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1, padx=10, pady=10)

button_add = tk.Button(root, text="Thêm sản phẩm", command=add_product)
button_add.grid(row=2, column=0, columnspan=2, pady=10)

listbox_products = tk.Listbox(root, width=50)
listbox_products.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

button_delete = tk.Button(root, text="Xóa sản phẩm", command=delete_product)
button_delete.grid(row=4, column=0, columnspan=2, pady=10)

# Load dữ liệu ban đầu
load_products()

# Chạy ứng dụng
root.mainloop()
# CÓ THAM KHẢO CHAT GPT NHỮNG PHẦN KHÓ HIỂU
