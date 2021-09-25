#!/usr/bin/node
const displayMessage = (greeting) => {
  process.stdout.write(`${greeting}\n`);
};

module.exports = displayMessage;
