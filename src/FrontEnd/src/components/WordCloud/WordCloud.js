import React from 'react';
import ReactWordcloud from 'react-wordcloud';

const WordCloud = ({ words }) => {
  const options = {
    colors: ['#0000ff', '#00ff00', '#ff0000', '#ffff00', '#ff00ff'], // 自定义词云的颜色
    enableTooltip: true,
    deterministic: true,
    rotations: 3,
    rotationAngles: [-90, 0, 90],
    fontSizes: [10, 60], // 字体大小范围
    scale: 'sqrt',
    spiral: 'archimedean',
    padding: 1,
  };

  return <ReactWordcloud words={words} options={options} />;
};

export default WordCloud;
