#!/usr/bin/node
// prints all characters of a Star Wars movie
const req = require('request');
const num = process.argv[2] + '/';
const link = 'https://swapi-api.hbtn.io/api/films/';

req(link + num, async function (e, result, body) {
  if (e) return console.error(e);
  const linklist = JSON.parse(body).characters;
  for (const a of linklist) {
    await new Promise(function (resolve, reject) {
      req(a, function (e, result, body) {
        if (e) return console.error(e);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
