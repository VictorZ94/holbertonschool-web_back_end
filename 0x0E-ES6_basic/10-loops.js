export default function appendToEachArrayValue(array, appendString) {
  for (const [idx, elem] of array.entries()) {
    const value = elem;
    array[idx] = appendString + value;
  }

  return array;
}
