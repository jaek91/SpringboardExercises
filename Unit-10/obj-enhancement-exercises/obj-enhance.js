
//-----Same keys and Values-----//
/* function createInstructor(firstName, lastName){
    return {
      firstName: firstName,
      lastName: lastName
    }
  } */

/* Write an ES2015 Version */
const createInstructor = (firstName,lastName) => ({firstName,lastName});



//-----computed property names-----//

/* var favoriteNumber = 42;
var instructor = {
  firstName: "Colt"
}
instructor[favoriteNumber] = "That is my favorite!" */

/* Write an ES2015 Version */

let favoriteNumber = 42;

let instructor = {
    firstName: "Colt",
    [favoriteNumber]: "That is my favorite"
}

//------object methods-------// 
/* var instructor = {
    firstName: "Colt",
    sayHi: function(){
      return "Hi!";
    },
    sayBye: function(){
      return this.firstName + " says bye!";
    }
  } */

let instructor = {
    firstName: "Colt",
    sayHi() {return "Hi";},
    sayBye() {return this.firstName + " says bye!";}
}

//-----createAnimal Function-----//

const createAnimal = (species,verb,noise) => ({
    species, 
    [verb]() {return noise;}
})
