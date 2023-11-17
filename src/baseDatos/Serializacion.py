import pickle

def serializar(Restaurante):

    file=open("src/baseDatos/temp/Datos.pickle","wb")
    pickle.dump(Restaurante,file)
    file.close()

def deserializar():
    file=open("src/baseDatos/temp/Datos.pickle","rb")
    datos=pickle.load(file)
    return datos