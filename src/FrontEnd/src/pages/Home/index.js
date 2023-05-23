import React, { useEffect, useState } from 'react';
import Draggable from 'react-draggable';
import ReactEcharts from 'echarts-for-react';
import Bar from '@/components/Bar';
import { http } from '@/utils';
import './index.scss';
import WordCloud from '@/components/WordCloud/WordCloud';

const MemoizedWordCloud = React.memo(WordCloud); // 使用React.memo包装词云组件

const Home = () => {
  const [negative, setNegative] = useState(null);
  const [neutral, setNeutral] = useState(null);
  const [positive, setPositive] = useState(null);
  const [wordsArray, setWordsArray] = useState(null);
  const [wordCloudClicked, setWordCloudClicked] = useState(false); // 添加一个状态用于记录词云是否被点击

  useEffect(() => {
    http
      .get('/sentiment')
      .then((response) => {
        const sentimentDetectTweet = response.sentiment_detect_tweet;
        setNegative(sentimentDetectTweet.negative);
        setNeutral(sentimentDetectTweet.neutral);
        setPositive(sentimentDetectTweet.positive);

        const text = "I hate this fuking world and this class very much";
        const words = text.split(" ").map((word) => ({ text: word, value: 1 }));
        setWordsArray(words);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  useEffect(() => {
    if (wordsArray && !wordCloudClicked) {
      setWordCloudClicked(true);
    }
  }, [wordsArray, wordCloudClicked]);

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


      <div className="wordcloud-container">
        <Draggable>
          <div className="chart-card">
            {wordCloudClicked && <MemoizedWordCloud words={wordsArray} />}
          </div>
        </Draggable>
      </div>
    </div>
  );
};

export default Home;
