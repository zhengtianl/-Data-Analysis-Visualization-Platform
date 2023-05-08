import { Button } from 'antd';
import { useNavigate } from 'react-router-dom';
import './index.scss';
import { useState, useEffect } from 'react';

function Login() {
  const navigate = useNavigate();
  const [currentTime, setCurrentTime] = useState('');
  
  useEffect(() => {
    const intervalId = setInterval(() => {
      const now = new Date();
      const hours = now.getHours().toString().padStart(2, '0');
      const minutes = now.getMinutes().toString().padStart(2, '0');
      const seconds = now.getSeconds().toString().padStart(2, '0');
      setCurrentTime(`${hours}:${minutes}:${seconds}`);
    }, 1000);
    return () => clearInterval(intervalId);
  }, []);



  async function onFinish() {
    navigate('/home', { replace: true });
  }

  return (
    <div className="login">
      <div className="time">{currentTime}</div>
      <Button className='but' type="primary" size="large" block onClick={onFinish}>
        Click open the world
      </Button>
      <audio controls autoplay>
        <source src={require('@/assets/bgm.mp3')} type="audio/mpeg" />
      </audio>

    </div>
  );
}

export default Login;
