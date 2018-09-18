// Math: Absolute Value

console.log(`Absolute value Math.abs: ${Math.abs(-100)}`);
console.log(`Absolute value Math.abs: ${Math.abs(-100)}`);
console.log(`Absolute value Math.abs: ${Math.abs(-100)}`);


// Ceiling, floor, round

console.log(`Ceiling Math.ceil: ${Math.ceil(1.5)}`);
console.log(`Math.floor: ${Math.floor(1.5)}`);
console.log(`Math.round: ${Math.round(1.5)}`);

// Max and Min

console.log(`Math.max ${Math.max(100,50)}`)
console.log(`Math.min ${Math.min(80,40)}`)

// If else

const some_num = 3

if (some_num === 3){
    console.log("somenum is 3");
} else if (some_num === 2) {
    console.log("some_num is 2")
} else if (some_num === 1) {
    console.log("some_num is 1")
} else {
    console.log("?")
}

// Ternary

const x = 2
const y = 3

console.log(`x % 2 === 0 ? 'even':'odd' ${x % 2 === 0 ? 'even':'odd' }`)
console.log(`x % 2 === 0 ? 'even':'odd' ${y % 2 === 0 ? 'even':'odd' }`)


// Exceptions

try {
    foo();
} catch (error) {
    console.log('foo is not defined');
}

// Continue / Break

for (let i = 1; i <= 100; i ++ ){
    if (i === 3){
        console.log("fizz")
        continue
    }

    if( i === 5) {
        console.log("buzz")
        break
    }
    console.log(i);
}

// Length

const some_str = "foobar"

console.log(`some_str.length ${some_str.length}`)

// Interpolation

const hello = "hello"

console.log(`${hello} world`);

// Multiline

console.log(`
Line 1
line 2
line 3
`);

// String to integers

const string1 = '1'
const number1 = parseInt(string1)

console.log(number1 + 1);

// Contains

if ('123'.includes('2')) {
    console.log('2 is in the string')
}

if(!'456'.includes('2')) {
    console.log('2 is not in the string')
}

// Substring

const subString = "012345"

console.log(`subString.substring() ${subString.substring(2,5)}`)

// Join

const someList = ['a', 'b', 'c']
console.log(`someList.join() ${someList.join(',')}`)

// Strip

const stripString = '   abc   '
console.log(`stripString.trim() ${stripString.trim()}`)

// Split

let abc_str = "a,b,c"
const abc_str_list = abc_str.split(',')

console.log(`abc_str_list[0] ${abc_str_list[0]}`)
console.log(`abc_str_list[1] ${abc_str_list[1]}`)
console.log(`abc_str_list[2] ${abc_str_list[2]}`)

// Replace 

const replace_str = "a b c d e"
console.log(`replace_str ${replace_str.replace(/ /g,',')}`)


// Regex Match

if ('iphone 8'.match(/\d/g)) {
    console.log('has a number')
}

if (!'iphone x'.match(/\d/g)) {
    console.log('doenst have a number')
}

// Iteration

const iteration_list = [1,2,3]

iteration_list.forEach(element => {
    console.log(element)
})

// Length

const len_list = [1,2,3,4]
console.log(len_list.length)

// Enumerate 

const enumerate_list = [4,5,6,7,8]
enumerate_list.forEach((value, index) =>
    console.log(`${index} ${value}`)
)
