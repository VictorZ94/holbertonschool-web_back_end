export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get getName() {
    return this._name;
  }

  set setName(name) {
    if (typeof (name) !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;
  }

  get getLenth() {
    return this._length;
  }

  set setLength(length) {
    if (typeof (length) !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = length;
  }

  get getStudents() {
    return this._students;
  }

  set setStudents(students) {
    if (Array.isArray(students) && students.every((s) => typeof s === 'string')) {
      this._students = students;
    } else {
      throw new TypeError('Students must be an array of strings');
    }
  }
}
