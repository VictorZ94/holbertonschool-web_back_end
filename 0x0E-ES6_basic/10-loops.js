export default function appendToEachArrayValue(array, appendString) {
  const myArr = [];
  for (const [idx, elem] of array.entries()) {
    const value = elem;
    myArr[idx] = appendString + value;
  }

  return myArr;
}
