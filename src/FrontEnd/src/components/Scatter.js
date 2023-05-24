import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, Label } from 'recharts';
import React, { useEffect, useState } from 'react';

const UnemploymentScatterPlot = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/unemployment')
      .then(response => response.json())
      .then(data => setData(data.unemploy_rate));
  }, []);

  return (
    <ScatterChart
      width={400}
      height={300}
      margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
    >
      <CartesianGrid />
      <XAxis dataKey="num_alcohol" name="num_alcohol" unit="places">
        <Label value="Number of Alcohol Places" offset={-5} position="insideBottom" />
      </XAxis>
      <YAxis dataKey="total_unemployment" name="total_unemployment" unit="people">
        <Label value="Total Unemployment" angle={-90} position="insideLeft" />
      </YAxis>
      <Tooltip cursor={{ strokeDasharray: '3 3' }} />
      <Scatter name="Cities" data={data} fill="#8884d8">
        {data.map((entry, index) => (
          <Label value={entry.city} position="top" key={`label-${index}`} />
        ))}
      </Scatter>
    </ScatterChart>
  );
};

export default UnemploymentScatterPlot;
