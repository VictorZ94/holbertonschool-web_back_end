function calculateNumber(type, a, b) {
    switch (type) {
        case 'SUBTRACT':
            return Math.round(b) - Math.round(a);
        case 'DIVIDE':
            if (b === 0)
                return 'Error'
            return Math.round(a) / Math.round(b);
        default:
            return Math.round(a) + Math.round(b);;
    }
}

module.exports = calculateNumber;
