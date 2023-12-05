// FETCH and READ the person.JSON disk file
alert('QAP 5 Fetch the Data')
fetch('./person.json')
  .then(response => response.json())
  .then(data => {
    // Do something with the JSON data from person.JSON
    console.log(data); // Log the JSON data to the console

    // Access a value from the JSON data
    console.log(data[0].fname);

    // Loop through an array in the JSON data from person.JSON
    data.forEach(person => {
      switch(person.gender){
        case "female": 
          console.log(`${person.fname} should use the female washroom.`);
          break;
        case "non-binary": 
          console.log(`${person.fname} should use the inclusive washroom.`);
          break;
        case "male":
          console.log(`${person.fname} should use the male washroom.`);
          break;
        default:
          console.log(`${person.fname} should be mindful in choosing a washroom.`);
      }
      console.log(person); // Log each person in the array to the console for gender.
    });
    data.forEach(person => {
      switch(person.age){
        case "23": 
          console.log(`${person.fname} is 23 years old.`);
          break;
        case "25": 
          console.log(`${person.fname} is 25 years old.`);
          break;
          case "31": 
          console.log(`${person.fname} is 31 years old.`);
          break;
        case "32":
          console.log(`${person.fname} is 32 years old.`);
          break;
        default:
          console.log(`${person.fname}'s age is undisclosed.`);
      }
      console.log(person); // Log each person in the array to the console for age.
    });
  })
  .catch(error => {
    // Catch any errors that occur while fetching the file
    console.error(error);
  });
