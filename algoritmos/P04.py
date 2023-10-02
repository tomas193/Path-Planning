from tkinter import *
from time import sleep
import csv

map1=[]
map2=[]
map3=[]
map4=[]
mapas=[]
np=[]#lista de estados no permitidos
with open('map01.csv', 'r') as csv_file:
    reader0 = csv.reader(csv_file)
    for row in reader0:
        map1.append(row)
    mapas.append(map1)
with open('map02.csv', 'r') as csv_file:
    reader1 = csv.reader(csv_file)
    for row in reader1:
        map2.append(row)
    mapas.append(map2)
with open('map03.csv', 'r') as csv_file:
    reader2 = csv.reader(csv_file)
    for row in reader2:
        map3.append(row)
    mapas.append(map3)
with open('map04.csv', 'r') as csv_file:
    reader3 = csv.reader(csv_file)
    for row in reader3:
        map4.append(row)
    mapas.append(map4)

mapa=int(input('\nEscoja un mapa: '))

for a in range(0,len(mapas[mapa-1])):
    var0=float(mapas[mapa-1][a][0])
    var1=float(mapas[mapa-1][a][1])
    var2=float(mapas[mapa-1][a][2])
    var3=float(mapas[mapa-1][a][3])
    for b in range(0,int(var2)+1):
        for c in range(0,int(var3)+1):
            punto=[]
            x=int(var0)+b
            y=int(var1)+c
            punto.append(x)
            punto.append(y)
            np.append(punto)

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
        self.photoimage = PhotoImage(file='r5.png')  # Se crea la imagen que recorrera la cuadricula, siendo asignada a un png dentro del proyecto
        self.robot = self.canvas.create_image(-25, 450, image=self.photoimage, anchor=NW)
        # to take care movement in x direction
        self.opcion = 2
        self.resolucion = float(input('Digite el tipo de resolucion; 1.0, 0.5, 0.25, 0.125: '))
        self.algorithm = 1
        W = []
        Q = []
        x_i = input('Ingrese coordenadas del estado inicial (x,y): ').split(',')
        X_G = input('Ingrese coordenadas del estado meta (x,y): ').split(',')
        xi = [int(x_i[0]), int(x_i[1])]
        XG = [int(X_G[0]), int(X_G[1])]
        index_xi = get_index(xi)
        index_XG = get_index(XG)

        for i in range(11):
            for j in range(11):
                index = j + (i * 10 + i)
                p = Punto(i, j, index)
                    # print(index, p.list)

                W.append(p)
        if self.algorithm == 1:
            R = BFS(W[index_xi], W[index_XG], W, Q, self)

        count = 0
        for i in W:
            if i.visitado == True:
                # print(f'estado = {i.list}, index = {get_index(i.list)}, visitado = {i.visitado}, cuenta = {count}')
                count += 1
        print(f'El numero de estados visitados es: {count}')
        # canvas object to create shape
        self.canvas.pack()

    def movement(self, event):  # Funcion para realizar movimientos en el algoritmo
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

        for k in range(0,len(mapas[mapa-1])):
            var0=float(mapas[mapa-1][k][0])
            var1=float(mapas[mapa-1][k][1])
            var2=float(mapas[mapa-1][k][2])
            var3=float(mapas[mapa-1][k][3])
            rec=[(int(var0)*50),500-((int(var1)+int(var3))*50),((int(var0)+int(var2))*50),500-(int(var1)*50)] 
            self.canvas.create_rectangle(rec[0],rec[1],rec[2],rec[3], fill='red') #(xinicial,yinicial, xfinal,yfinal)
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
        self.canvas.create_text(x, y, fill=color,font="Times 15",text="X", anchor=NW)

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