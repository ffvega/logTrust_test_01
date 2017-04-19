Ejercicio 1
-----------
	El proyecto consiste en un archivo: Ejercicio_1.py
	Se han creado dos métodos:
		- perfect:		dado un número, determina si es perfecto, defectivo y abundante, mostrasdo una traza por pantalla indicándolo
		- perfect_list	dado una lista de números, llama al método perfect con cada uno de ellos.
		
	Se han añadido unas líneas "main" para probar los métodos.
	

Ejercicio 2
-----------
	El proyecto consiste en un archivo: Ejercicio_2.html
	Se han creado los siguientes elementos:
		- class ClassNormalized: 	clase definida para almacenar los datos normalizados 
									de los ficheros json.
		- class ClassData: 			clase para almacenar los datos acumulados por fecha.
		- function formatJSON_1: 	función que normaliza los datos del archivo json 1.
		- function formatJSON_2: 	función que normaliza los datos del archivo json 2.
		- function formatJSON_3: 	función que normaliza los datos del archivo json 3.
		- function insertionSort: 	función que ordena la lista de tipo ClassData (date y value)
		- function getCategories: 	clasifica los elementos por categoría.
		- function accumulateByDate:para las listas clasificadas por categoría,
									se agrupan los elementos por fecha, sumando los valores.
		- function accumulateByCategory: se agrupan los elementos por categoría, sumando todos
									los valores independientemente de la fecha.
		- function drawLineChart:	dibuja el gráfico lineal.
		- function drawPieChart:	dibuja el gráfico circular.
		

	El flujo del proceso es el siguiente:
		- Obtiene los valores de cada una de las fuentes.
		- Parsea los valores obtenidos y crea tres arrays de objetos, uno por fuente.
		- Normaliza los tres arrays, según el formato:
									- categoría: CAT n
									- Fecha: YYYY-MM-DD
									- Valor
		- Clasifica los elementos normalizados por categorías,
			repartiéndolos en tantas listas como categorías.
		- Ordena las listas categorizadas por fecha.
		- Las listas ordenadas se agrupan por fecha, sumando los valores en los que la fecha coincide.
		- Las listas ordenadas se agrupan por cateoría, sumando todos los valores.
		- Dibuja la gráfica lineal.
		- Dibuja la gráfica circular.
		
		
IMPORTANTE
----------
	Notas sobre el ejercicio 2:
		Debido a un problema de conectividad, he optado por embeber los datos fuente.
		He considerado esta opción para poder subir una versión funcional,
		ya que considero este "GET" la parte menos importante del ejercicio.
		En cuanto resuelva este problema subiré la funcionalidad final.
	
		