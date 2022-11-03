import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';
import * as ChartAnnotation from 'chartjs-plugin-annotation';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
);

ChartJS.register(ChartAnnotation);


export const options:any  = {
  responsive: false,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'bottom',
    }
  },
};

const LineChart = (
  props: any
) => {
  const {xAxisData,yAxisData} = props;
  return <Line options={options} height={500} width={1000} data={{labels:xAxisData,datasets:yAxisData}} />;
}

export default LineChart;
