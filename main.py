import tkinter as tk

class mycalculator:
    def __init__(self):

      self.root = tk.Tk()

      self.root.geometry ("300x300")
      self.root.title("mycalculator")

      self.label = tk.Label(self.root, text="hello world!", font=('Arial', 18)) 
      self.label.pack()

      self.button = tk.Button(self.root, text="1", height=5, width=5)
      self.button.place(x=20, y=50)
      self.button = tk.Button(self.root, text="2", height=5, width=5)
      self.button.place(x=90, y=50)
      self.button = tk.Button(self.root, text="3", height=5, width=5)
      self.button.place(x=160, y=50)
      self.button = tk.Button(self.root, text="4", height=5, width=5)
      self.button.place(x=20, y=120)
      self.button = tk.Button(self.root, text="5", height=5, width=5)
      self.button.place(x=90, y=120)
      self.button = tk.Button(self.root, text="6", height=5, width=5)
      self.button.place(x=160, y=120)
      self.button = tk.Button(self.root, text="7", height=5, width=5)
      self.button.place(x=20, y=190)
      self.button = tk.Button(self.root, text="8", height=5, width=5)
      self.button.place(x=90, y=190)
      self.button = tk.Button(self.root, text="9", height=5, width=5)
      self.button.place(x=160, y=1900)




      self.root.mainloop()

mycalculator()