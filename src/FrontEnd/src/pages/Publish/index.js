import { observer } from 'mobx-react-lite'
import './index.scss'
import 'react-quill/dist/quill.snow.css'
import { useState, useEffect } from 'react'
import { http } from '@/utils/http'

const Publish = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    http.get('/sentiment')
      .then(response => {
        setData(response);
        console.log(response);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div className="Covid-19">
      {data && (
        <div>
          <h3>Positive: {data.sentiment_list.positive}</h3>
          <h3>Negative: {data.sentiment_list.negative}</h3>
          <h3>Neutral: {data.sentiment_list.neutral}</h3>
        </div>
      )}
    </div>
  )
}

export default observer(Publish)
