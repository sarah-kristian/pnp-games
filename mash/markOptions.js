// Developing script to mark every nth item in a list of options
// it should excluding unique values and already marked items


const sampleData = {
    category1: ['option1a', 'option1b', 'option1c'],
    category2: ['option2a', 'option2b', 'option2c'],
    category3: ['option3a', 'option3b', 'option3c'],
    category4: ['option4a', 'option4b', 'option4c']
  };
  
// // Combine all options into a single array
// const allOptions = Object.values(sampleData).flat();


// Create a mapping of option to its category
const optionCategoryMap = {};
Object.entries(sampleData).forEach(([key, value]) => {
    value.forEach(option => optionCategoryMap[option] = key);
});



const optionList = {
    option1a: 'category1',
    option1b: 'category1',
    option1c: 'category1',
    option2a: 'category2',
    option2b: 'category2',
    option2c: 'category2',
    option3a: 'category3',
    option3b: 'category3',
    option3c: 'category3',
};

// Function to count occurrences of a value in the object
function countOccurrences(obj, value) {
    return Object.values(obj).filter(val => val === value).length;
}

// Function to mark nth item (excluding already marked and unique values)
function markNthUnmarked(optionList, n) {
    const keys = Object.keys(optionList);
    let count = 0;
    let i = 0;

    while (count < n) {
        const key = keys[i % keys.length];
        const value = optionList[key];
        const occurrences = countOccurrences(optionList, value);

        if (optionList[key] !== 'strikethrough' && occurrences > 1) {
            count++;
            if (count === n) {
                optionList[key] = 'strikethrough';
                return true; // Item was marked
            }
        }
        i++;
    }
    return false; // No item was marked
}

// Loop to mark every 5th item until all that remains are strikethroughs and unique values

while (markNthUnmarked(optionList, 5)) {
    // Continue marking every 5th item
}

console.log(optionList);

