import React from 'react';
import './index.scss';
import { observer } from 'mobx-react-lite';
import Map from '@/components/Map';
import { Card } from 'antd';
import Draggable from 'react-draggable';
import MelbourneMap from '@/components/Map/melbourneMap';
import SydMap from '@/components/Map/SydMap';
import Brisban from '@/components/Map/Brisban';
import PerthMap from '@/components/Map/PerthMap';
const Article = () => {
  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <div style={{ flex: 1 }}>
        <Map />
      </div>
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        <Draggable>
          <Card style={{ flex: 1 }}>
            <div style={{ height: '100%' }}>
              <PerthMap />
            </div>
          </Card>
        </Draggable>
        <div style={{ display: 'flex', flex: 1 }}>
          <Draggable>
            <Card style={{ flex: 1 }}>
              <div style={{ height: '100%' }}>
                <MelbourneMap />
              </div>
            </Card>
          </Draggable>
          <Draggable>
            <Card style={{ flex: 1 }}>
              <div style={{ height: '100%' }}>
                <SydMap></SydMap>
              </div>
            </Card>
          </Draggable>
        </div>
        <Draggable>
          <Card style={{ flex: 1 }}>
            <div style={{ height: '100%' }}>
              <Brisban />
            </div>
          </Card>
        </Draggable>
      </div>
    </div>
  );
};

export default observer(Article);
