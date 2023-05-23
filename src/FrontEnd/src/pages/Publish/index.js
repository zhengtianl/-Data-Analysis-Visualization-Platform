import { observer } from 'mobx-react-lite'
import './index.scss'
import 'react-quill/dist/quill.snow.css'
import { http } from '@/utils/http'
import React, { useEffect, useState } from 'react';
import Draggable from 'react-draggable';
import Bar from '@/components/Bar';
import { Select, Button} from 'antd';
import './index.scss';

const Unemployment = () => {
  const [alcoholCount, setAlcoholCount] = useState([]);
  const [numberOfAlcoholCities, setNumberOfAlcoholCities] = useState(3);
  const [numberOfUnemploymentCities, setNumberOfUnemploymentCities] = useState(3);
  const [rankTweet, setRankTweet] = useState([]);
  const [selectedCity, setSelectedCity] = useState('');
  const { Option } = Select;
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

  const alcoholCities = alcoholCount.map((item) => item.city);
  const rankCities = rankTweet.map((item) => item.city);

  const commonCities = alcoholCities.filter((city) => rankCities.includes(city));

  const calculateRatios = () => {
    const ratios = {};

    commonCities.forEach((city) => {
      const alcoholCityObject = alcoholCount.find((item) => item.city === city);
      const rankCityObject = rankTweet.find((item) => item.city === city);
  
      if (alcoholCityObject && rankCityObject) {
        const alcoholCount = alcoholCityObject.count;
        const rankCount = rankCityObject.count;
        const ratio = alcoholCount / rankCount;

        ratios[city] = ratio;

        
      }
    });

    return ratios;
  };

  const ratios = calculateRatios();

  const handleChangeCity = (value) => {
    setSelectedCity(value);
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
            title="Cities with the most tweets"
          />
        </div>
      </Draggable>

      <Draggable>
      <div className="chart-card" title="Alcohol tweets as a share of all tweets">
          <div className="select-container" title="Alcohol tweets as a share of all tweets">
            <Select value={selectedCity} onChange={handleChangeCity} title="Alcohol tweets as a share of all tweets">
              <Option value="">Select City</Option>
              {Object.keys(ratios).map((city) => (
                <Option value={city} key={city}>
                  {city}
                </Option>
              ))}
            </Select>
            {selectedCity && (
              <div className="selected-value">
                <Bar
                  style={{ width: '500px', height: '300px' }}
                  xData={[selectedCity]} // Wrap the selectedCity value in an array
                  sData={[ratios[selectedCity] * 100]} // Wrap the ratios[selectedCity] value in an array
                  title="Alcohol tweets as a share of all tweets"
                />
              </div>
            )}
          </div>
        </div>
      </Draggable>
    </div>
  );
};

export default observer(Unemployment); 