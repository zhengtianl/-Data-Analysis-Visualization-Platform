import Bar from "@/components/Bar"
import './index.scss'
import React from 'react';
import ReactEcharts  from 'echarts-for-react';
const Home = () => {
        const options = {
            grid: { top: 8, right: 8, bottom: 24, left: 36 },
            xAxis: {
                type: 'category',
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            },
            yAxis: {
                type: 'value',
            },
            series: [
                {
                    data: [820, 932, 901, 934, 1290, 1330, 1320],
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
        sData={[100000, 20000, 60000]}
        title='Emotion statistics'/>


        <Bar
        style={{ width: '500px', height: '400px' }}
        xData={['vue', 'angular', 'react']}
        sData={[50, 60, 70]}
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