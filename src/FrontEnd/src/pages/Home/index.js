import React, { useEffect, useState } from 'react';
import Draggable from 'react-draggable';
import ReactEcharts from 'echarts-for-react';
import Bar from '@/components/Bar';
import { http } from '@/utils';
import './index.scss';

const Home = () => {
  const [negative, setNegative] = useState(null);
  const [neutral, setNeutral] = useState(null);
  const [positive, setPositive] = useState(null);

  useEffect(() => {
    http
      .get('/sentiment')
      .then((response) => {
        const sentimentDetectTweet = response.sentiment_detect_tweet;
        setNegative(sentimentDetectTweet.negative);
        setNeutral(sentimentDetectTweet.neutral);
        setPositive(sentimentDetectTweet.positive);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className="home">
      <Draggable>
        <div className="chart-card">
          <Bar
            style={{ width: '500px', height: '400px' }}
            xData={['positive', 'negative', 'neutral']}
            sData={[positive, negative, neutral]}
            title="Emotion statistics"
          />
        </div>
      </Draggable>
      <Draggable>
        <div className="chart-card">
          <ReactEcharts
            option={{
              title: {
                text: 'Emotional Pie chart',
                left: 'left',
                top: 5
              },
              series: [
                {
                  name: 'Utilization',
                  type: 'pie',
                  radius: ['80%'],
                  avoidLabelOverlap: false,
                  label: {
                    show: false,
                    position: 'center'
                  },
                  emphasis: {
                    label: {
                      show: true,
                      fontSize: '30',
                      fontWeight: 'bold'
                    }
                  },
                  data: [
                    { value: positive, name: 'positive' },
                    { value: negative, name: 'negative' },
                    { value: neutral, name: 'neutral' }
                  ]
                }
              ]
            }}
          />
        </div>
      </Draggable>
    </div>
  );
};

export default Home;
