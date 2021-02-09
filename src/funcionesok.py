import pandas as pd
import geopandas as gpd
import sys
from dotenv import load_dotenv
import os
import requests
import json
from functools import reduce
import operator
from cartoframes.viz import Map, Layer, popup_element
from haversine import haversine
from pymongo import MongoClient,GEOSPHERE
import shapely.geometry


donde = input
def geocode(address):
    """
    Introduciendo un dirección se obtiene las coordenadas
    """
    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    try:
        return {
            "type":"Point",
            "coordinates":[float(data["latt"]),float(data["longt"])]}
    except:
        return data                        
                           
                           
def geo_api():
    
    """
    Introduciendo un criterio para llamar a la API de Foursquare, obtienes un mapa con los puntos obtenidos
    
    """
    
    load_dotenv()
    tok1 = os.getenv("tok1")
    tok2 = os.getenv("tok2")
    url_query = 'https://api.foursquare.com/v2/venues/explore' 
          
    criterio = input("¿Qué quieres buscar en Foursquare? \n")
    limite = input ("¿Cuántas búsquedas quieres que muestre? \n")
    radio = input("¿En qué radio?(medida = metros) \n")
          
    params = {"client_id" : tok1,
              "client_secret" : tok2,
              "v": "20180323",
              "ll": f"60.17212, 24.94519",
              "query":f"{criterio}",
              "limit": {limite},
              "radius": {radio}
            }
    
    resp = requests.get(url = url_query, params=params)
    data = json.loads(resp.text)
    decoding_data = data.get ("response")
    decoded = decoding_data.get("groups")[0]
    items = decoded.get("items")
    
    mapa_nombre = ["venue", "name"]
    m_latitude = ["venue", "location", "lat"]
    m_longitude = ["venue", "location", "lng"]
    
    def getFromDict(diccionario,mapa):
        return reduce(operator.getitem,mapa,diccionario)
    
    list_items =[]
    for dic in items:
        items_dict = {}
        items_dict["name"] = getFromDict(dic,mapa_nombre)
        items_dict["latitud"] = getFromDict(dic,m_latitude)
        items_dict["longitud"] = getFromDict(dic,m_longitude)
        
        list_items.append(items_dict)
        
        dataframefinal = pd.DataFrame(list_items)
        
        gdf = gpd.GeoDataFrame(dataframefinal,geometry = gpd.points_from_xy(dataframefinal.longitud, dataframefinal.latitud))
        mapa = Map(Layer(gdf, popup_hover = [popup_element("name",f"{criterio}")]))

    
    return mapa

"""

def mongo(gdf_criterio, db):
    

    Introduciendo un geodaframe de un criterio, crea una colección en Mongo con un indice de 2 esferas y calcula el punto más cercano con unas coordenadas
    
    
    
    gdf['geometry']=gdf['geometry'].apply(lambda x:shapely.geometry.mapping(x))
    client = MongoClient()
    db = client.ironhack
    collection = {db}
    collection.create_index ([("geometry", GEOSPHERE)])
    data = gdf.to_dict(orient='records')
    collection.insert_many(data)
    cercano = {db}.find({"geometry":{"$near":{"type":"Point", "coordinates":[f"60.17212, 24.94519"]}}})
    display(place_near_geo)
    
    return cercano


"""










    