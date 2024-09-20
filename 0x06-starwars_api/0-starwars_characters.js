#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/people/' + process.argv[2];

console.log(url);
