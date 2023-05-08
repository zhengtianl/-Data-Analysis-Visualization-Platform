import { observer } from 'mobx-react-lite'
import './index.scss'
import 'react-quill/dist/quill.snow.css'
import { useState, useEffect } from 'react'
import axios from 'axios'

const Publish = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/data')
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
          <h3>Positive: {data.positive}</h3>
          <h3>Negative: {data.negative}</h3>
          <h3>Neutral: {data.neutral}</h3>
        </div>
      )}
    </div>
  )
}

export default observer(Publish)
