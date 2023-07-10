class myArray {
  constructor(data) {
    this.data = data;
  }

  map(callback) {
    for (let i = 0; i < this.data.length; i++) {
      callback(this.data[i]);
    }
  }
}


arr = new myArray([
  { id: 1, name: 'John' },
  { id: 2, name: 'James' },
  { id: 3, name: 'Joe' },
  { id: 4, name: 'Nate' },
  { id: 5, name: 'Chris' }
]);

arr.map(item => console.log(`id: ${item.id} - name: ${item.name}`));