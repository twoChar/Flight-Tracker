
import React, { useEffect, useState } from "react";
import axios from "axios";

function FlightStatus() {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/flights")
      .then(response => {
        setFlights(response.data);
      })
      .catch(error => {
        console.error("Error fetching flights data:", error);
      });
  }, []);

  return (
    <div className="container">
      <h1>Flight Status</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Flight ID</th>
            <th>Airline</th>
            <th>Status</th>
            <th>Departure Gate</th>
            <th>Arrival Gate</th>
            <th>Scheduled Departure</th>
            <th>Scheduled Arrival</th>
          </tr>
        </thead>
        <tbody>
          {flights.map((flight, index) => (
            <tr key={index}>
              <td>{flight.flight_id}</td>
              <td>{flight.airline}</td>
              <td>{flight.status}</td>
              <td>{flight.departure_gate}</td>
              <td>{flight.arrival_gate}</td>
              <td>{new Date(flight.scheduled_departure).toLocaleString()}</td>
              <td>{new Date(flight.scheduled_arrival).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default FlightStatus;
