const fs = require('fs');

function countStudents(filePath) {
  const arrayObject = [];
  const newObject = {};
  let i;
  try {
    const data = fs.readFileSync(filePath);
    const arrayString = data.toString().split('\n');
    const subArray = arrayString[0].split(',');

    for (i = 1; i < arrayString.length - 1; i += 1) {
      if (arrayString[i] !== '') for (let iter1 = 0; iter1 < subArray.length; iter1 += 1) newObject[subArray[iter1]] = arrayString[i].split(',')[iter1];

      arrayObject.push({ ...newObject });
    }
    console.log(`Number of students: ${arrayObject.length}`);
    // console.log(arrayObject);
    const fieldcs = arrayObject.filter((item) => item.field === 'CS');
    const fieldswe = arrayObject.filter((item) => item.field === 'SWE');
    console.log(`Number of students in CS: ${fieldcs.length}. List: ${fieldcs.map((item) => item.firstname).join(', ')}`);
    console.log(`Number of students in SWE: ${fieldswe.length}. List: ${fieldswe.map((item) => item.firstname).join(', ')}`);
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
