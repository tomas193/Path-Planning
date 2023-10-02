# imports every file form tkinter and tkinter.ttk
from tkinter import *
from time import sleep
class Punto:
    def __init__(self, y, x, index):
        self.visitado = False
        self.list = [x,y]
        self.flag = False
        self.x = x
        self.y = y
        self.tx = (x*50)-50
        self.ty = ((10-y)*50)-50

    def check_clockwise(self, Q, W, gfg):
        up =  [self.x, self.y+1]
        right = [self.x+1, self.y]
        down = [self.x, self.y-1]
        left = [self.x-1, self.y]
        if up[1] <= 10:
            if W[get_index(up)].visitado == False:
                #print(f'Debido a que {W[get_index(up)].list} ha sido == {W[get_index(up)].visitado}, pasara a True')
                W[get_index(up)].visitado = True
                Q.append(W[get_index(up)])
                gfg.create_cross(W[get_index(up)].x, W[get_index(up)].y)
        if right[0] <= 10:
            if W[get_index(right)].visitado == False:
                #print(f'Debido a que {W[get_index(right)].list} ha sido == {W[get_index(right)].visitado}, pasara a True')
                W[get_index(right)].visitado = True
                Q.append(W[get_index(right)])
                gfg.create_cross(W[get_index(right)].x, W[get_index(right)].y)

        if down[1] >= 0:
            if W[get_index(down)].visitado == False:
                #print(f'Debido a que {W[get_index(down)].list} ha sido == {W[get_index(down)].visitado}, pasara a True')
                W[get_index(down)].visitado = True
                Q.append(W[get_index(down)])
                gfg.create_cross(W[get_index(down)].x, W[get_index(down)].y)

        if left[0] >= 0:
            if W[get_index(left)].visitado == False:
                #print(f'Debido a que {W[get_index(left)].list} ha sido == {W[get_index(left)].visitado}, pasara a True')
                W[get_index(left)].visitado = True
                Q.append(W[get_index(left)])
                gfg.create_cross(W[get_index(left)].x, W[get_index(left)].y)

        return Q, W

class GFG:
    def __init__(self, master=None):
        self.master = master
        self.canvas = Canvas(master, width=500, height=500, bg='cyan')
        self.photoimage = PhotoImage(file='C:/Users/harri/Documents/SEMESTRE 5/Diseño de Algoritmos/P2/r5.png')  # Se crea la imagen que recorrera la cuadricula, siendo asignada a un png dentro del proyecto
        self.robot = self.canvas.create_image(-25, 450, image=self.photoimage, anchor=NW)
        # to take care movement in x direction
        self.opcion = int(input('\nDigite 1 para modo manual; 2 para modo autónomo: '))
        if self.opcion == 1:
            self.resolucion = float(input('Digite el tipo de resolucion; 1.0, 0.5, 0.25, 0.125: '))
            self.movimientos = int(input('Digite 1 para vecindad de Von Neumann, 2 para vecindad de Moore: '))

        else:
            self.resolucion = 1
            self.algorithm = int(input('Digite 1: algoritmo primero amplitud; 2: algoritmo primero profundidad: '))
            W = []
            Q = []
            x_i = input('Ingrese coordenadas del estado inicial (x,y): ').split(',')
            X_G = input('Ingrese coordenadas del estado meta (x,y): ').split(',')

            xi = [int(x_i[0]), int(x_i[1])]
            XG = [int(X_G[0]), int(X_G[1])]
            index_xi = get_index(xi)
            index_XG = get_index(XG)

            #print(index_xi, index_XG)
            for i in range(11):
                for j in range(11):
                    index = j + (i * 10 + i)
                    p = Punto(i, j, index)
                    # print(index, p.list)

                    W.append(p)
            if self.algorithm == 1:
                R = BFS(W[index_xi], W[index_XG], W, Q, self)
            else:
                R = DFS(W[index_xi], W[index_XG], W, Q, self)

            count = 0
            for i in W:
                if i.visitado == True:
                    # print(f'estado = {i.list}, index = {get_index(i.list)}, visitado = {i.visitado}, cuenta = {count}')
                    count += 1
            print(f'El numero de estados visitados es: {count}')
        # canvas object to create shape
        self.canvas.pack()

    def movement(self, event):  # Funcion para mover la imagen que se deseara utilizar más a delante
        w, h = 500, 500  # Se establecen w,h como las dimensiones de la ventana que se abrira al ejecutar el programa
        x, y = self.canvas.coords(self.robot)
        if self.opcion == 1:
            if self.movimientos == 2:
                if event.keysym == 'q':
                    if y > -50 and x > -50:
                        self.canvas.move(self.robot, (-50*self.resolucion), (-50 * self.resolucion))  # se mueve en adecuarlo al espacio de 500x500
                elif event.keysym == 'w':
                    if y > -50 and x + 50 < w:
                        self.canvas.move(self.robot, (50*self.resolucion), (-50 * self.resolucion))
                elif event.keysym == 'a':
                    if x > -50 and y + 50 < h:  # Se elije -50 en lugar de 0 devido a que s desea estar en la esquina del espacio de trabajo
                        self.canvas.move(self.robot, (-50 * self.resolucion), (50*self.resolucion))
                elif event.keysym == 's':
                    if x + 50 < w and y + 50 < h:
                        self.canvas.move(self.robot, (50 * self.resolucion), (50*self.resolucion))

            if event.keysym == 'Up':
                if y > -50:
                    self.canvas.move(self.robot, 0, (-50*self.resolucion))  # se mueve en adecuarlo al espacio de 500x500
            elif event.keysym == 'Down':
                if y + 50 < h:
                    self.canvas.move(self.robot, 0, (50*self.resolucion))
            elif event.keysym == 'Left':
                if x > -50:  # Se elije -50 en lugar de 0 devido a que s desea estar en la esquina del espacio de trabajo
                    self.canvas.move(self.robot, (-50*self.resolucion), 0)
            elif event.keysym == 'Right':
                if x + 50 < w:
                    self.canvas.move(self.robot, (50*self.resolucion), 0)

    def create_grid(self, event=None):  # Funcion para crear la cuadricula en el fondo de la ventanda, basada en: https://stackoverflow.com/questions/34006302/how-to-create-a-grid-on-tkinter-in-python
        h = self.canvas.winfo_height()  # Se obtienen la altura y base de la ventana con sus funciones respectivas
        w = self.canvas.winfo_width()
        self.canvas.delete('linea_de_cuadricula')  # Borrara las lineas de la cuadricula

        # Se recorrera toda la ventana creando todas las  lineas verticales en intervalos de 50
        for i in range(0, w, int(50 * self.resolucion)):
            self.canvas.create_line([(i, 0), (i, h)], tag='linea_de_cuadricula')

        # Se recorrera toda la ventana creando todas las  lineas verticales en intervalos de 50
        for i in range(0, h, int(50 * self.resolucion)):
            self.canvas.create_line([(0, i), (w, i)], tag='linea_de_cuadricula')

    def create_cross(self, x, y, color = "black", event = None):
        x = (x*50)-7.5
        y = 500-(y*50)-7.5
        #print(x, y)
        self.canvas.create_text(x, y, fill=color,font="Times 15    ",text="X", anchor=NW)

