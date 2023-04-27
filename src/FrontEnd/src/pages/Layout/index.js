import { Layout, Menu, Popconfirm } from 'antd'
import {
  HomeOutlined,
  DiffOutlined,
  EditOutlined,
  LogoutOutlined
} from '@ant-design/icons'
import './index.scss'
import { Outlet, Link, useLocation,useNavigate } from 'react-router-dom'
import { useStore } from '@/store'
import { useEffect } from 'react'
import { observer } from 'mobx-react-lite'
const { Header, Sider } = Layout

const GeekLayout = () => {
  const { pathname } = useLocation()
  const { userStore, loginStore, channelStore } = useStore()
  const navigate = useNavigate()
  //console.log(pathname)
  useEffect(() => {
    userStore.getUserInfo() 
    channelStore.loadChannelList()
   }, [userStore,channelStore])
  const confirm = () => {
    loginStore.loginOut()
    navigate('/login')
  };
  return (
    <Layout>
      <Header className="header">
        <div className="user-info">
          <span className="user-logout">
            <Popconfirm 
            onConfirm={confirm}
            title="Confirm to Exit"
            okText="Exit"
            cancelText="Cancel">
              <LogoutOutlined /> Exit
            </Popconfirm>
          </span>
        </div>
      </Header>
      <Layout>
        <Sider width={200} className="site-layout-background">
          <Menu
            mode="inline"
            theme="dark"
            defaultSelectedKeys={[pathname]}
            style={{ height: '100%', borderRight: 0 }}
          >
            <Menu.Item icon={<HomeOutlined />} key="/">
              <Link to={'/'}>Emotional</Link>
            </Menu.Item>
            <Menu.Item icon={<DiffOutlined />} key="/article">
              <Link to={'/article'}>Area</Link>
            </Menu.Item>
            <Menu.Item icon={<EditOutlined />} key="/publish">
              <Link to ={'/publish'}>Covid-19</Link>
            </Menu.Item>
          </Menu>
        </Sider>
        <Layout className="layout-content" style={{ padding: 20 }}>
          <Outlet />
        </Layout>
      </Layout>
    </Layout>
  )
}

export default observer(GeekLayout)