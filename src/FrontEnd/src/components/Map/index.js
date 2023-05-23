import React, { useRef, useEffect, useState } from 'react';
import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import { Layout, Button } from 'antd';
import './Map.css';

mapboxgl.accessToken = 'pk.eyJ1IjoieWlmZXlhbmcxIiwiYSI6ImNrb251MG44ZzA0Njkyd3BweWFyMWJvcjYifQ.oEO3lpWd3GLwRu13euHIvA';

export default function Map() {
  const mapContainer = useRef(null);
  const map = useRef(null);
  const [lng, setLng] = useState(133.7751); // Australia's longitude
  const [lat, setLat] = useState(-25.2744); // Australia's latitude
  const [zoom, setZoom] = useState(4); // Initial zoom level

  useEffect(() => {
    if (map.current) return; // Initialize map only once
    map.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: 'mapbox://styles/yifeyang1/ckp41vh7i0pli19o3x6fe84jh/draft',
      center: [lng, lat],
      zoom: zoom
    });

    map.current.on('load', () => {
      // Add heatmap layer
      map.current.addSource('heatmap-data', {
        type: 'geojson',
        data: {
          type: 'FeatureCollection',
          features: [
            // Sydney data
            {
              type: 'Feature',
              properties: {
                intensity: 1 // Sydney's intensity set to 1
              },
              geometry: {
                type: 'Point',
                coordinates: [151.2093, -33.8688] // Sydney's coordinates
              }
            },
            // Melbourne data
            {
              type: 'Feature',
              properties: {
                intensity: 0.8 // Melbourne's intensity set to 0.8
              },
              geometry: {
                type: 'Point',
                coordinates: [144.9631, -37.8136] // Melbourne's coordinates
              }
            },

            {
              "type": "Feature",
              "properties": {
                "intensity": 0.5 
              },
              "geometry": {
                "type": "Point",
                "coordinates": [153.0251, -27.4698] //
              }
            },


            {
              "type": "Feature",
              "properties": {
                "intensity": 0.328 // 墨尔本的强度为0.8
              },
              "geometry": {
                "type": "Point",
                "coordinates": [138.6535, -34.9353] //
              }
            },


            {
              "type": "Feature",
              "properties": {
                "intensity": 0.1
              },
              "geometry": {
                "type": "Point",
                "coordinates": [147.0229, -32.2176] //
              }
            },



            {
              "type": "Feature",
              "properties": {
                "intensity": 0.2 
              },
              "geometry": {
                "type": "Point",
                "coordinates": [115.8799, -31.9423] //
              }
            },

            {
              "type": "Feature",
              "properties": {
                "intensity": 0.3 // 墨尔本的强度为0.8
              },
              "geometry": {
                "type": "Point",
                "coordinates": [149.1499, -32.6516] //
              }
            },
          ]
        }
      });

      map.current.addLayer({
        id: 'heatmap-layer',
        type: 'heatmap',
        source: 'heatmap-data',
        paint: {
          'heatmap-color': [
            'interpolate',
            ['linear'],
            ['heatmap-density'],
            0,
            'rgba(0, 0, 0, 0)', // Lowest density color (transparent)
            1,
            'rgba(255, 0, 0, 1)' // Highest density color (red)
          ],
          'heatmap-opacity': 0.8, // Opacity of the heatmap layer
          'heatmap-intensity': [
            'interpolate',
            ['linear'],
            ['zoom'],
            0,
            1,
            9,
            3
          ] // Intensity of the heatmap layer based on zoom level
        }
      });
    });
  }, [lng, lat, zoom]);

  useEffect(() => {
    if (!map.current) return; // Wait for map to initialize
    map.current.on('move', () => {
      setLng(map.current.getCenter().lng.toFixed(4));
      setLat(map.current.getCenter().lat.toFixed(4));
      setZoom(map.current.getZoom().toFixed(2));
    });
  });

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
            <span className="legend-label">unemployment rate</span>
          </span>
        </div>

        <div className="sidebar">
          <div>Longitude: {lng} | Latitude: {lat} | Zoom: {zoom}</div>
        </div>
        <div ref={mapContainer} className="map-container" />
        <div className="map-buttons">
          <Button type="primary" onClick={() => handleZoom('in')}>
            Zoom In
          </Button>
          <Button type="primary" onClick={() => handleZoom('out')}>
            Zoom Out
          </Button>
        </div>
      </Layout>
    </Layout>
  );
}
