function getStudentIdsSum(students) {
  if (Array.isArray(students)) {
    const reducer = (sum, students) => sum + students.id;
    return students.reduce(reducer, 0);
  }
  return [];
}

export default getStudentIdsSum;
