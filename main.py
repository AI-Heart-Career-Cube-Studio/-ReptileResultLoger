from tkinter import Button

import tkinter as tk

information = None
name = None
password = None
database = None

def jsonToSQL():
    global information
    read_json(information.get())

def fill(root):
    import read_json
    global information
    tk.Label(root,text="输入数据信息",font=(20)).pack(fill=tk.X)
    information = tk.Entry(root,font=(20))
    information.pack(fill=tk.X)
    tk.Button(root,text="录入框中json文件",font=(20),command=jsonToSQL).pack(fill=tk.X)

def login(root):
    def link_to ():
        import write_in_sql
        write_in_sql.user = username.get()
        write_in_sql.password = password.get()
        write_in_sql.db = baseName.get()
        for w in root.winfo_children():
            w.destroy()
        fill(root)
    tk.Label(root,text="输入用户名").pack(fill=tk.X)
    username = tk.Entry(root,font=(20))
    username.pack(fill=tk.X)
    tk.Label(root,text="输入密码").pack(fill=tk.X)
    password = tk.Entry(root,show="*",font=(20))
    password.pack(fill=tk.X)
    tk.Label(root,text="输入数据库名称").pack(fill=tk.X)
    baseName = tk.Entry(root,font=(20))
    baseName.pack(fill=tk.X)
    tk.Button(root,text="登入",command=link_to).pack(fill=tk.X)
    

def main():

    root = tk.Tk()

    icon = tk.PhotoImage(file="icon.png")

    root.title("TYPE")
    root.resizable(False, False)

    root.iconphoto(True,icon)

    login(root)
    root.mainloop()

if __name__ == '__main__':
    main()