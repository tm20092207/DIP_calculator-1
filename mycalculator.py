import tkinter as tk

class mycalculator:
    def __init__(self):

      self.root = tk.Tk()

      self.root.geometry ("300x380")
      self.root.title("mycalculator")

      self.label = tk.Label(self.root, text="hello world!", font=('Arial', 18)) 
      self.label.pack()

      self.button = tk.Button(self.root, text="AC", height=3, width=7)
      self.button.place(x=20, y=50)
      self.button = tk.Button(self.root, text="7", height=3, width=7)
      self.button.place(x=20, y=110)
      self.button = tk.Button(self.root, text="4", height=3, width=7)
      self.button.place(x=20, y=170)
      self.button = tk.Button(self.root, text="1", height=3, width=7)
      self.button.place(x=20, y=230)
      self.button = tk.Button(self.root, text="0", height=3, width=16)
      self.button.place(x=20, y=290)
      self.button = tk.Button(self.root, text="+/-", height=3, width=7)
      self.button.place(x=85, y=50)
      self.button = tk.Button(self.root, text="8", height=3, width=7)
      self.button.place(x=85, y=110)
      self.button = tk.Button(self.root, text="5", height=3, width=7)
      self.button.place(x=85, y=170)
      self.button = tk.Button(self.root, text="2", height=3, width=7)
      self.button.place(x=85, y=230)
      self.button = tk.Button(self.root, text="%", height=3, width=7)
      self.button.place(x=150, y=50)
      self.button = tk.Button(self.root, text="9", height=3, width=7)
      self.button.place(x=150, y=110)
      self.button = tk.Button(self.root, text="6", height=3, width=7)
      self.button.place(x=150, y=170)
      self.button = tk.Button(self.root, text="3", height=3, width=7)
      self.button.place(x=150, y=230)
      self.button = tk.Button(self.root, text=".", height=3, width=7)
      self.button.place(x=150, y=290)
      self.button = tk.Button(self.root, text="/", height=3, width=7)
      self.button.place(x=215, y=50)
      self.button = tk.Button(self.root, text="*", height=3, width=7)
      self.button.place(x=215, y=110)
      self.button = tk.Button(self.root, text="-", height=3, width=7)
      self.button.place(x=215, y=170)
      self.button = tk.Button(self.root, text="+", height=3, width=7)
      self.button.place(x=215, y=230)
      self.button = tk.Button(self.root, text="=", height=3, width=7)
      self.button.place(x=215, y=290)
      self.button.bind("<Button-1>", self.trigger_event)


      self.root.mainloop()
    
    
    def trigger_event(self, event):
      print(event)


mycalculator()
