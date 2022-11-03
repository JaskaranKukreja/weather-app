import { Coordinates } from "./types";

const START_POINT: Coordinates = {
    'LATITUDE': 49.895077,
    'LONGITUDE': -97.138451
};

const ZOOM_LEVEL: number = 5;

const TOP_CANADIAN_CITIES_COORDINATES: Array<Coordinates> = [
    //Toronto
    {'LATITUDE': 43.651070,'LONGITUDE': -79.347015},
    //Montreal
    {'LATITUDE': 45.630001,'LONGITUDE': -73.519997},
    //Ottawa
    {'LATITUDE': 45.424721,'LONGITUDE': -75.695000},
    //Edmonton
    {'LATITUDE': 53.522778,'LONGITUDE': -113.623055},
    //Winnipeg
    {'LATITUDE': 49.895077,'LONGITUDE': -97.138451},
    //Vancouver
    {'LATITUDE': 49.246292,'LONGITUDE': -123.116226},
]

const WEATHER_API_BASE_URL: string = 'https://weatherapi.pelmorex.com/v1';

const WIND_DIRECTION_CODE_TO_NAME_MAP = {
    'N': 'North',
    'S': 'South',
    'E': 'East',
    'W': 'West'
}

export {
    START_POINT,
    ZOOM_LEVEL,
    TOP_CANADIAN_CITIES_COORDINATES,
    WEATHER_API_BASE_URL,
    WIND_DIRECTION_CODE_TO_NAME_MAP
}