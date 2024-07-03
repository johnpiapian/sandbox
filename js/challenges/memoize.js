// memoize a function
const memoize = (fn) => {
    const cache = new Map();
    return (arg) => {
        if (cache.has(arg)) {
            return cache.get(arg);
        }
        const result = fn(arg);
        cache.set(arg, result);
        return result;
    };
};

function calculateTimeElapsed(fn, ...args) {
    const startTime = performance.now();
    const result = fn(...args);
    const endTime = performance.now();
    console.log(`Result: ${result} \nTime Elapsed: ${endTime - startTime} milliseconds`)
    return result;
}


// function to memoize
const fib = (n) => {
    if (n < 2) return n
    return fib(n - 2) + fib(n - 1)
}

const square = (n) => n * n

// Memozied function
const memoizedFib = memoize(fib);

// Timed
const n = 40
console.log('Original function: ')
calculateTimeElapsed(fib, n)
console.log('Memoized function: ')
calculateTimeElapsed(memoizedFib, n)