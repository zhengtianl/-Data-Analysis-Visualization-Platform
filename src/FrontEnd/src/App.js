// 导入路由
import {Route, Routes } from 'react-router-dom'
// 导入页面组件
import { history } from './utils/history'
import Layout from './pages/Layout'
import Login from '@/pages/Login'
import '@/App.css'
import { AuthRoute } from './components/AuthRoute'
import Article from './pages/Article'
import Home from './pages/Home'
import Publish from './pages/Publish'
import { unstable_HistoryRouter as HistoryRouter } from 'react-router-dom'
// 配置路由规则
function App() {
  return (
    <HistoryRouter history={history}>
      <div className="App">
        <Routes>
            {/*需要鉴权*/}
            <Route path="/" element={
              <AuthRoute>
                <Layout />
              </AuthRoute>
            }>
              <Route index element={<Home />} />
              <Route path="article" element={<Article />} />
              <Route path="Publish" element={<Publish />} />
            </Route>
            <Route path="/login" element={<Login/>}/>
        </Routes>
      </div>
    </HistoryRouter>
  )
}

export default App