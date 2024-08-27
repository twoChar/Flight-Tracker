import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Flights = () => {
  const [flights, setFlights] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/flights')
      .then(response => {
        setFlights(response.data);
      })
      .catch(error => {
        console.error('Error fetching flights data:', error);
        setError(error);
      });
  }, []);

  return (
    <div>
      {error && <div style={{color: 'red'}}>Error: {error.message}</div>}
      {flights.length === 0 && !error && <div>Loading flights...</div>}
      {flights.map(flight => (
        <div key={flight.flight_id}>
          <h3>{flight.airline} - {flight.flight_id}</h3>
          <p>Status: {flight.status}</p>
          <p>Departure Gate: {flight.departure_gate}</p>
          <p>Arrival Gate: {flight.arrival_gate}</p>
          <p>Scheduled Departure: {new Date(flight.scheduled_departure).toLocaleString()}</p>
          <p>Scheduled Arrival: {new Date(flight.scheduled_arrival).toLocaleString()}</p>
        </div>
      ))}
    </div>
  );
};

export default Flights;
