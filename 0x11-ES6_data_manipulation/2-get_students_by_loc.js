function getStudentsByLocation(data) {
  if (Array.isArray(data)) {
    return data.filter((elem) => elem.location === 'San Francisco');
  }
  return [];
}

export default getStudentsByLocation;
