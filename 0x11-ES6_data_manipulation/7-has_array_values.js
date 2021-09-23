function hasValuesFromArray(set, array) {
  return array.every((x) => set.has(x));
}

export default hasValuesFromArray;
