import { observer } from 'mobx-react-lite'
import './index.scss'
import 'react-quill/dist/quill.snow.css'
import { useState, useEffect } from 'react'
import axios from 'axios'

const Publish = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/sentiment')
      .then(response => {
        setData(response.data);
        console.log(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div className="Covid-19">
      {data && (
        <div>
          <h3>Positive: {data.sentiment_list.negative}</h3>
          <h3>Negative: {data.sentiment_list.positive}</h3>
          <h3>Neutral: {data.sentiment_list.neutral}</h3>
        </div>
      )}
    </div>
  )
}

export default observer(Publish)
