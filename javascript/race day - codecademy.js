let raceNumber = Math.floor(Math.random() * 1000);
let early_registration = true;
let runner_age = 12;

if (early_registration && runner_age > 18){
  raceNumber += 1000;
}
if(early_registration && runner_age > 18){
  console.log(`Your race will start at 9:30 am. Your racenumber is ${raceNumber}`);
}
else if(!early_registration && runner_age >= 18){
  console.log(`Your race will start at 11:00 am. Your racenumber is ${raceNumber}`)
}
else if (runner_age <18){
  console.log(`Youth registrants run at 12:30, regardless of registration. Your racenumber is ${raceNumber}`);
}
else{
console.log('please see the registration desk.')
}
