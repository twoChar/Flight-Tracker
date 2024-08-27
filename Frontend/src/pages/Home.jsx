import React, { useEffect, useState } from "react";
import { BrowserRouter, Route, Link } from "react-router-dom";
import "./home.css";
function Home() {
  const [aircraftTableVisibility, setAircraftTableVisibility] =
    useState("d-none");
  const [aircraftNoResultsVisibility, setAircraftNoResultsVisibility] =
    useState("d-none");
  const [searchedAircraft, setSearchedAircraft] = useState(
    '{"ICAOTypeCode":"","Manufacturer":"Unknown","ModeS":"","OperatorFlagCode":"","RegisteredOwners":"Unknown","Registration":"","Type":""}'
  );
  const [aircraftInfoUrl, setAircraftInfoUrl] = useState("#");
  const [airportTableVisibility, setAirportTableVisibility] =
    useState("d-none");
  const [airportNoResultsVisibility, setAirportNoResultsVisibility] =
    useState("d-none");
  const [searchedAirport, setSearchedAirport] = useState(
    '{"airport":"n/a","country_code":"","iata":"Unknown","icao":"Unknown","latitude":0,"longitude":0,"region_name":"n/a"}'
  );
  const [airportInfoUrl, setAirportInfoUrl] = useState("#");

  function handleChange2(event) {
    var airportFetchUrl =
      "https://hexdb.io/api/v1/airport/iata/";

    if (event.target.value.length === 3 || event.target.value.length === 4) {
      if (event.target.value.length === 3) {
        airportFetchUrl =
          "https://hexdb.io/api/v1/airport/iata/";
      }
      if (event.target.value.length === 4) {
        airportFetchUrl =
          "https://hexdb.io/api/v1/airport/icao/";
      }
      fetch(airportFetchUrl + event.target.value)
        .then((response) => response.json())
        .then((responseData) => {
          console.log(responseData);
          setSearchedAirport(responseData);
          setAirportInfoUrl("airport/" + responseData.icao);
          if (typeof responseData.icao !== "undefined") {
            setAirportNoResultsVisibility("d-none");
            setAirportTableVisibility("d-block");
          } else {
            setAirportTableVisibility("d-none");
            setAirportNoResultsVisibility("d-block");
          }
        })
        .catch((e) => {
          setSearchedAirport(
            '{"airport":"n/a","country_code":"","iata":"Unknown","icao":"Unknown","latitude":0,"longitude":0,"region_name":"n/a"}'
          );
          setAirportTableVisibility("d-none");
          setAirportNoResultsVisibility("d-block");
        });
    } else {
      setAirportTableVisibility("d-none");
      setAirportNoResultsVisibility("d-none");
    }
  }

  return (
    <>
      <nav
        id="nav-home"
        className="navbar navbar-expand navbar-dark bg-dark"
      >
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
          <img className="navbar-logo" src="./logo192.png" /> Real-Time Flight Tracker
          </Link>
          <button
            className="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbar01"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
        </div>
      </nav>
      <section
        className="jumbotron text-light text-left"
        style={{ "backgroundImage": "url(./jumbotron-background.png)" }}
      >
        <div className="container">
          <div className="row">
            <div className="col-md-8">
              <h1 className="display-4">Flights Status</h1>
              <p className="lead">
                This is real-time flight tracker website shows Flight Status, Flights on a map (where you can click on an aircraft for more information) and can send notification.</p>
              <p>
                <Link
                  id="lnk"
                  to="map"
                  className="btn btn-info btn-lg mt-2 ml-2"
                >
                  View map
                </Link>
                <Link id="lnk" to="flight-status" className="btn btn-info btn-lg mt-2 ml-2">
                  Flight Status
                </Link>
                <Link id="lnk" to="send-notification" className="btn btn-info btn-lg mt-2 ml-2">
                  Send Notification
                </Link>
              </p>
            </div>
            <div className="col-md-4 d-none d-md-block">  
              <img className="jumbotron-img" src="./jumbotron-image.png" />
            </div>
          </div>
        </div>
      </section>
      <div className="container features-container pb-5">
        <h1 className="text-center">Search</h1>
        <div className="row mt-5">

          <div className="col-md-6">
            <h3>Search by airport</h3>

            <input
              className="form-control"
              type="text"
              onChange={handleChange2}
              maxLength="4"
              id="search-by-reg"
              placeholder="Enter airport registration"
            />
            <h5 className={airportNoResultsVisibility}>No results found</h5>
            <div className={airportTableVisibility}>
              <table
                className="mt-2 text-center border"
                style={{ width: "100%" }}
                id="airport-search-result"
              >
                <thead className="bg-success text-light">
                  <tr>
                    <th>Airport</th>
                    <th>ICAO</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>
                      <Link to={airportInfoUrl}>{searchedAirport?.airport}</Link>
                    </td>
                    <td>{searchedAirport?.icao}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Home;
