import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

entry = tk.Entry(root)
entry.grid(row=0, column=0)

# Stack to store operations
operations_stack = []
deleted_items = []  # Store the items deleted by "Delete All" operation

def addition():
    data = entry.get()
    list_box.insert(tk.END, data)
    index,value=list_boxlist_box.get()
    operations_stack.append(('add', data))  # Store the operation in the stack

def deleteitem():
    try:
        select_index = list_box.curselection()
        data = list_box.get(select_index[0])  # Get the deleted item for undo
        list_box.delete(select_index)
        operations_stack.append(('delete', data))  # Store the operation in the stack
    except IndexError:
        print('Select a Text first.')

def deleteitemall():
    global deleted_items
    deleted_items = list(list_box.get(0, tk.END))  # Store all items before deleting
    list_box.delete(0, tk.END)
    operations_stack.append(('deleteall', None))  # Store the operation in the stack

def undo():
    if operations_stack:
        operation, data = operations_stack.pop()
        if operation == 'add':
            list_box.delete(tk.END)  # Remove the last added item
        elif operation == 'delete':
            list_box.insert(tk.END, data)  # Add back the deleted item
        elif operation == 'deleteall':
            for item in deleted_items:
                list_box.insert(tk.END, item)  # Add back all deleted items

bt_add = tk.Button(root, text="Add Text", command=addition)
bt_add.grid(row=0, column=1)

list_box = tk.Listbox(root, width=28)
list_box.grid(row=2, column=0)

bt_delete = tk.Button(root, text="Delete Item", command=deleteitem)
bt_delete.grid(row=2, column=1)

bt_delete_all = tk.Button(root, text="Delete All", command=deleteitemall)
bt_delete_all.grid(row=3, column=1)

bt_undo = tk.Button(root, text="Undo", command=undo)
bt_undo.grid(row=4, column=1)

root.mainloop()
