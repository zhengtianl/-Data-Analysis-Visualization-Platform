import './index.scss'
import { observer } from 'mobx-react-lite'
import Map from "@/components/Map"

const Article = () => {

  return (
    <div>
      <Map></Map>
    </div>
  )
}

export default observer(Article)