import tkinter as tkfrom controlador
import ControladorUsuarios
def main():
  root = tk.Tk()    
  app = ControladorUsuarios(root)    
  root.mainloop()
  
if __name__ == "__main__":
  main()
