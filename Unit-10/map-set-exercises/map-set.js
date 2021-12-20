//Q1: What does the following code return?

const set1 = new Set([1,1,2,2,3,4]) //{1,2,3,4}
console.log(set1);

//Q2: What does the following code return?

let set2 = [...new Set("referee")].join(""); //ref

//Q3: What does the Map m look like after running the following code?

//output: { [ 1, 2, 3 ] => true, [ 1, 2, 4 ] => false }
let m = new Map(); 
m.set([1,2,3], true);
m.set([1,2,4], false);

//hasDuplicate function

const hasDuplicate = (arr) => {
    const uniques = Array.from(new Set (arr));
    return arr.length === uniques.length ? false: true;
}
/* 
const arr =[1,2,2,3,4,5];
const arr2 = [1,2,3,4,4,4,5];
console.log(hasDuplicate(arr));
console.log(hasDuplicate(arr2)); */

//vowelCount function

const vowel = "aeiou";
const isVowel = char => (vowel.includes(char));

const vowelCount = (str) => {
    const lowercase = str.toLowerCase();
    const strArr = Array.from(lowercase);
    let results = new Map();

    for (let char of strArr) {
        if (isVowel(char)) {
            results.has(char) ? results.set(char, results.get(char) + 1) : results.set(char,1);
        } 
    }
    
    return results;
}

str = "awesome";
console.log(vowelCount(str));