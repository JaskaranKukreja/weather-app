import { Coordinates } from "./types";
import {WEATHER_API_BASE_URL} from "./constants";

const getWeatherAPIURL = (coordinates: Coordinates): string => {
    return `${WEATHER_API_BASE_URL}/observation?lat=${coordinates.LATITUDE}&long=${coordinates.LONGITUDE}`;
}

function average(data: Array<number>) {
    return data.reduce((a, b) => a + b, 0) / data.length;
}

export {
    getWeatherAPIURL,
    average
}