import React, { useEffect, useState } from 'react';
import Draggable from 'react-draggable';
import ReactEcharts from 'echarts-for-react';
import Bar from '@/components/Bar';
import { http } from '@/utils';
import './index.scss';
import WordCloud from '@/components/WordCloud/WordCloud';
import Map3 from '@/components/Map3';

const MemoizedWordCloud = React.memo(WordCloud, (prevProps, nextProps) => {
  return prevProps.words === nextProps.words; // 根据words属性判断是否相等
});

const Home = () => {
  const [negative, setNegative] = useState(null);
  const [neutral, setNeutral] = useState(null);
  const [positive, setPositive] = useState(null);
  const [wordCloudClicked, setWordCloudClicked] = useState(false);
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
    if (wordCloudData.length > 0 && !wordCloudClicked) {
      setWordCloudClicked(true);
    }
  }, [wordCloudData, wordCloudClicked]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://172.26.135.85:5000/wordcloud');
        const data = await response.json();

        const cleanWordListMas = data.clean_word_list_mas;
        const wordsArray = cleanWordListMas.split(' ');
        const wordCountMap = {};

        wordsArray.forEach((word) => {
          if (wordCountMap[word]) {
            wordCountMap[word]++;
          } else {
            wordCountMap[word] = 1;
          }
        });

        const wordCloudData = Object.entries(wordCountMap).map(([text, value]) => ({ text, value }));
        setWordCloudData(wordCloudData);
      } catch (error) {
        console.error('Error fetching word cloud data:', error);
      }
    };
    fetchData();
  }, []);
  
  return (
    <div className="home" style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
      <div className="chart-card" style={{ backgroundColor: '#f0f0f0' }}>
        <Bar
          style={{ width: '100%', height: '400px' }}
          xData={['positive', 'negative', 'neutral']}
          sData={[positive, negative, neutral]}
          title="Emotion statistics"
        />
      </div>

      <div className="chart-card" style={{}}>
      <ReactEcharts
          option={{
            title: {
              text: 'Emotional Pie Chart',
              left: 'left',
              top: 5
            },
            legend: {
              orient: 'vertical',
              left: '80%',
              data: ['positive', 'negative', 'neutral']
            },
            series: [
              {
                name: 'Emotion',
                type: 'pie',
                radius: '80%',
                avoidLabelOverlap: false,
                label: {
                  show: true,
                  formatter: '{b}: {c} ({d}%)',
                  position: 'outside'
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
          <Map3 />
        </div>
      </Draggable>
      <Draggable>
        <div className="chart-card wordcloud-container" style={{ backgroundColor: '#f0f0f0' }}>
          {wordCloudClicked && <MemoizedWordCloud words={wordCloudData} />}
        </div>
      </Draggable>
    </div>
  );
};

export default Home;
