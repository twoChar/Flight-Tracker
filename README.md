# flight-tracker-reactjs
A reactjs website that displays current flying planes on a map, showing details about each flight.

Examples:

![Example 1](https://raw.githubusercontent.com/reemrizzk/flight-tracker-reactjs/main/example1.png)

![Example 2](https://raw.githubusercontent.com/reemrizzk/flight-tracker-reactjs/main/example2.png)

## Features

1- Display current fetched flights on a map, ability to filter aircraft on map by call sign, you can hover on an aircraft to view the Call sign (If available), or click on it to view information about the flight, which can include:
- Call sign
- Aircraft type
- Registration
- Airline
- Route
- Altitude in feet
- Ground speed in Km/h

3- You can click "View flight" to display live flight path on the map, which auto refreshes every 10 seconds. if you want it to refresh more often, go to the file src\pages\Flight\FlightInfo.jsx ,  and at line 318: 
```
}, 10000); // How often flight status refreshes in milliseconds, change to a smaller number if you want it to refresh more often
```
you can change 10000 to another number, where the number equals amount of seconds multiplied by 10.

4- Information about airports, and recent arrivals and departures (if available).

5- Searching by aircraft registration or airport code.

## Packages used

1- react-router

2- react-leaflet

## Other resources and APIs used

1- The app uses [OpenSky Network API](https://opensky-network.org/) for information about flights to be displayed on the map. OpenSky network API has request limitations of 100 API requests per day for anonymous users or 1000 API requests per day for registered users.

2- The app uses [hexdb.io API](https://hexdb.io/) for information about Aircraft, call signs, and airports.

3- The app uses [Country Flags API](https://countryflagsapi.com) for flag images.

4- The app retreives most recent available image of aircraft from [JetPhotos](http://jetphotos.com/). Link is retreived from [hexdb.io API](https://hexdb.io/).

5-The app uses [LeafletJs](https://leafletjs.com/) with [OpenStreetMap](https://www.openstreetmap.org/) for the map.


## How to run project

1- First you need to install [NodeJs](https://nodejs.org/en/)

2- Clone this repository, and in the terminal, run:

### `npm install`

3- In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

