import React from 'react';
import ReactWordcloud from 'react-wordcloud';
import "./style.css"

const WordCloud = ({ words }) => {
  const options = {
    colors: ['#0000ff', '#00ff00', '#ff0000', '#ffff00', '#ff00ff', '#800080', '#008080'],
    enableTooltip: true,
    deterministic: true,
    rotations: 3,
    rotationAngles: [-90, 0, 90],
    fontSizes: [30, 100],
    scale: 'sqrt',
    spiral: 'archimedean',
    padding: 1,
    fontStyle: 'oblique', // 
    fontFamily: 'Arial, sans-serif',
  };

  return (
    <div className="wordcloud-container">
      <h2 className="wordcloud-title">Mastodon Word Cloud</h2>
      <ReactWordcloud words={words} options={options} />
    </div>
  );
};

export default WordCloud;
