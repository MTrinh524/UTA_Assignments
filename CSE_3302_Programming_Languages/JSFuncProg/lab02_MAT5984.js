// Minh Trinh
// 1001705984
// 10/4/2022

//QUESTION 1
// array of ints from 1-10
let inputtable = [1,2,3,4,5,6,7,8,9,10]

//These multiples uses the maps() function to get each element
//in the array to set an operation on to it

//question 2
// set of multiples of 5 btwn 1-51
let fiveTable = inputtable.map(function(element){
    //multiples each index of the array by 5
    return element * 5
});
//console.log(fiveTable), results: [ 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 ]

// set of multiples of 13 btwn 1-131
let thirteenTable = inputtable.map(function(element){
    //multiplies each index of the array by 13
    return element * 13
});
//console.log(thirteenTable), results: [ 13, 26, 39, 52, 65, 78, 91, 104, 117, 130 ]

// set of squares of ints from "inputtable"
let squaresTable = inputtable.map(function(element){
    //using the Math.pow function to get the squares by setting "element" to the power of 2
    return Math.pow(element, 2)
});
//console.log(squaresTable), results: [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]

//QUESTION 3
// set odd multiples of 5 btwn 1-100
function oddMultFive(start, end, arr, x){
    //exists the recursion whenever the start becomes greater than the end
    if(start > end){
        return arr //returns the array that contains the set of odd multples of 5
    }
    //if start is even then increments start by 5
    if(start % 2 == 0){
        return oddMultFive(start+5, end, arr, x)
    }
    //else if the start is odd
    else{
        arr[x] = start //set 'x' index of the array to start, increment start by 10, and pre increment x
        return oddMultFive(start+10, end, arr, ++x)
    }
}
let arr = []
console.log(oddMultFive(0, 100, arr, 0))
//results: [ 5, 15, 25, 35, 45, 55, 65, 75, 85, 95 ]

//QUESTION 4
// set of even multiples of 7 btwn 1-100
function sum_even_multiples_seven(start, end, sum){
    //breaks out of the recursion whenever start becomes greater than the end
    if(start > end){
        //returns the total sum of even multpes of 7 btwn 1-100
        return sum
    }
    //if the start is NOT an even number
    if(start % 2 == 1){
        //add start by 7 and call the recursion again
        //P.S. I feel like this part isn't needed considering it will check for multiples of 14 which are both even and a multiple of 7
        return sum_even_multiples_seven(start+7, end, sum)
    }
    else{
        //if the start IS an even number, add the start into sum
        sum += start
        //recalls the recursion for the next number that is both a multiple of 7 and is even
        return sum_even_multiples_seven(start+14, end, sum)
    }
}
//pass in 0 instead of 1 so that we can get 7 or 14 when we add by 7 or 14 instead of 8 or 15
let sumevenmultseven = sum_even_multiples_seven(0,100,0)
//console.log(sumevenmultseven), results: 392

//QUESTION 5
//this is a curried version of the original function that takes r in first and then h later
var cylinder_volume = r => h => 3.14*r*r*h; 

var compute_cylinder_volume = cylinder_volume(5); //inputs a radius of 5 into cylinder_volume
var compute10 = compute_cylinder_volume(10); //calls compute_cylinder_volume and inputs the h of 10
//console.log(compute10), results: 785
var compute_cylinder_volume = cylinder_volume(5); //inputs a radius of 5 into cylinder_volume
var compute17 = compute_cylinder_volume(17); //calls compute_cylinder_volume and inputs the h of 17
//console.log(compute17), results: 1334.5
var compute_cylinder_volume = cylinder_volume(5); //inputs a radius of 5 into cylinder_volume
var compute11 = compute_cylinder_volume(11); //calls compute_cylinder_volume and inputs the h of 11
//consolve.log(compute11), results: 863.5

//QUESTION 6
//uses closure to make HTML tables that allow us to uses functions stated in a previous line
makeTag = function(beginTag, endTag){
    return function(textcontent){
        return beginTag +textcontent +endTag;
    }
}

//creates the beginTag and endTag then inserts the contents "table" in btwn
var contents = makeTag('<', '>')
console.log(contents("table")) //signifies the start of the HTML table
//creates the beginTag and endTag then inserts the contents "tr" in btwn

//"th" signifies the start of the table header with the general attributes being
//"Carbrand", "Carmodel", and "Year"
//"/th" signifies the end of the current table header
console.log(contents("tr")) //signifies the start of the table row
console.log(contents("th") + "Carbrand" + contents("/th"))
console.log(contents("th") + "Carmodel" + contents("/th"))
console.log(contents("th") + "Year" + contents("/th"))
console.log(contents("/tr")) //signifies the end of the table row

//starts the first row of entries/data in the table
console.log(contents("tr"))
//"td" signifies the start of the table data for the specified table header
//depending on the order of contents inputted
//"/td" signifies the end of the table data
console.log(contents("td") + "Toyota" + contents("/td"))
console.log(contents("td") + "Avalon" + contents("/td"))
console.log(contents("td") + "2020" + contents("/td"))
//ends the first row of entries'data in the table
console.log(contents("/tr"))

//starts the second row of entries/data in the table
console.log(contents("tr"))
//"td" signifies the start of the table data for the specified table header
//depending on the order of contents inputted
//"/td" signifies the end of the table data
console.log(contents("td") + "Chevrolet" + contents("/td"))
console.log(contents("td") + "Camaro" + contents("/td"))
console.log(contents("td") + "2018" + contents("/td"))
//ends the second row of entries'data in the table
console.log(contents("/tr"))

//signifies the end of the table
console.log(contents("/table"))


