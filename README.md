Ejercicio 1
-----------
	El proyecto consiste en un archivo: Ejercicio_1.py
	Se han creado dos m�todos:
		- perfect:		dado un n�mero, determina si es perfecto, defectivo y abundante, mostrasdo una traza por pantalla indic�ndolo
		- perfect_list	dado una lista de n�meros, llama al m�todo perfect con cada uno de ellos.
		
	Se han a�adido unas l�neas "main" para probar los m�todos.
	

Ejercicio 2
-----------
	El proyecto consiste en un archivo: Ejercicio_2.html
	Se han creado los siguientes elementos:
		- class ClassNormalized: 	clase definida para almacenar los datos normalizados 
									de los ficheros json.
		- class ClassData: 			clase para almacenar los datos acumulados por fecha.
		- function formatJSON_1: 	funci�n que normaliza los datos del archivo json 1.
		- function formatJSON_2: 	funci�n que normaliza los datos del archivo json 2.
		- function formatJSON_3: 	funci�n que normaliza los datos del archivo json 3.
		- function insertionSort: 	funci�n que ordena la lista de tipo ClassData (date y value)
		- function getCategories: 	clasifica los elementos por categor�a.
		- function accumulateByDate:para las listas clasificadas por categor�a,
									se agrupan los elementos por fecha, sumando los valores.
		- function accumulateByCategory: se agrupan los elementos por categor�a, sumando todos
									los valores independientemente de la fecha.
		- function drawLineChart:	dibuja el gr�fico lineal.
		- function drawPieChart:	dibuja el gr�fico circular.
		

	El flujo del proceso es el siguiente:
		- Obtiene los valores de cada una de las fuentes.
		- Parsea los valores obtenidos y crea tres arrays de objetos, uno por fuente.
		- Normaliza los tres arrays, seg�n el formato:
									- categor�a: CAT n
									- Fecha: YYYY-MM-DD
									- Valor
		- Clasifica los elementos normalizados por categor�as,
			reparti�ndolos en tantas listas como categor�as.
		- Ordena las listas categorizadas por fecha.
		- Las listas ordenadas se agrupan por fecha, sumando los valores en los que la fecha coincide.
		- Las listas ordenadas se agrupan por cateor�a, sumando todos los valores.
		- Dibuja la gr�fica lineal.
		- Dibuja la gr�fica circular.
		
		
IMPORTANTE
----------
	Notas sobre el ejercicio 2:
		Debido a un problema de conectividad, he optado por embeber los datos fuente.
		He considerado esta opci�n para poder subir una versi�n funcional,
		ya que considero este "GET" la parte menos importante del ejercicio.
		En cuanto resuelva este problema subir� la funcionalidad final.
	
		