import Bar from "@/components/Bar"
import './index.scss'
import React, {useEffect, useState} from 'react';
import ReactEcharts  from 'echarts-for-react';
import axios from "axios";

const Home = () => {
    const [negative, setNegative] = useState(null);
    const [neutral, setNeutral] = useState(null);
    const [positive, setPositive] = useState(null);
  
    useEffect(() => {
      axios.get('http://127.0.0.1:5000/sentiment')
        .then(response => {
          const sentimentList = response.data.sentiment_list;
          setNegative(sentimentList.negative);
          setNeutral(sentimentList.neutral);
          setPositive(sentimentList.positive);
          console.log(sentimentList);
        })
        .catch(error => {
          console.log(error);
        });
    }, []);

    const options = {
            grid: { top: 8, right: 8, bottom: 24, left: 36 },
            xAxis: {
                type: 'category',
                data: ['positive', 'negative', 'neutral'],
            },
            yAxis: {
                type: 'value',
            },
            series: [
                {
                    data: [negative, neutral, positive],
                    type: 'line',
                    smooth: true,
                },
            ],
            tooltip: {
                trigger: 'axis',
            },
        };

    

    return (
    <div className="home">
        <Bar
        style={{ width: '500px', height: '400px' }}
        xData={['positive', 'negative', 'neutral']}
        sData={[positive, negative, neutral]}
        title='Emotion statistics'/>

        <Bar
        style={{ width: '500px', height: '400px' }}
        xData={['vue', 'angular', 'react']}
        sData={[negative, negative, positive]}
        title='Area '/>
        <ReactEcharts option={options} />;
        <ReactEcharts
            option={{
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b}: {c} ({d}%)'
                },
                legend: {
                    orient: 'vertical',
                    left: 10,
                    data: ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
                },
                series: [
                    {
                        name: 'Utilization',
                        type: 'pie',
                        radius: ['50%', '70%'],
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
                        labelLine: {
                            show: false
                        },
                        data: [
                            {value: 335, name: 'positive'},
                            {value: 310, name: 'negative'},
                            {value: 234, name: 'neutral'},
                        ]
                    }
                ]
            }}
        />
    </div>
  )
}

export default Home