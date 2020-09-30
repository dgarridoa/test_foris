# Ordenamiento de estudiantes

El presente trabajo consiste en ordenar una lista de estudiantes acorde al total de minutos presentes en clases de mayor a menor.

## A. Dependencias

Para el desarrollo del proyecto se utilizó Python 3 junto a <a href="https://numpy.org/">NumPy</a>, una librería científica optimizada para operaciones con arrays.

```
python==3.7.4
numpy==1.17.2
```

Con <a href="https://www.anaconda.com/">Anaconda</a> es bastante sencillo crear un entorno para la ejecución del código, por ejemplo:

```
conda create --name foris_test --file requirements.txt -c conda-forge
```

## B. Contenido

El contenido del proyecto se encuentra en la carpeta **src/**. A continuación se detalla:

- **report.py**: código que genera el reporte con los estudiantes ordenados en orden descente por minutos totales acumulados. Posee tres funciones:
    - **minutes**: función útil para llevar un string de la forma "HH:MM" a minutos (int).
    - **load_data**: esta función carga los datos especificados en el argumento `path` de la función y retorna un diccionario. Las llaves del diccionario son los nombres de los alumnos, cada alumno esta asociado una lista de listas que almacena el día y el delta tiempo en minutos (que puede ser vacía si no registra asistencias).  Ejemplo: `{"diego": [[1, 60], [1, 30], [2, 120], ...}`. Adicionalmente, esta función posee dos execepciones en el caso de que el formato del archivo de entrada no sea el adecuado. Estas son:
        - Si se llama al comando `Presence` sin haber creado previamente al estudiante por el comando `Student Nombre`, siendo el mensaje `Student Nombre doesn't exist`.
        - Si hay una linea que comienza sin el comando `Student` o `Presence` entrega una mensaje de error `ValueError: No command given`.
    - **build_report**: esta función construye el reporte a partir del diccionario que retorna la función anterior. Esta función usa la librería `numpy`.
        
        En primer lugar, la función crea un array de ceros con `numpy` de dimensión `Nx3`, donde la primera columna recibirá los `ids` de los estudiantes, la segunda el tiempo total en minutos y la tercera la cantidad de días únicos.

        En segundo lugar, la función recorre el diccionario por `load_data`, luego transforma la lista de lista a un `numpy array`, esto facilita el calculo del tiempo total a través del método `np.sum` y la cantidad de días únicos que ha estado presente a través del método `np.unique`. Los valores calculados van siendo ingresados en la matriz de ceros junto al id del estudiante. En caso de que un estudiante no registra presencias se rellena con cero la columna de minutos totales y días.

        En tercer lugar, se realiza un quicksort sobre el array. Para realizar el quicksort se selecciona la columna que registra los minutos totales y se le aplica un `argsort()`, esto entrega un array con los ids de los estudiantes ordenadas por tiempo total en forma ascendente, luego se usan estos índices para reordenar el array completo a través de indexación, para finalmente revertir el orden con `[::-1]` y así obtener un orden descendiente.

        Por último, se crea una lista de strings, estos string son formateados por los inputs generados en la etapa previa, teniendo en consideraicón que los estudiantes que no registran presencia reciben otro string. Luego con `\n.join(...)` se lleva la lista a un string con saltos de líneas, de esta manera el print resulta más estético.

- **instance_generator.py**: archivo con función `random_generator` que sirve para generar instancias aleatorías. Esta función usa la librería `numpy`. Recibe tres argumentos:
    - `size = (s,c,n)`: que especifica la cantidad de estudiantes (`s`), salas (`c`) y presencias (`n`) a generar.
    - `seed`: semilla aleatoria, tiene por objetivo replicar resultados.
    - `path`: ruta donde se guardará la instancia.  
- **instances/**: carpeta con instancias generadas por la función `random_generator`.
    - **instance01.txt**: `random_generator((3,3,10), "instances/instance01.txt")`
    - **instance02.txt**: `random_generator((10,10,100), "instances/instance02.txt")`
    - **instance03.txt**: `random_generator((50,50,1000), "instances/instance03.txt")`
    - **instance04.txt**: `random_generator((5000,100,100000), "instances/instance04.txt")`
    - **instance05.txt**: instancia con estudiante sin presencias (`dhjtvse:  0 minutes`)
    - **instance06.txt**: instancia con excepción `NameError: Student pvad doesn't exist`
    - **instance07.txt**: instancia con excepción `ValueError: No command given`

## C. Uso

```bash
python main.py <input_file>
```
Por ejemplo:
```bash
python main.py instances/instance01.txt
>>>
pvad: 3174 minutes in 4 days
dhjtvse: 1161 minutes in 3 days
gyymbgh: 451 minutes in 2 days

python main.py instances/instance04.txt
>>>
aydkrd: 16664 minutes in 6 days
rvxfun: 15973 minutes in 6 days
qdqf: 15489 minutes in 6 days
...
```