const { expect } = require('chai');
const calculateNumber = require("./1-calcul.js");

describe('calculateNumber', () => {
    describe('Test case SUM', () => {
        // test values
        it('Return value should be equal', () => {
            expect(calculateNumber('SUM', 1, 3)).to.equal(4);
        });
        it('1st arg rounds towards up', () => {
            expect(calculateNumber('SUM', 1.9, 7)).to.equal(9);
        });
        it('2do arg rounds towards up', () => {
            expect(calculateNumber('SUM',1, 3.7)).to.equal(5);
        });
        it('1st arg rounds towards down', () => {
            expect(calculateNumber('SUM', 1.2, 8)).to.equal(9);
        });
        it('2do arg rounds towards down', () => {
            expect(calculateNumber('SUM', 0, 3.2)).to.equal(3);
        });
        it('Both args round towards up', () => {
            expect(calculateNumber('SUM', 10.5, 3.9)).to.equal(15);
        });
        it('Both args round towards down', () => {
            expect(calculateNumber('SUM', 15.4, 3.1)).to.equal(18);
        });
        it('zero args', () => {
            expect(calculateNumber('SUM', 0.1, 0.1)).to.equal(0);
        });
        it('zero with a lot of float numbers', () => {
            expect(calculateNumber('SUM', 0.005555, 0.55555)).to.equal(1);
        });
        it('too much decimals', () => {
            expect(calculateNumber('SUM', 1.23456789, 9.876543210)).to.equal(11);
        });
    });

    // Test case for substract operator
    describe('unitTest case SUBTRACT', () => {
        it('Return value should be equal', () => {
            expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(2);
        });
        it('1st arg rounds towards up', () => {
            expect(calculateNumber('SUBTRACT', 1.9, 7)).to.equal(5);
        });
        it('2do arg rounds towards up', () => {
            expect(calculateNumber('SUBTRACT', 1, 3.7)).to.equal(3);
        });
        it('1st arg rounds towards down', () => {
            expect(calculateNumber('SUBTRACT', 1.2, 8)).to.equal(7);
        });
        it('2do arg rounds towards down', () => {
            expect(calculateNumber('SUBTRACT', 0, 3.2)).to.equal(3);
        });
        it('Both args round towards up', () => {
            expect(calculateNumber('SUBTRACT', 10.5, 3.9)).to.equal(-7);
        });
        it('Both args round towards down', () => {
            expect(calculateNumber('SUBTRACT', 15.4, 3.1)).to.equal(-12);
        });
        it('zero args', () => {
            expect(calculateNumber('SUBTRACT', 0.1, 0.1)).to.equal(0);
        });
        it('zero with a lot of float numbers', () => {
            expect(calculateNumber('SUBTRACT', 0.005555, 0.55555)).to.equal(1);
        });
        it('too much decimals', () => {
            expect(calculateNumber('SUBTRACT', 1.23456789, 9.876543210)).to.equal(9);
        });
        it('too much decimals negative', () => {
            expect(calculateNumber('SUBTRACT', 9.23456789, 1.876543210)).to.equal(-7);
        });
        it('negative args', () => {
            expect(calculateNumber('SUBTRACT', -20.89, -1.2)).to.equal(20);
        });
        it('one args as negative number', () => {
            expect(calculateNumber('SUBTRACT', -6.9, 9.00001)).to.equal(16);
        });
        it('Positive numbers', () => {
            expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(4);
        });
    });

    // Test case for Divide operator
    describe('unitTest case DIVIDE', () => {
        it('Return value should be equal', () => {
            expect(calculateNumber('DIVIDE', 1, 2)).to.equal(0.5);
        });
        it('1st arg rounds towards up', () => {
            expect(calculateNumber('DIVIDE', 1.9, 7)).to.equal(0.2857142857142857);
        });
        it('2do arg rounds towards up', () => {
            expect(calculateNumber('DIVIDE', 1, 3.7)).to.equal(0.25);
        });
        it('1st arg rounds towards down', () => {
            expect(calculateNumber('DIVIDE', 8, 1)).to.equal(8);
        });
        it('2do arg rounds towards down', () => {
            expect(calculateNumber('DIVIDE', 0, 3.2)).to.equal(0);
        });
        it('Both args round towards up', () => {
            expect(calculateNumber('DIVIDE', 10.5, 3.9)).to.equal(2.75);
        });
        it('Both args round towards down', () => {
            expect(calculateNumber('DIVIDE', 15.4, 3.1)).to.equal(5);
        });
        it('zero with a lot of numbers', () => {
            expect(calculateNumber('DIVIDE', 0.005555, 0.55555)).to.equal(0);
        });
        it('Divide by 0', () => {
            expect(calculateNumber('DIVIDE', 1.23456789, 0)).to.equal('Error');
        });
        it('Divide by number negative', () => {
            expect(calculateNumber('DIVIDE', -9, -3)).to.equal(3);
        });
    });
});
