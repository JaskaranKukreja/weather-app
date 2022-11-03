import React, { useEffect, useRef} from 'react';
import { MarkerClusterer } from "@googlemaps/markerclusterer";
import { WeatherData } from '../types';

const Map = ({onClick,center,zoom,weatherData,addMarker}: any) => {
    const ref:any = useRef();
    const [map, setMap] = React.useState<google.maps.Map|any>();
    const [infoWindow,setInfoWindow] = React.useState<google.maps.InfoWindow>();

    useEffect(() => {
        if(!addMarker || !weatherData)
            return;
        const data = weatherData.filter(
            (d: any) => d.coordinates.LATITUDE === addMarker.LATITUDE 
            && d.coordinates.LONGITUDE === addMarker.LONGITUDE
        )
        const marker = getMarker(data[0],infoWindow);
        if(map){
            marker.setMap(map);
        }
    },[addMarker]);

    useEffect(() => {
        const map = new window.google.maps.Map(ref.current, {
            center,
            zoom,
        });
        map.addListener("click", onClick);
        const infoWindow = new google.maps.InfoWindow();
        
        const markers = weatherData.map((data: any) => {  
            return getMarker(data,infoWindow)
        });
        
        new MarkerClusterer({ map, markers });
        setMap(map);
        setInfoWindow(infoWindow);
    },[]);

    const getMarker = (data: any,infoWindow:google.maps.InfoWindow|undefined) => {
        const marker = new google.maps.Marker({
            position: {
                lat: data.coordinates.LATITUDE,
                lng: data.coordinates.LONGITUDE
            },
            label: data.temperature.toString()
        });
        marker.addListener("click",() => {
            infoWindow && infoWindow.setContent(`
                <div>
                    <p>Temperature: ${data.temperature}&deg;C<p>
                    <p>Feels like: ${data.feelsLike}&deg;C</p>
                    <p>Wind direction: ${data.wind.direction}</p>
                    <p>Wind speed: ${data.feelsLike}(km/h)</p>
                </div>
            `);
            infoWindow && infoWindow.open({anchor:marker,map: map});
        });
        return marker;
    }

    return <div ref={ref} id="map" style={{ height: "750px" }}/>;
}

export default Map;