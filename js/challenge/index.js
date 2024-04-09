"use strict";

function assert(result, expected) {
    // Success case
    if (typeof result === typeof expected) {

        function isEqualArray(expected, result, index = 0) {
            if (expected.length <= index) return true;
            if (expected[index] !== result[index]) return false;
            return isEqualArray(expected, result, ++index);
        }

        // compare arrays
        if (Array.isArray(result) && isEqualArray(expected, result)) {
            console.log(`SUCCESS -> Expected: [${expected}] \n\t-> Result: [${result}]\n`);
            return true;
        }

        if (result === expected) {
            console.log(`SUCCESS -> Expected: ${expected} \n\t-> Result: ${result}\n`);
            return true;
        }
    }

    // Error case
    if (Array.isArray(result)) {
        console.error(`Error: Expected: [${expected}] \n\t-> Result: [${result}]\n`);
    } else {
        console.error(`Error: Expected: ${expected} \n\t-> Result: ${result}\n`);
    }

    return false;
}

// Functions
function isPalindrome(text, start = 0, end = text.length - 1) {
    if (start >= end) return true;
    if (text.charAt(start) != text.charAt(end)) return false;
    return isPalindrome(text, ++start, --end);
}

function reverse(text, curr = -1) {
    if (curr == -1) return reverse(text, text.length - 1);
    if (curr > 0) return text.charAt(curr) + reverse(text, --curr);
    return text.charAt(0);
}

function fib(n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

function fib_seq(n, result = [], curr = 1) {
    if (n < curr) return result;
    result.push(fib(curr));
    return fib_seq(n, result, ++curr);
}

function fizzbuzz(n, result = []) {
    if (n <= result.length) return result;
    
    const curr_n = result.length + 1;

    if (curr_n % 3 === 0 && curr_n % 5 === 0) result.push("FizzBuzz");
    else if (curr_n % 3 === 0) result.push("Fizz");
    else if (curr_n % 5 === 0) result.push("Buzz");
    else result.push(curr_n.toString());

    return fizzbuzz(n, result);
}

// test cases
assert(isPalindrome("level"), true);
assert(isPalindrome("test"), false);
assert(reverse("test"), "tset");
assert(fib(10), 55);
assert(fib_seq(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]);
assert(fizzbuzz(3), ["1","2","Fizz"]);