import React, { useEffect, useRef } from 'react';
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';
import './Map.css';
import MelbourneData from './melbourne.geojson';

mapboxgl.accessToken = 'pk.eyJ1IjoieWlmZXlhbmcxIiwiYSI6ImNrb251MG44ZzA0Njkyd3BweWFyMWJvcjYifQ.oEO3lpWd3GLwRu13euHIvA';

const MelbourneMap = () => {
  const mapContainer = useRef(null);

  useEffect(() => {
    const map = new mapboxgl.Map({
      container: mapContainer.current,
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [144.9631, -37.8136], // Melbourne's coordinates
      zoom: 10,
    });

    // Add map controls
    map.addControl(new mapboxgl.NavigationControl());

    // Add GeoJSON source and layer
    map.on('load', () => {
      map.addSource('melbourne-data', {
        type: 'geojson',
        data: MelbourneData, // 使用 melbourne.geojson 文件
      });

      map.addLayer({
        id: 'melbourne-layer',
        type: 'fill',
        source: 'melbourne-data',
        paint: {
          'fill-color': [
            'match', // 使用 match 表达式
            ['get', 'cartodb_id'], // 获取 cartodb_id 属性
            31, '#ff0000', // 当 cartodb_id 为 31 时的颜色
            42, '#00ff00', // 当 cartodb_id 为 42 时的颜色
            '#0000ff' // 默认颜色（浅蓝色）
          ],
          'fill-opacity': 0.8,
        },
      });
    });

    return () => {
      map.remove();
    };
  }, []);

  return <div ref={mapContainer} className="map-container" />;
};

export default MelbourneMap;
