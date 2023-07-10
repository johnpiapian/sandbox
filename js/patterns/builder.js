class Car {
  constructor(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
  }

  getMake() {
    return this.make;
  }

  getModel() {
    return this.model;
  }

  getYear() {
    return this.year;
  }

  static builder() {
    return new CarBuilder();
  }
}

class CarBuilder {
  constructor() {
    this.make = '';
    this.model = '';
    this.year = '';
  }

  withMake(make) {
    this.make = make;
    return this;
  }

  withModel(model) {
    this.model = model;
    return this;
  }

  withYear(year) {
    this.year = year;
    return this;
  }

  build() {
    return new Car(this.make, this.model, this.year);
  }
}

class CarManager {
  constructor(cars) {
    this.cars = cars;
  }

  display() {
    this.cars.map(car => {
      console.log(`${car.getMake()} - ${car.getModel()} - ${car.getYear()}`);
    })
  }
}

cars = [
  Car.builder()
    .withMake("Toyota")
    .withModel("Camery")
    .withYear(2010)
    .build(),
  Car.builder()
    .withMake("Toyota")
    .withModel("Prius")
    .withYear(2019)
    .build(),
];

cm = new CarManager(cars);
cm.display();