import React from "react"

import UserStore from './user.Store'
import ChannelStore from "./channel.Store"
class RootStore {
  // 组合模块
  constructor() {
    this.userStore = new UserStore()
    this.channelStore = new ChannelStore()
  }
}

const StoresContext = React.createContext(new RootStore())
export const useStore = () => React.useContext(StoresContext)