class Cliente:
    def __init__(self,numcliente,nombre,saldo):
        self.numcliente=numcliente
        self.nombre=nombre
        self.saldo=saldo



if __name__ == '__main__':
    cliente=Cliente("Ángel",1000)
    o=0
    while o!=4:
        print("Que quieres hacer")
        print("1.Cargar datos del cliente")
        print("2.consultar cuenta (depositar e ingresar)")
        o=int(input("Introduce la opción"))
        if o==1:
            print("Cargando datos del cliente\n")
            print()
