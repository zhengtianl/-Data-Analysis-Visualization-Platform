
import React, {useRef, useEffect, useState } from 'react';
import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import { Layout, Button} from 'antd';
import Hospital_Statistics from '@/data/Hospital_Statistics.json';
import './Map.css';



var staticLayers = [];
mapboxgl.accessToken = 'pk.eyJ1IjoieWlmZXlhbmcxIiwiYSI6ImNrb251MG44ZzA0Njkyd3BweWFyMWJvcjYifQ.oEO3lpWd3GLwRu13euHIvA';

export default function Map() {
  var mapContainer = useRef(null);
  var map = useRef(null);
  const [lng, setLng] = useState(145.3607);
  const [lat, setLat] = useState(-37.8636);
  const [zoom, setZoom] = useState(7.96);

  useEffect(() => {
    if (map.current) return; // initialize map only once
    map.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: 'mapbox://styles/yifeyang1/ckp41vh7i0pli19o3x6fe84jh/draft',
      center: [lng, lat],
      zoom: zoom
    });
  });

  useEffect(() => {
    if (!map.current) return; // wait for map to initialize
    map.current.on('move', () => {
      setLng(map.current.getCenter().lng.toFixed(4));
      setLat(map.current.getCenter().lat.toFixed(4));
      setZoom(map.current.getZoom().toFixed(2));
    });
  });



  useEffect(() => {
    map.current.on('load', () => {
      map.current.loadImage('https://i.loli.net/2021/05/25/rdNiyRkwZWafj5x.png', function (error, image) {
        if (error) throw error;
        map.current.addImage('exclamation', image); //38x55px, shadow adds 5px
      });
      const aurinData = Hospital_Statistics.features;
      map.current.addSource('hospital_location', {
        type: 'geojson',
        data: {
          type: 'FeatureCollection',
          features: aurinData.map(hospital => {
            return {
              type: 'Feature',
              geometry: {
                type: 'Point',
                coordinates: hospital.geometry.coordinates,
              },
            };
          }),
        },
      });

      map.current.addLayer({
        'id': 'hospitals_loc',
        'type': 'symbol',
        'source': 'hospital_location',
        'layout': {
          // Make the layer visible by default.
          'icon-image': 'exclamation',
          'icon-size': 0.05,
        },
      });
      staticLayers.push('hospitals_loc');
    });
  }, []);

  const handleZoom = (action) => {
    if (action === 'in') {
      map.current.zoomIn();
    } else if (action === 'out') {
      map.current.zoomOut();
    }
  };
  


  return (
    <Layout style={{ minHeight: '200vh' }}>
      <Layout>
        <div className="legend">
          <span className="legend-item">
            <span className="legend-color" style={{ backgroundColor: 'rgba(0, 0, 0, 0.2)' }}></span>
            <span className="legend-label">Less Happy</span>
          </span>
          <span className="legend-item">
            <span className="legend-color" style={{ backgroundColor: 'rgba(1, 2, 3, 4)' }}></span>
            <span className="legend-label">More Happy</span>
          </span>
        </div>

        <div className='sidebar'>
          <div>Longitude: {lng} | Latitude: {lat} | Zoom: {zoom}</div>
        </div>
        <div ref={mapContainer} className="map-container" />
        <div className="map-buttons">
          <Button type='primary' onClick={() => handleZoom('in')}>Zoom In</Button>
          <Button type='primary' onClick={() => handleZoom('out')}>Zoom Out</Button>
        </div>
      </Layout>
    </Layout>
  ); 
}