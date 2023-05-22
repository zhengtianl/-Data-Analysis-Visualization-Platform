import { observer } from 'mobx-react-lite'
import './index.scss'
import 'react-quill/dist/quill.snow.css'
import { http } from '@/utils/http'
import React, { useEffect, useState } from 'react';
import Draggable from 'react-draggable';
import Bar from '@/components/Bar';
import ReactEcharts from 'echarts-for-react';
import { Button } from 'antd';
import './index.scss';

const Unemployment = () => {
  const [alcoholCount, setAlcoholCount] = useState([]);
  const [numberOfAlcoholCities, setNumberOfAlcoholCities] = useState(3);
  const [numberOfUnemploymentCities, setNumberOfUnemploymentCities] = useState(3);
  const [rankTweet, setRankTweet] = useState([]);

  const handleShowAlcoholCities = (num) => {
    setNumberOfAlcoholCities(num);
  };

  const handleShowUnemploymentCities = (num) => {
    setNumberOfUnemploymentCities(num);
  };
  
  const handleShowAllCities = (num) => {
    setNumberOfAlcoholCities(num);
    setNumberOfUnemploymentCities(num);
  };

  useEffect(() => {
    http
      .get('/alcohol_detect')
      .then((response) => {
        const alcoholCountTweet = response.alcohol_count_lga;
        const sortedData = alcoholCountTweet.sort((a, b) => b.count - a.count);
        const topCities = sortedData.slice(0, numberOfAlcoholCities);
        setAlcoholCount(topCities);
      })
      .catch((error) => {
        console.log(error);
      });

    http
      .get('/rank')
      .then((response) => {
        const rankTweetData = response.rank_tweet;
        const sortedData = rankTweetData.sort((a, b) => b.rank - a.rank);
        const topCity = sortedData.slice(0, numberOfUnemploymentCities)
        setRankTweet(topCity);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [numberOfAlcoholCities, numberOfUnemploymentCities]);

  const getAlcoholChartData = () => {
    return alcoholCount.map((item) => ({
      name: 'Alcohol Mentioned',
      value: item.count,
      city: item.city,
    }));
  };

  const getUnemploymentChartData = () => {
    return rankTweet.map((item) => ({
      name: 'Unemployment Mentioned',
      value: item.count,
      city: item.city,
    }));
  };

  const getChartOptions = () => {
    const alcoholData = getAlcoholChartData();
    const unemploymentData = getUnemploymentChartData();

    return {
      tooltip: {
        trigger: 'axis'
      },
      legend: {
        data: ['Alcohol Mentioned', 'Unemployment Mentioned']
      },
      grid: {
        width: '60%', // 调整图表的宽度
        left: '20%' // 调整图表的位置
      },
      xAxis: {
        type: 'category',
        data: alcoholData.map((item) => item.city)
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          name: 'Alcohol Mentioned',
          type: 'line',
          stack: 'area',
          areaStyle: {},
          data: alcoholData.map((item) => item.value)
        },
        {
          name: 'Unemployment Mentioned',
          type: 'line',
          stack: 'area',
          areaStyle: {},
          data: unemploymentData.map((item) => item.value)
        }
      ]
    };
  };

  return (
    <div className="unemployment-and-alcohol">
      <div className="button-group">
        <Button type="primary" style={{ marginBottom: '10px' }} block onClick={() => handleShowAllCities(1)}>
          All top1
        </Button>
        <Button type="primary" style={{ marginBottom: '10px' }} block onClick={() => handleShowAllCities(3)}>
          All top3
        </Button>
        <Button type="primary" style={{ marginBottom: '10px' }} block onClick={() => handleShowAllCities(5)}>
          All top5
        </Button>
      </div>
      
      <Draggable>
        <div className="chart-card">
          <div>
            <Button style={{ marginRight: '10px' }} onClick={() => handleShowAlcoholCities(1)}>
              top1
            </Button>
            <Button style={{ marginRight: '10px' }} onClick={() => handleShowAlcoholCities(3)}>
              top3
            </Button>
            <Button style={{ marginRight: '10px' }} onClick={() => handleShowAlcoholCities(5)}>
              top5
            </Button>
          </div>

          <Bar
            style={{ width: '500px', height: '300px' }}
            xData={alcoholCount.map((item) => item.city)}
            sData={alcoholCount.map((item) => item.count)}
            title="Cities with the most alcohol mentioned"
          />
        </div>
      </Draggable>

      <Draggable>
        <div className="chart-card">
          <div>
            <Button style={{ marginRight: '10px' }} onClick={() => handleShowUnemploymentCities(1)}>
              top1
            </Button>
            <Button style={{ marginRight: '10px' }} onClick={() => handleShowUnemploymentCities(3)}>
              top3
            </Button>
            <Button style={{ marginRight: '10px' }} onClick={() => handleShowUnemploymentCities(5)}>
              top5
            </Button>
          </div>
          <Bar
            style={{ width: '500px', height: '300px' }}
            xData={rankTweet.map((item) => item.city)}
            sData={rankTweet.map((item) => item.count)}
            title="Cities with the most unemployment mentioned"
          />
        </div>
      </Draggable>

      <Draggable>
        <div className="chart-card">
          <ReactEcharts
            option={getChartOptions()}
          />
        </div>
      </Draggable>
    </div>
  );
};

export default observer(Unemployment);