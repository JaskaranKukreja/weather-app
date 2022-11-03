import React, { ReactElement, useEffect, useState } from 'react';
import { Wrapper, Status } from "@googlemaps/react-wrapper";
import {START_POINT,ZOOM_LEVEL,TOP_CANADIAN_CITIES_COORDINATES} from '../constants';
import { getWeatherData } from '../api';
import { WeatherData,Coordinates } from '../types';
import Map from '../components/Map';

const render = (status: Status): ReactElement => {
    if (status === Status.LOADING) return <h3>{status} ..</h3>;
    return <h3>{status} ...</h3>;
};

const HomePage = () => {
    const [weatherData,setWeatherData] = useState<Array<WeatherData> | undefined>(undefined);
    const [addMarker,setAddMarker] = useState<Coordinates>();

    useEffect(() => {
        if(!weatherData){
            (async () => {
                const data = [];
                for(const coordinates of TOP_CANADIAN_CITIES_COORDINATES){
                    const response = (await getWeatherData(coordinates));
                    data.push({...response,'coordinates': coordinates});
                }
                setWeatherData(data);
            })();
        }
    },[]);
    
    const onClick = async (options: any) => {
        const {latLng} = options;
        const coordinates = {'LATITUDE': latLng.lat(),'LONGITUDE': latLng.lng()};
        const data = weatherData || [];
        if(coordinates.LATITUDE && coordinates.LONGITUDE){
            const response = await getWeatherData(coordinates);
            if(response){
                data.push({...response,'coordinates': coordinates});
                setWeatherData(data);
                setAddMarker(coordinates);
            } 
        }
    }

    if(!weatherData){
        return null;
    }

    return (
        <div className='mt-5'>
            <Wrapper apiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY || ''} render = {render}>
                <Map 
                    center={{ lat: START_POINT.LATITUDE, lng: START_POINT.LONGITUDE }} 
                    zoom={ZOOM_LEVEL}
                    weatherData={weatherData}
                    addMarker={addMarker}
                    onClick={onClick}
                />    
            </Wrapper>
        </div>
        
    );
}
 
export default HomePage;