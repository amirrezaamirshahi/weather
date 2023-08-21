import requests
from fastapi import FastAPI, HTTPException, status


def createURL(CityName):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "2fa1918df05614761ab6ffbf82c26d71"
    CITY = CityName
    try:
        return BASE_URL + "q=" + CITY+"&APPID="+API_KEY
    except:
        return False


def KelvinToCelsius(kelvin):
    return kelvin - 273.15


app = FastAPI()


@app.get("/{cityName}", status_code=status.HTTP_200_OK)
async def root(cityName: str):
    response = requests.get(createURL(cityName))
    if not response:
        raise HTTPException(status_code=404, detail="city not found")

    else:
        response = requests.get(createURL(cityName)).json()
        res = {"temp": KelvinToCelsius(response['main']['temp']), "maxtemp": KelvinToCelsius(
            response['main']['temp_max']), "mintemp": KelvinToCelsius(response['main']['temp_min'])}
        return res
