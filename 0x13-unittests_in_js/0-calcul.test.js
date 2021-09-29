const assert = require('chai').assert;
const calculateNumber = require("./0-calcul.js");

describe('calculateNumber', () => {

    // block prototype
    it('is a function', () => {
        assert.isFunction(calculateNumber, 'should be prototype of function');
    });

    // test values
    it('Return value should be equal', () => {
        assert.strictEqual(calculateNumber(1, 3), 4, 'Integer args');
    });
    it('1st arg rounds towards up', () => {
        assert.strictEqual(calculateNumber(1.9, 7), 9, '1st arg should round to up');
    });
    it('2do arg rounds towards up', () => {
        assert.strictEqual(calculateNumber(1, 3.7), 5, '2do arg should round to up');
    });
    it('1st arg rounds towards down', () => {
        assert.strictEqual(calculateNumber(1.2, 8), 9, '1st arg should round to up');
    });
    it('2do arg rounds towards down', () => {
        assert.strictEqual(calculateNumber(0, 3.2), 3, '2do arg should round down');
    });
    it('Both args round towards up', () => {
        assert.strictEqual(calculateNumber(10.5, 3.9), 15, 'Both args should round to up');
    });
    it('Both args round towards down', () => {
        assert.strictEqual(calculateNumber(15.4, 3.1), 18, 'Both args should round to down');
    });
    it('zero args', () => {
        assert.strictEqual(calculateNumber(0.1, 0.1), 0, 'these numbers are equal');
    });
    it('zero with a lot of float numbers', () => {
        assert.strictEqual(calculateNumber(0.005555, 0.55555), 1, 'float numbers');
    });
    it('too much decimals', () => {
        assert.strictEqual(calculateNumber(1.23456789, 9.876543210), 11, 'float numbers');
    });
});
