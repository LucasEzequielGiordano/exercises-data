import os
import shutil
def copy(nombre):
    repeticion = 1
    repeticion += 1

    while os.path.exists(f"copia{str(repeticion)}-{nombre}"):
        repeticion += 1

    shutil.copyfile(nombre, f"copia{str(repeticion)}-{nombre}")

copy('Datos.xlsx')