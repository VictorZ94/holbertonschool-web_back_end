const getListStudentIds = (data) => {
  if (Array.isArray(data)) {
    return data.map((elem) => elem.id);
  }
  return [];
};

export default getListStudentIds;
