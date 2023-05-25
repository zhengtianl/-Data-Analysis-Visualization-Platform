import React, { useEffect, useState } from 'react';
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';

const CustomScatter = (props) => {
    const { cx, cy, payload } = props;
    return (
      <>
        <circle cx={cx} cy={cy} fill="#8884d8" r={5} />
        <text x={cx} y={cy} dy={-5} textAnchor="middle" fontSize={10} fill="#333">
          {payload.city_name}
        </text>
      </>
    );
  };
const ScatterPlot = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const jsonData = [
      { city_name: "melbourne", x: 36, y: 2699 },
      { city_name: "sydney", x: 146, y: 2171 },
      { city_name: "brisbane", x: 1125, y: 979 },
      { city_name: "perth", x: 23, y: 620 },
      { city_name: "adelaide", x: 19, y: 592 },
      { city_name: "gold coast", x: 496, y: 265 },
      { city_name: "toowoomba", x: 420, y: 192 },
      { city_name: "hobart", x: 33, y: 149 },
      { city_name: "newcastle", x: 355, y: 128 },
      { city_name: "sunshine coast", x: 367, y: 108 },
      { city_name: "wollongong", x: 295, y: 85 },
      { city_name: "central coast", x: 669, y: 78 },
      { city_name: "central coast", x: 62, y: 78 },
      { city_name: "cairns", x: 1150, y: 67 },
      { city_name: "townsville", x: 1027, y: 67 }
    ];

    setData(jsonData);
  }, []);

  return (
    <ScatterChart width={800} height={600} margin={{ top: 20, right: 20, bottom: 20, left: 20 }}>
      <CartesianGrid />
      <XAxis type="number" dataKey="x" name="X" />
      <YAxis type="number" dataKey="y" name="Y" />
      <Tooltip cursor={{ strokeDasharray: '3 3' }} />
      <Legend />
      <Scatter data={data} shape={<CustomScatter />} />
    </ScatterChart>
  );
};

export default ScatterPlot;
