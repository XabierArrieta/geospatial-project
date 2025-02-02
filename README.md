# geospatial-project



![Spot](/images/spot.png)

Este es un proyecto que lo he realizado durante el Bootcamp de Data Anatlytics en [Ironhack](https://www.ironhack.com/es/data-analytics) Madrid.

# Objetivo

El **objetivo** de este proyecto es *determinar la ubicación perfecta de una compañía de videojuegos* en base a unos criterios:

- Los Account managers viajan mucho.
- El 30% de los empleados de la compañía tiene al menos un hijo/a.
- La edad de los trabajadores está entre 25 y 40 años.
- A los ejecutivos les gusta mucho la cadena de cafés "Starbucks".
- La CEO de la compañía es vegana.

# Proceso

Para conseguir mi objtivo, comienzo con un dataset de [Crunchbase] (https://www.crunchbase.com/) que contiene información de mas de 18000 compañias. 

Los países con más empresas de videojuegos en 2019 son Estados Unidos, Reino Unido y Francia. El top 10 lo completa Finlandia. 

En 2008 realizé mi Erasmus en Finlandia y por eso he decidido localizar mi empresa en Helsinki.

1. Filtro con [Mongodb](https://www.mongodb.com/3) siguiendo los siguientes criterios y así ubicar mi empresa (notebooks>01.Filtro_empresa.ipynb);
   - País: Finlandia
   - Oficina: Helsinki
   - Fundada: Después del año 2000
   - Numero de empleados: menos de 100
   - Categoría: Videojuegos    

2. Una vez que tengo la ubicación de mi empresa, continuo haciendo llamadas a la [API de Foursquare](https://api.foursquare.com/v2/venues/explore) para conseguir los criterios anteriormente citados, y busc0 (notebooks>002.API_Foursquare.ipynb);
    -   Aeropuerto
    -   Guarderías
    -   Discotecas
    -   Starbucks
    -   Restaurantes veganos

    Con el resultado de las llamadas, calculo la ubicacíon del punto más cercano a mi oficina.

3. Finalmente, con los 5 puntos de las ubicaciones extraídas, creo un mapa con Folium(notebooks>03.Mapa.ipynb).
   
   Entrando en la carpeta **"notebooks"** prodrás encontrar todo el proceso.

   Las *librerías* utilizadas son: requests, json, pandas, reduce, geopandas, pymongo.


# Resultado

El **aeropuerto** más cercano es:

    Helsinki Airport (HEL) (Helsinki-Vantaan lentoasema)
         
    Distancia: 19,5km
    Latitud: 60.319129
    Longitud: 24.968297

La **guarderia** más cercana es:

    Daghemmet B. E. Von Schantz

    Distancia: 2,5km
    Latitud: 60.158121
    Longitud: 24.936681

La **discoteca** más cercana es:

    Haven

    Distancia: 1,7km
    Latitud: 60.16654471941996
    Longitud: 24.9513536704468

El **Starbucks** más cercano es:

    Starbucks

    Distancia: 500m
    Latitud: 60.167737
    Longitud: 24.943369

El **restaurante vegano** más cercano es:

    Pontus

    Distancia: 1,5km
    Latitud: 60.1587920757416
    Longitud: 24.94628194859813


![Helsinki](/images/helsinki.png)

# Referencias

* [Crunchbase](https://data.crunchbase.com/docs)
* [Mongodb](https://www.mongodb.com/3)
* [Fursquare API](https://developer.foursquare.com/)
* [Número de empresas de videojuegos en el mundo en 2019](https://es.statista.com/estadisticas/714837/empresas-de-las-principales-industrias-del-videojuego-del-mundo/)
* [Visit Finland](https://www.visitfinland.com/es/helsinki/)


![Moomin](/images/moomin.png)
