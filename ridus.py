# Función para cargar los datos
def cargar_datos(archivo, columnas, saltar_filas=1):
    
    try:
        df = pd.read_csv(archivo, delim_whitespace=True, skiprows=saltar_filas, names=columnas)
        return df
    except Exception as error:
        print(f"Error al cargar {archivo}: {error}")
        return None

def promedio(lista):
    
    x = sum(lista)
    prom = x / len(lista)
    return prom

def mediana(lista):
    
    lista = sorted(lista)
    n = len(lista)
    if n % 2 == 0:
        med1 = lista[(n // 2) - 1]
        med2 = lista[n // 2]
        media = promedio([med1, med2])
    else:
        media = lista[n // 2]
    return media

def moda(lista):
    
    from collections import Counter
    conteo = Counter(lista)
    max_frecuencia = max(conteo.values())
    moda = [key for key, val in conteo.items() if val == max_frecuencia]
    return moda

def rango(lista):

    return max(lista) - min(lista)

def varianza(lista):

    x = promedio(lista)
    varianza = sum((elem - x) ** 2 for elem in lista) / len(lista)
    return varianza

def desviacion_estandar(lista):
    
    var = varianza(lista)
    desviacion = var ** 0.5
    return desviacion

def rango_intercuartilico(lista):
    
    lista = sorted(lista)
    n = len(lista)
    if n % 2 == 0:
        Q1_index1 = n // 4
        Q1_index2 = Q1_index1 - 1
        Q3_index1 = (n * 3) // 4
        Q3_index2 = Q3_index1 - 1
        Q1 = (lista[Q1_index1] + lista[Q1_index2]) / 2
        Q3 = (lista[Q3_index1] + lista[Q3_index2]) / 2
    else:
        Q1_index = n // 4
        Q3_index = (n * 3) // 4
        Q1 = lista[Q1_index]
        Q3 = lista[Q3_index]
    IQR = Q3 - Q1
    return IQR

def MAD(lista):
    
    med = mediana(lista)
    desv_abs = [abs(elem - med) for elem in lista]
    mad = mediana(desv_abs)
    return mad

def covarianza(x, y):
    
    x_prom = promedio(x)
    y_prom = promedio(y)
    N = len(x)
    cov = sum((xi - x_prom) * (yi - y_prom) for xi, yi in zip(x, y)) / N
    return cov

def coeficiente_correlacion(x, y):
    
    covar = covarianza(x, y)
    varx = varianza(x)
    vary = varianza(y)
    r = covar / ((varx * 0.5) * (vary * 0.5))
    return r
