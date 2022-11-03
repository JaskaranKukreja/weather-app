import React  from 'react';
import { BrowserRouter as Router,Route,Routes } from "react-router-dom";
import HomePage from './pages/HomePage';
import WeatherPredictionPage from './pages/WeatherPredictionPage';
import WeatherHistoryPage from './pages/WeatherHistoryPage';
import NotFoundPage from './pages/NotFoundPage';
function App() {
  return (
    <Router>
        <Routes>
          <Route path="/" element={<HomePage/>}/>
          <Route path="/predict" element={<WeatherPredictionPage/>}/>
          <Route path="/history" element={<WeatherHistoryPage/>}/>
          <Route path="*" element={<NotFoundPage/>}/>
        </Routes>
    </Router>
  );
}

export default App;
