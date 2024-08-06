#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Define a recursive function to handle the character requests
const req = (dt, i) => {
  // Base case: if we've reached the end of the array, return
  if (i === dt.length) return;

  // Make a request to the current character URL
  request(dt[i], (err, response, body) => {
    // Handle any errors that occur during the request
    if (err) {
      throw err;
    } else {
      // Parse the response body as JSON and log the character name
      console.log(JSON.parse(body).name);

      // Recursively call the function with the next character URL
      req(dt, i + 1);
    }
  });
};

// Make a request to the specified film endpoint
request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    // Handle any errors that occur during the request
    if (err) {
      throw err;
    } else {
      // Parse the response body as JSON and get the character URLs
      const characts = JSON.parse(body).characters;

      // Call the recursive function to fetch the character names
      req(characts, 0);
    }
  }
);
