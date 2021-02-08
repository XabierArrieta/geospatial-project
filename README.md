# geospatial-project

![Spot](/Images/spot.png)

Este es un proyecto que lo he realizado durante el Bootcamp de Data Anatlytics en [Ironhack](https://www.ironhack.com/es/data-analytics) Madrid.

# Obejtivo

El objetivo de este proyecto es determinar la ubicación perfecta de una compañía de videojuegos en base a unos criterios:
- A los diseñadores les gusta ir a charlas de diseño y compartir conocimientos. Debe haber algunas empresas cercanas que también diseñen.
- El 30% del personal de la empresa tiene al menos 1 hijo.
- A los desarrolladores les gusta estar cerca de nuevas empresas tecnológicas exitosas que hayan recaudado al menos 1 millón de dólares.
- A los ejecutivos les gusta mucho Starbucks. Asegúrese de que haya un Starbucks no muy lejos.
- Los gerentes de cuentas necesitan viajar mucho.
- Todos en la empresa tienen entre 25 y 40 años, dales un lugar para ir de fiesta.
- El CEO es vegano.
- Si quieres hacer feliz al encargado de mantenimiento, un estadio de baloncesto debe estar a unos 10 km.
- El perro de la oficina, "Dobby", necesita un peluquero todos los meses. Asegúrese de que haya uno no demasiado lejos.


# Proceso

Para conseguir mi objtivo, comienzo con un dataset de [Crunchbase] (https://www.crunchbase.com/) que contiene información de mas de 18000 compañias. 
Continuo limpiando el dataset y eniqueciendola añadiendo información con la API de Foursquare.
Finalmente, filtro los datos según los criterios establecidos y selecciono la ubicación de la companía y así satisfacer a la mayoría de empleados, incluyendo un mapa interactivo usando Folium.

# Referencias

[Crunchbase](https://data.crunchbase.com/docs)
[Fursquare API](https://developer.foursquare.com/)