def BFS(xi, XG, W, Q, gfg):
    gfg.create_cross(xi.x,xi.y, 'green')
    x = xi
    gfg.canvas.moveto(gfg.robot, x.tx, x.ty )
    Q.append(x)
    x.visitado = True
    while len(Q) != 0:
        #print(x.list)
        if x.list == XG.list:
            gfg.create_cross(XG.x, XG.y, 'red')
            return len(Q), 'SUCCESS', Q
        Q, W = x.check_clockwise(Q, W, gfg)
        Q.pop(0)
        x = Q[0]
        gfg.canvas.moveto(gfg.robot, x.tx, x.ty)

def DFS(xi, XG, W, Q, gfg):
    gfg.create_cross(xi.x,xi.y, 'green')
    x = xi
    gfg.canvas.moveto(gfg.robot, x.tx, x.ty )
    Q.append(x)
    x.visitado = True
    while len(Q) != 0:
        #print(x.list)
        if x.list == XG.list:
            gfg.create_cross(XG.x, XG.y, 'red')
            return len(Q), 'SUCCESS', Q
        Q, W = x.check_clockwise(Q, W, gfg)
        Q.remove(x)
        x = Q[len(Q)-1]
        gfg.canvas.moveto(gfg.robot, x.tx, x.ty)
        sleep(0.1)

def get_index(list):
    index = (11*list[1]) + list[0]

    return index

if __name__ == "__main__":

    # object of class Tk, responsible for creating
    # a tkinter toplevel window
    master = Tk()
    master.title('Práctica #3')  # Se pone un titulo a la ventana

    gfg = GFG(master)

    master.bind('<Configure>', gfg.create_grid)  # Se llama la función para crear la cuadricula

    master.bind("<q>", gfg.movement)
    master.bind("<w>", gfg.movement)
    master.bind("<a>", gfg.movement)
    master.bind("<s>", gfg.movement)
    master.bind("<Up>",gfg.movement)
    master.bind("<Down>",gfg.movement)
    master.bind("<Left>", gfg.movement)
    master.bind("<Right>", gfg.movement)
    # Infinite loop breaks only by interrupt
    mainloop()

