# geospatial-project

![Spot](/images/spot.png)

Este es un proyecto que lo he realizado durante el Bootcamp de Data Anatlytics en [Ironhack](https://www.ironhack.com/es/data-analytics) Madrid.

# Obejtivo

El objetivo de este proyecto es determinar la ubicación perfecta de una compañía de videojuegos en base a unos criterios:

- Los Account managers viajan mucho.
- El 30% de los empleados de la compañía tiene al menos un hijo/a.
- La edad de los trabajadores está entre 25 y 40 años.
- A los ejecutivos les gusta mucho la cadena de cafés "Starbucks".
- La CEO de la compañía es vegana.

# Proceso

Para conseguir mi objtivo, comienzo con un dataset de [Crunchbase] (https://www.crunchbase.com/) que contiene información de mas de 18000 compañias. 

Los países con más empresas de videojuegos en 2019 son Estados Unidos, Reino Unido y Francia. El top 10 lo completa Finlandia. 

En 2008 realizé mi Erasmus en Finlandia y por eso he decidido localizar mi empresa en Helsinki.

1. Filtro siguiendo unos criterios y consigo ubicar mi empresa;
   -     País; Finlandia
   -     Oficina; Helsinki
   -     Fundada; Después del año 2000
   -     Numero de empleados; menos de 100
   -     Categoría; Videojuegos    

2. Una vez que tengo la ubicación de mi empresa, continuo haciendo llamadas a la API de Foursquare para conseguir los criterios anteriormente citados;
    -   Aeropuerto
    -   Guarderías
    -   Discotecas
    -   Starbucks
    -   Restaurantes veganos
Con el resultado de las llamadas, calculo la ubicacíon del más cercano a mi oficina.

3. Finalmente, con los 5 puntos de las ubicaciones extraidas, creo un mapa con Folium.

# Resultado 

![Helsinki](/images/helsinki.png)

# Referencias

[Crunchbase](https://data.crunchbase.com/docs)
[Fursquare API](https://developer.foursquare.com/)
[Número de empresas de videojuegos en el mundo, 2019](https://es.statista.com/estadisticas/714837/empresas-de-las-principales-industrias-del-videojuego-del-mundo/)
[Visit Finland](https://www.visitfinland.com/es/helsinki/)


![Moomin](/images/moomin.png)
