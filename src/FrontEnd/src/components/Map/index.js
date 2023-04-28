import React, { useRef, useEffect, useState } from 'react';
import mapboxgl from 'mapbox-gl';

mapboxgl.accessToken = 'pk.eyJ1IjoieWlmZXlhbmcxIiwiYSI6ImNrb251MG44ZzA0Njkyd3BweWFyMWJvcjYifQ.oEO3lpWd3GLwRu13euHIvA';

function Map() {
    const mapContainer = useRef(null);
    const map = useRef(null);
    const [lng, setLng] = useState(-122.4194);
    const [lat, setLat] = useState(37.7749);
    const [zoom, setZoom] = useState(10);

    useEffect(() => {
        if (map.current) return;
        map.current = new mapboxgl.Map({
            container: mapContainer.current,
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [144.9631, -37.8136],
            zoom: zoom
        });
    });

    useEffect(() => {
        if (!map.current) return;
        map.current.on('move', () => {
            setLng(map.current.getCenter().lng.toFixed(4));
            setLat(map.current.getCenter().lat.toFixed(4));
            setZoom(map.current.getZoom().toFixed(2));
        });
    });

    useEffect(() => {
        if (map.current) return;
        map.current = new mapboxgl.Map({
            container: mapContainer.current,
            style: {
                version: 8,
                sources: {
                    'my-data': {
                        type: 'geojson',
                        data: 'my-data.geojson'
                    }
                },
                layers: [
                    {
                        id: 'my-data-layer',
                        type: 'heatmap',
                        source: 'my-data',
                        paint: {
                            'heatmap-weight': {
                                property: 'density',
                                type: 'exponential',
                                stops: [
                                    [0, 0],
                                    [100, 1]
                                ]
                            },
                            'heatmap-intensity': 1.5,
                            'heatmap-color': [
                                'interpolate',
                                ['linear'],
                                ['heatmap-density'],
                                0, 'rgba(0, 0, 255, 0)',
                                0.2, 'royalblue',
                                0.4, 'cyan',
                                0.6, 'lime',
                                0.8, 'yellow',
                                1, 'red'
                            ],
                            'heatmap-radius': {
                                stops: [
                                    [1, 10],
                                    [6, 60]
                                ]
                            }
                        }
                    }
                ]
            },
            center: [144.9631, -37.8136],
            zoom: zoom
        });
      });
      


    return (
        <div>
            <div className="sidebar">
                Longitude: {lng} | Latitude: {lat} | Zoom: {zoom}
            </div>
            <div ref={mapContainer} className="map-container" style={{ height: '800px' }} />
        </div>
    );
}

export default Map;
