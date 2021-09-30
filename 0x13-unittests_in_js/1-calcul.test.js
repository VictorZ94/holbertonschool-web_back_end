const assert = require('assert');
const calculateNumber = require("./1-calcul.js");

describe('calculateNumber', () => {
    describe('Test case SUM', () => {
        // test values
        it('Return value should be equal', () => {
            assert.strictEqual(calculateNumber('SUM', 1, 3), 4, 'Integer args');
        });
        it('1st arg rounds towards up', () => {
            assert.strictEqual(calculateNumber('SUM', 1.9, 7), 9, '1st arg should round to up');
        });
        it('2do arg rounds towards up', () => {
            assert.strictEqual(calculateNumber('SUM',1, 3.7), 5, '2do arg should round to up');
        });
        it('1st arg rounds towards down', () => {
            assert.strictEqual(calculateNumber('SUM', 1.2, 8), 9, '1st arg should round to up');
        });
        it('2do arg rounds towards down', () => {
            assert.strictEqual(calculateNumber('SUM', 0, 3.2), 3, '2do arg should round down');
        });
        it('Both args round towards up', () => {
            assert.strictEqual(calculateNumber('SUM', 10.5, 3.9), 15, 'Both args should round to up');
        });
        it('Both args round towards down', () => {
            assert.strictEqual(calculateNumber('SUM', 15.4, 3.1), 18, 'Both args should round to down');
        });
        it('zero args', () => {
            assert.strictEqual(calculateNumber('SUM', 0.1, 0.1), 0, 'these numbers are equal');
        });
        it('zero with a lot of float numbers', () => {
            assert.strictEqual(calculateNumber('SUM', 0.005555, 0.55555), 1, 'float numbers');
        });
        it('too much decimals', () => {
            assert.strictEqual(calculateNumber('SUM', 1.23456789, 9.876543210), 11, 'float numbers');
        });
    });

    // Test case for substract operator
    describe('unitTest case SUBTRACT', () => {
        it('Return value should be equal', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), 2, 'Integer args');
        });
        it('1st arg rounds towards up', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 1.9, 7), 5, '1st arg should round to up');
        });
        it('2do arg rounds towards up', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 1, 3.7), 3, '2do arg should round to up');
        });
        it('1st arg rounds towards down', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 8), 7, '1st arg should round to up');
        });
        it('2do arg rounds towards down', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 0, 3.2), 3, '2do arg should round down');
        });
        it('Both args round towards up', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 10.5, 3.9), -7, '1st args is greather than 2nd args');
        });
        it('Both args round towards down', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 15.4, 3.1), -12, 'Both args should round to down');
        });
        it('zero args', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 0.1, 0.1), 0, 'these numbers are equal');
        });
        it('zero with a lot of float numbers', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 0.005555, 0.55555), 1, 'float numbers');
        });
        it('too much decimals', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 1.23456789, 9.876543210), 9, 'float numbers');
        });
        it('too much decimals negative', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 9.23456789, 1.876543210), -7, 'float numbers');
        });
        it('negative args', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', -20.89, -1.2), 20, 'Negative arguments');
        });
        it('one args as negative number', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', -6.9, 9.00001), 16, 'Negative arguments');
        });
        it('Positive numbers', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), 4, 'Positive arguments');
        });
    });

    // Test case for Divide operator
    describe('unitTest case DIVIDE', () => {
        it('Return value should be equal', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1, 2), 0.5, 'Integer args');
        });
        it('1st arg rounds towards up', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1.9, 7), 0.2857142857142857, '1st arg should round to up');
        });
        it('2do arg rounds towards up', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1, 3.7), 0.25, '2do arg should round to up');
        });
        it('1st arg rounds towards down', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 8, 1), 8, '1st arg should round to up');
        });
        it('2do arg rounds towards down', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 0, 3.2), 0, '2do arg should round down');
        });
        it('Both args round towards up', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 10.5, 3.9), 2.75, '1st args is greather than 2nd args');
        });
        it('Both args round towards down', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 15.4, 3.1), 5, 'Both args should round to down');
        });
        it('Return a NaN number', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 0.1, 0.1), NaN, 'these numbers are equal');
        });
        it('zero with a lot of numbers', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 0.005555, 0.55555), 0, 'float numbers');
        });
        it('Divide by 0', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1.23456789, 0), 'Error', 'Divide by 0');
        });
        it('Divide by number negative', () => {
            assert.strictEqual(calculateNumber('DIVIDE', -9, -3), 3, 'Divide by negative numbers');
        });
    });
});
