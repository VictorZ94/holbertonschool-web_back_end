function getStudentsByLocation(data, match) {
  if (Array.isArray(data)) {
    data.filter((elem) => elem.location === match);
  }
  return [];
}

export default getStudentsByLocation;
