#!/usr/bin/node
const fs = require('fs');

function countStudents(filePath) {
  let data;
  const arrayObject = [];
  const newObject = {};

  try {
    data = fs.readFileSync(filePath);
  } catch (error) {
    throw new Error('Cannot load the database');
  }
  const arrayString = data.toString().split('\n');
  const subArray = arrayString[0].split(',');

  for (const i in arrayString) {
    if (arrayString[i] !== '' && i !== 0) {
      for (let iter1 = 0; iter1 < subArray.length; iter1 += 1) {
        newObject[subArray[iter1]] = arrayString[i].split(',')[iter1];
      }
      arrayObject.push({ ...newObject });
    }
  }
  arrayObject.shift();
  console.log(`Number of students: ${arrayObject.length}`);
  const fieldcs = arrayObject.filter((item) => item.field === 'CS');
  const fieldswe = arrayObject.filter((item) => item.field === 'SWE');
  console.log(`Number of students in CS: ${fieldcs.length}. List: ${fieldcs.map((item) => item.firstname).join(', ')}`);
  console.log(`Number of students in SWE: ${fieldswe.length}. List: ${fieldswe.map((item) => item.firstname).join(', ')}`);
}

module.exports = countStudents;
