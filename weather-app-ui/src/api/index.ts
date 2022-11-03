import axios from 'axios';
import { Coordinates } from '../types';
import { getWeatherAPIURL } from '../utils';

export const getWeatherData = async (coordinates: Coordinates) => {
    try{
        const { data } = await axios.get(getWeatherAPIURL(coordinates));
        return data;
    }catch(error){
        console.log('Error message: ', error);
    }
}

export const getWeatherPrediction = async (city: string) => {
    try{
        const { data } = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/weather/predict?city=${city}`);
        return data;
    }catch(error){
        console.log('Error message: ', error);
    }
}

export const getWeatherHistory = async (city: string) => {
    try{
        const { data } = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/weather/history?city=${city}`);
        return data;
    }catch(error){
        console.log('Error message: ', error);
    }
}