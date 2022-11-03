export type Coordinates = {
    LATITUDE: number,
    LONGITUDE: number
}

export interface WeatherData {
  time: {
    local: string,
    utc: string
  },
  weatherCode: {
    value: string
  },
  temperature: number,
  dewPoint: number,
  feelsLike: number,
  wind: {
    direction: string,
    speed: number,
    gust: number
  },
  relativeHumidity: number,
  pressure: {
    value: number,
    trend: number
  },
  visibility: number,
  ceiling: number,
  coordinates: Coordinates
}

export type WeatherHistoryResponsePayload = {
  [date: string]: {
    date: string,
    maxTemp: number,
    minTemp: number
  }
}

export type WeatherPredictionDataPayload = {
  [date:string]:{
    [period:string]: {
      temperature: number,
      feelsLike: number,
      wind: string,
    }
  }
}
