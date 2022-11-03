import React, { useEffect, useState } from 'react';
import { getWeatherPrediction } from '../api';
import LineChart from '../components/LineChart';
import { WeatherPredictionDataPayload } from '../types';
import { average } from '../utils';

const WeatherPredictionPage = () => {
    const queryParams = new URLSearchParams(window.location.search);
    const [weatherForecastData,setWeatherForecastData] = useState<WeatherPredictionDataPayload>({});

    useEffect(() => {
        const city = queryParams.get('city') || '';
        (async function () {
            const weatherForeCastData = await getWeatherPrediction(city);
            setWeatherForecastData(weatherForeCastData);
        })();
    },[]);

    const getChartData = () => {
        const minTempData:Array<number> = [];
        const maxTempData:Array<number> = [];
        let index = 0;
        Object.values(weatherForecastData).forEach(weatherPeriodData => {
            minTempData[index] = Math.min(...Object.values(weatherPeriodData).map((d)=>d.temperature))
            maxTempData[index] = Math.max(...Object.values(weatherPeriodData).map((d)=>d.temperature))
            index+=1;
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

    if(!weatherForecastData){
        return null;
    }

    return (
        <>
            <h1 className='ml-10 mt-5 text-3xl font-bold'>
                Weather trend for next {weatherForecastData && Object.keys(weatherForecastData).length} days.
            </h1>
            <div className='p-10 grid place-items-center'>
                {weatherForecastData && Object.keys(weatherForecastData).length>0 && <LineChart xAxisData={Object.keys(weatherForecastData)} yAxisData={getChartData()}/>} 
            </div>
            
            <h1 className='ml-10 mt-5 text-3xl font-bold'>
                Weather prediction for next {weatherForecastData && Object.keys(weatherForecastData).length} days.
            </h1>
            <div className='p-10 grid place-items-center'>
                <table className="border-collapse w-100%">
                    <thead>
                        <tr>
                            <th className="text-center text-lg p-4 border border-2 border-black">Date</th>
                            <th className="text-center text-lg p-4 border border-2 border-black">Morning</th>
                            <th className="text-center text-lg p-4 border border-2 border-black">Afternoon</th>
                            <th className="text-center text-lg p-4 border border-2 border-black">Evening</th>
                            <th className="text-center text-lg p-4 border border-2 border-black">Overnight</th>
                        </tr>
                    </thead>
                    
                    <tbody>
                        {
                            Object.keys(weatherForecastData).map((date: string) => (
                                <tr key={`${date}`}>
                                    <td className="text-center text-sm p-4 border border-2 border-black">
                                        {date}
                                    </td>
                                    <td className="text-left text-sm p-4 border border-2 border-black">
                                        {weatherForecastData[date]['period1'] ? (
                                            <>
                                                <p><b>Temperature:</b> {weatherForecastData[date]['period1']['temperature']}&#8451;</p>
                                                <p><b>Feels like:</b> {weatherForecastData[date]['period1']['feelsLike']}&#8451;</p>
                                                <p><b>Wind (km/h)</b>: {weatherForecastData[date]['period1']['wind']}</p>
                                            </>
                                        ): 'N/A'}
                                    </td>
                                    <td className="text-left text-sm p-4 border border-2 border-black">
                                        {weatherForecastData[date]['period2'] ? (
                                            <>
                                                <p><b>Temperature:</b> {weatherForecastData[date]['period2']['temperature']}&#8451;</p>
                                                <p><b>Feels like:</b> {weatherForecastData[date]['period2']['feelsLike']}&#8451;</p>
                                                <p><b>Wind (km/h):</b> {weatherForecastData[date]['period2']['wind']}</p>
                                            </>
                                        ): 'N/A'}
                                    </td>
                                    <td className="text-left text-sm p-4 border border-2 border-black">
                                        {weatherForecastData[date]['period3'] ? (
                                            <>
                                                <p><b>Temperature:</b> {weatherForecastData[date]['period3']['temperature']}&#8451;</p>
                                                <p><b>Feels like:</b> {weatherForecastData[date]['period3']['feelsLike']}&#8451;</p>
                                                <p><b>Wind (km/h):</b> {weatherForecastData[date]['period3']['wind']}</p>
                                            </>
                                        ): 'N/A'}
                                    </td>
                                    <td className="text-left text-sm p-4 border border-2 border-black">
                                        {weatherForecastData[date]['period4'] ? (
                                            <>
                                                <p><b>Temperature:</b> {weatherForecastData[date]['period4']['temperature']}&#8451;</p>
                                                <p><b>Feels like:</b> {weatherForecastData[date]['period4']['feelsLike']}&#8451;</p>
                                                <p><b>Wind (km/h):</b> {weatherForecastData[date]['period4']['wind']}</p>
                                            </>
                                        ): 'N/A'}
                                    </td>
                                </tr>
                            ))
                        }
                    </tbody>
                    
                </table>
            </div>
            
        </>
    )
}

export default WeatherPredictionPage;