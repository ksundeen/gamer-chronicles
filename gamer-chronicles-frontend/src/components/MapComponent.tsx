import { useEffect, useRef } from "react";
import maplibregl from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";
import SidePanel from "./SidePanel";

const geojsonData = {
  type: "FeatureCollection",
  features: [
    {
      type: "Feature",
      properties: {
        id: 1,
        name: "Catan",
        description: "Players take on the roles of settlers, each attempting to build and develop holdings while trading and acquiring resources. Players gain victory points as their settlements grow and the first to reach a set number of victory points, typically 10, wins.",
        designers: ["Klaus Teuber"],
        first_published_year: 1995,
        first_released_location: "Germany",
        game_type: ["board game"],
        game_genre: ["multiplayer", "strategy", "negotiation"],
        number_players: ["3-4", "5-6"],
        play_time: ["1-2 hours"],
        website: "http://catan.com/",
        image: "https://upload.wikimedia.org/wikipedia/en/thumb/a/a3/Catan-2015-boxart.jpg/250px-Catan-2015-boxart.jpg"
      },
      geometry: {
        type: "Point",
        coordinates: [10.451526, 51.165691]
      }
    },
    {
      type: "Feature",
      properties: {
        id: 2,
        name: "Donkey Kong Country",
        description: "It is a reboot of Nintendo's Donkey Kong franchise and follows the gorilla Donkey Kong and his nephew Diddy Kong as they set out to recover their stolen banana hoard from the crocodile King K. Rool and his army, the Kremlings. The player traverses 40 side-scrolling levels as they jump between platforms and avoid obstacles. They collect items, ride minecarts and animals, defeat enemies and bosses, and find secret bonus stages. In multiplayer modes, two players work cooperatively or race.",
        sources: ["https://en.wikipedia.org/wiki/Donkey_Kong_Country"],
        designers: ["Rare", "Gregg Mayles", "Chris Sutherland"],
        first_published_year: 1994,
        first_released_location: "United Kingdom",
        game_type: ["board game"],
        game_genre: ["platform", "multiplayer", "cooperative"],
        number_players: ["1-2"],
        play_time: ["5-15 hours"],
        website: "https://en.wikipedia.org/wiki/Donkey_Kong_Country",
        image: "https://upload.wikimedia.org/wikipedia/en/thumb/1/1a/Donkey_Kong_Country_SNES_cover.png/250px-Donkey_Kong_Country_SNES_cover.png"
      },
      geometry: {
        type: "Point",
        coordinates: [-3.435973, 55.378051]
      }
    }
  ]
};

const MapComponent = () => {
  const mapContainer = useRef<HTMLDivElement | null>(null);
  const mapRef = useRef<maplibregl.Map | null>(null); // Store the map instance

  useEffect(() => {
    if (!mapContainer.current || mapRef.current) return; // Ensure container exists and prevent re-initialization

    const map = new maplibregl.Map({
      container: mapContainer.current,
      style: "https://demotiles.maplibre.org/style.json",
      center: [9.0000, 53.0000],
      zoom: 10
    });

    map.addControl(new maplibregl.NavigationControl(), "top-right");

    // Store the map instance in ref
    mapRef.current = map;

    // Add markers from GeoJSON
    geojsonData.features.forEach(feature => {
      const { coordinates } = feature.geometry;
      const coordLatLng = {lng: coordinates[0], lat: coordinates[1]}
      const { name, description, game_genre, game_type, 
        number_players, play_time, image, first_published_year, first_released_location
    } = feature.properties;

      const popup = new maplibregl.Popup({ offset: 25 }).setHTML(
        `<div>
          <img src="${image}" width="100%" />
          <h3>${name}</h3>
          <p>${description}</p>
          <div>${game_genre}</div>
          <div>${game_type}</div>
          <div>${number_players}</div>
          <div>${play_time}</div>
          <div>${first_published_year}</div>
          <div>${first_released_location}</div>
        </div>`
      );

      new maplibregl.Marker().setLngLat(coordLatLng).setPopup(popup).addTo(map);
    });

    return () => {
        if (mapRef.current) {
          mapRef.current.remove(); // Clean up when component unmounts
          mapRef.current = null;
        }
      };
    }, []);

  return (
    <div style={{ height: "100vh", width: "100vw" }}>
      <SidePanel />
      <div ref={mapContainer} style={{ height: "100%", width: "100%" }} />
    </div>
  );
};

export default MapComponent;
