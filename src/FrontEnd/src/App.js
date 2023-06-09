// 导入路由
import {Route, Routes } from 'react-router-dom'
// 导入页面组件
import { history } from './utils/history'
import Layout from './pages/Layout'
import Login from '@/pages/Login'
import '@/App.css'
import Map from './pages/Map'
import Home from './pages/Home'
import Unemployment from './pages/Publish'
import { unstable_HistoryRouter as HistoryRouter } from 'react-router-dom'
// 配置路由规则
function App() {
  return (
    <HistoryRouter history={history}>
      <div className="App">
        <Routes>
        <Route path="/login" element={<Login/>}/>
              <Route path="/" element={<Layout />}>
              <Route index element={<Home/>} />
              <Route path="map" element={<Map />} />
              <Route path="Unemployment" element={<Unemployment />} />
            </Route>
            
        </Routes>
      </div>
    </HistoryRouter>
  )
}

export default App




