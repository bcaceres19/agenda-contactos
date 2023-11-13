from tkinter import ttk


class Tabla(ttk.Treeview):
    def __init__(self, master, informacion, cabecera,**kwargs):
        super().__init__(master,**kwargs)
        style = ttk.Style()
        style.configure("Treeview", font=("Mullish",13))
        if cabecera:
            self.configure(show="headings", columns=cabecera,height=15)
            self.cabecera(informacion)
            self.grid(row=1, column=1, sticky="ew")
        else:
            self.contenido(informacion)

    def cabecera(self, informacion):
        for i in informacion:
            self.heading(i.get("id"), text=i.get("texto"))
            self.column(i.get("id"), anchor="center",width=300)

    def contenido(self, informacion):
        self.insert(parent='', index=0, values=informacion)