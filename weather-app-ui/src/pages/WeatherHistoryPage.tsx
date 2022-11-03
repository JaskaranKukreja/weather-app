import React, { useEffect, useState } from 'react';

import { getWeatherHistory } from '../api';
import LineChart from '../components/LineChart';
import { WeatherHistoryResponsePayload } from '../types';
import { average } from '../utils';

const WeatherHistoryPage = () => {
    const queryParams = new URLSearchParams(window.location.search);
    const [weatherHistory,setWeatherHistory] = useState<WeatherHistoryResponsePayload>({});

    useEffect(() => {
        const city = queryParams.get('city') || '';
        (async function () {
            const weatherForeCastData = await getWeatherHistory(city);
            setWeatherHistory(weatherForeCastData);
        })();
    },[]);

    const getChartData = () => {
        const minTempData:Array<number> = [];
        const maxTempData:Array<number> = [];

        Object.values(weatherHistory).forEach(({maxTemp,minTemp}) => {
            minTempData.push(minTemp)
            maxTempData.push(maxTemp)
        })
        
        return [
            {
              label: 'High Temp',
              data: maxTempData,
              borderColor: 'rgb(255, 99, 132)',
              backgroundColor: 'rgba(255, 99, 132, 0.5)',
            },
            {
              label: 'Low Temp',
              data: minTempData,
              borderColor: 'rgb(53, 162, 235)',
              backgroundColor: 'rgba(53, 162, 235, 0.5)',
            },
            {
                label: 'Mean',
                data: maxTempData.map(e => average([...maxTempData, ...minTempData])),
                borderColor: 'rgb(155, 161, 153)',
                borderDash: [10,5]
            }
          ]
    }

    if(!weatherHistory){
        return null;
    }

    return (
        <>
            <h1 className='ml-10 mt-5 text-3xl font-bold'>
                Weather history for {new URLSearchParams(window.location.search).get('city') || ''}
            </h1>
            <div className='p-10 grid place-items-center'>
                {weatherHistory && Object.keys(weatherHistory).length>0 && <LineChart xAxisData={Object.keys(weatherHistory)} yAxisData={getChartData()}/>} 
            </div>    
        </>
    )
}

export default WeatherHistoryPage;