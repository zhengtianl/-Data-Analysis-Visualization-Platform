
import React, { useEffect, useState } from 'react';
import Draggable from 'react-draggable';
import ReactEcharts from 'echarts-for-react';
import Bar from '@/components/Bar';
import { http } from '@/utils';
import './index.scss';
import WordCloud from '@/components/WordCloud/WordCloud';
import Map3 from '@/components/Map3';
const MemoizedWordCloud = React.memo(WordCloud); // 使用React.memo包装词云组件

const Home = () => {
  const [negative, setNegative] = useState(null);
  const [neutral, setNeutral] = useState(null);
  const [positive, setPositive] = useState(null);
  const [wordsArray] = useState(null);
  const [wordCloudClicked, setWordCloudClicked] = useState(false); // 添加一个状态用于记录词云是否被点击
  const [wordCloudData, setWordCloudData] = useState([]);
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

  useEffect(() => {
    if (wordsArray && !wordCloudClicked) {
      setWordCloudClicked(true);
    }
  }, [wordsArray, wordCloudClicked]);


  const fetchData = () => {
    fetch('http://127.0.0.1:5000/wordcloud')
      .then(response => response.json())
      .then(data => {
        const cleanWordListMas = data.clean_word_list_mas;
        const wordsArray = cleanWordListMas.split(" ");
        const wordCountMap = {};

        wordsArray.forEach(word => {
          if (wordCountMap[word]) {
            wordCountMap[word]++;
          } else {
            wordCountMap[word] = 1;
          }
        });

        const wordCloudData = Object.entries(wordCountMap).map(([text, value]) => ({ text, value }));
        setWordCloudData(wordCloudData);
      })
      .catch(error => {
        console.error('Error fetching word cloud data:', error);
      });
  };

  fetchData();

  

  return (
    <div className="home" style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
      <div className="chart-card" style={{ backgroundColor: '#f0f0f0' }}>
        <Bar
          style={{ width: '500px', height: '400px' }}
          xData={['positive', 'negative', 'neutral']}
          sData={[positive, negative, neutral]}
          title="Emotion statistics"
        />
      </div>
  
      <div className="chart-card" style={{ backgroundColor: '#f0f0f0' }}>
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
      <Draggable>
      <div className="chart-card" style={{ backgroundColor: '#f0f0f0' }}>
        <Map3></Map3>
      </div>
      </Draggable>
      <div className="chart-card wordcloud-container" style={{ backgroundColor: '#f0f0f0' }}>
        {wordCloudClicked && <MemoizedWordCloud words={wordCloudData} />}
      </div>
    </div>
  );
}  

export default Home;