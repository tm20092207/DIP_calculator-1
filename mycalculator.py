import tkinter as tk

class mycalculator:
    def __init__(self):

      self.root = tk.Tk()
      self.display = tk.StringVar()

      self.root.geometry ("300x380")
      self.root.title("mycalculator")

      self.label = tk.Label(self.root, textvariable=self.display, font=('Arial', 18)) 
      self.label.pack()

      self.button = tk.Button(self.root, text="AC", height=3, width=7)
      self.button.place(x=20, y=50)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="7", height=3, width=7)
      self.button.place(x=20, y=110)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="4", height=3, width=7)
      self.button.place(x=20, y=170)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="1", height=3, width=7)
      self.button.place(x=20, y=230)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="0", height=3, width=16)
      self.button.place(x=20, y=290)
      self.button.bind("<Button-1>", self.action_0)
      self.button = tk.Button(self.root, text="+/-", height=3, width=7)
      self.button.place(x=85, y=50)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="8", height=3, width=7)
      self.button.place(x=85, y=110)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="5", height=3, width=7)
      self.button.place(x=85, y=170)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="2", height=3, width=7)
      self.button.place(x=85, y=230)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="%", height=3, width=7)
      self.button.place(x=150, y=50)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="9", height=3, width=7)
      self.button.place(x=150, y=110)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="6", height=3, width=7)
      self.button.place(x=150, y=170)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="3", height=3, width=7)
      self.button.place(x=150, y=230)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text=".", height=3, width=7)
      self.button.place(x=150, y=290)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="/", height=3, width=7)
      self.button.place(x=215, y=50)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="*", height=3, width=7)
      self.button.place(x=215, y=110)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="-", height=3, width=7)
      self.button.place(x=215, y=170)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="+", height=3, width=7)
      self.button.place(x=215, y=230)
      self.button.bind("<Button-1>", self.trigger_event)
      self.button = tk.Button(self.root, text="=", height=3, width=7)
      self.button.place(x=215, y=290)
      self.button.bind("<Button-1>", self.trigger_event)


      self.root.mainloop()
    
    
    def action_00(self, event):
      self.display.set("=")
      print(event)
    def action_0(self, event):
      self.display.set("0")
      print(event)
    def trigger_event(self, event):
      self.display.set("1")
      print(event)
    def trigger_event(self, event):
      self.display.set("2")
      print(event)
    def trigger_event(self, event):
      self.display.set("3")
      print(event)
    def trigger_event(self, event):
      self.display.set("4")
      print(event)
    def trigger_event(self, event):
      self.display.set("5")
      print(event)
    def trigger_event(self, event):
      self.display.set("6")
      print(event)
    def trigger_event(self, event):
      self.display.set("7")
      print(event)
    def trigger_event(self, event):
      self.display.set("8")
      print(event)
    def trigger_event(self, event):
      self.display.set("9")
      print(event)
      

mycalculator()
