import React, { useEffect, useRef } from 'react';
import mapboxgl from 'mapbox-gl';
import './Map.css';

mapboxgl.accessToken = 'pk.eyJ1IjoieWlmZXlhbmcxIiwiYSI6ImNrb251MG44ZzA0Njkyd3BweWFyMWJvcjYifQ.oEO3lpWd3GLwRu13euHIvA';

const SydMap = () => {
  const mapContainer = useRef(null);

  useEffect(() => {
    const map = new mapboxgl.Map({
      container: mapContainer.current,
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [151.2093, -33.8688], // Syd coordinates
      zoom: 10,
    });

    // Add map controls
    map.addControl(new mapboxgl.NavigationControl());

    return () => {
      map.remove(); // Clean up map instance on unmount
    };
  }, []);

  return <div ref={mapContainer} style={{ height: '400px' }} />;
};

export default SydMap;
