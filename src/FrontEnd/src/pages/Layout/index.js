import { Layout, Menu, Popconfirm } from 'antd'
import {
  HomeOutlined,
  DiffOutlined,
  EditOutlined,
  LogoutOutlined
} from '@ant-design/icons'
import './index.scss'
import { Outlet, Link, useLocation,useNavigate } from 'react-router-dom'
import { observer } from 'mobx-react-lite'
const { Header, Sider } = Layout

const GeekLayout = () => {
  const { pathname } = useLocation()
  const navigate = useNavigate()
  //console.log(pathname)
  const confirm = () => {
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
            <Menu.Item icon={<DiffOutlined />} key="/map">
              <Link to={'/map'}>Area</Link>
            </Menu.Item>
            <Menu.Item icon={<EditOutlined />} key="/Unemployment">
              <Link to ={'/Unemployment'}>Unemployment and Alcohol</Link>
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