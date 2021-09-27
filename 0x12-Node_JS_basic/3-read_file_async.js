#!/usr/bin/node
const fs = require('fs');

function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, (err, data) => {
      if (err) {
        return reject(Error('Cannot load the database'));
      }

      const arrayObject = [];
      const newObject = {};

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
      return resolve(arrayObject);
    });
  });
}

module.exports = countStudents;
