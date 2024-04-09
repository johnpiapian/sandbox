function find(arr, discriminator, index=0) {
    if (discriminator(arr[index])) return arr[index]
    if (arr.length < index) return undefined
    return find(arr, discriminator, ++index) 
}

function every(arr, discriminator, index=0) {
    if (index >= arr.length) return true
    if (!discriminator(arr[index])) return false
    return every(arr, discriminator, ++index)
}

function forEach(arr, callback, index=0) {
    if (index >= arr.length) return
    callback(arr[index])
    return forEach(arr, callback, ++index)
}

function compareArray(arr1, arr2, index=0) {
    if (index >= arr1.length) return true
    if (arr1.length != arr2.length || arr1[index] !== arr2[index]) return false
    return compareArray(arr1, arr2, ++index)
}

const myData = [
    {id: 1, data: 'A'},
    {id: 2, data: 'B'},
    {id: 3, data: 'C'},
    {id: 4, data: 'D'}
]

const arrA = [1, 2, 4, 5, 6]
const arrB = [1, 2, 4, 5, 6]

console.log(find(myData, (item) => item.id == 3)) 
console.log(every(myData, (item) => item.id <= 6))
forEach(myData, (item) => console.log(item))
console.log(compareArray(arrA, arrB))