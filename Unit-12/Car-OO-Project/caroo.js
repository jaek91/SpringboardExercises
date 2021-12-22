class Vehicle {
    constructor(make,model,year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    honk() {
        return "Beep!";
    }

    toString() {
        return `This vehicle is a ${this.make} ${this.model} from ${this.year}`;
    }
}

 let vehicle = new Vehicle("Toyota","Corolla","1999");
/* console.log(vehicle.honk());
console.log(vehicle.toString());
 */ 
class Car extends Vehicle {
    constructor(make,model,year) {
        super(make,model,year);
        this.numWheels = 4;
    }

}

/* let c1 = new Car("Toyota","Corolla","1999");
console.log(c1.honk());
console.log(c1.toString());
console.log(c1.numWheels); */

class Motorcycle extends Vehicle {
    constructor(make,model,year) {
        super(make,model,year);
        this.numWheels = 2;
    }

    revEngine() {
        return "VROOM!!!";
    }
}
/* 
let m1 = new Motorcycle("Honda", "Nighthawk", 2000);
console.log(m1.honk());
console.log(m1.revEngine());
console.log(m1.numWheels); */



class Garage {

constructor(capacity) {
    this.capacity = capacity;
    this.vehicles = [];
}

add(vehicle) {
    if (vehicle instanceof Vehicle && this.vehicles.length < this.capacity){
        this.vehicles.push(vehicle);
        return "Vehicle added!";
    }
    else if(this.vehicles.length === this.capacity) {
        return "Sorry, we're full";
    }
    else {
        return "Only vehicles are allowed here!";
    }
}

}

let garage = new Garage(2);
console.log(garage.vehicles); // []
console.log(garage.add(new Car("Hyundai", "Elantra", 2015))); // "Vehicle added!"
console.log(garage.vehicles); // [Car]
console.log(garage.add("Taco")); // "Only vehicles are allowed in here!"
console.log(garage.add(new Motorcycle("Honda", "Nighthawk", 2000))); // "Vehicle added!"
console.log(garage.vehicles); // [Car, Motorcycle]
console.log(garage.add(new Motorcycle("Honda", "Nighthawk", 2001))); // "Sorry, we're full."