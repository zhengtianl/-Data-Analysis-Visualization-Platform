import { Card, Button } from 'antd'
import './index.scss'
import { useState, useEffect } from 'react';

const CoverPages = () => {

  const [time, setTime] = useState(new Date().toLocaleTimeString());

  useEffect(() => {
    const interval = setInterval(() => {
      setTime(new Date().toLocaleTimeString());
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="login">
      <Button className='but'htmlType="submit" size="large" block>
        Click open the world
      </Button>
      <Card className='time' >{time}</Card>
    </div>
  )
}

export default CoverPages;
