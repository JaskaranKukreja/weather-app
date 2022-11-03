# React-weather-app-ui
Steps to run the app:
1. Add Google maps api key to REACT_APP_GOOGLE_MAPS_API_KEY present in .env file.
2. To install dependencies run command `npm install`
3. To run the application run command `npm start`
4. Please turn on CORS via a chrome extension, otherwise your browser might not load the page.
5. This react app consistes of three pages:
  - ${BASE_URL}/ => Should load a google map to show top canadian cities weather.
  - ${BASE_URL}/predict?city=toronto => Should load weather prediction for city of toronto. 
  - ${BASE_URL}/predict?city=toronto => Should load weather history for city of toronto.
