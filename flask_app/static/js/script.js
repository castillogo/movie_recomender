// Custom JS code for changing the color of the button when we hover over it

// console.log('script is connected! everything is working!');

var button = document.getElementsByClassName('submit-button')[0];


button.addEventListener('mouseover', function() {
  console.log('hello!');
  button.style.background = '#FFE4F8';
  button.style.color = '#62003C';
});

button.addEventListener('mouseout', function() {
  console.log('goodbye!');
  button.style.background = '#983D6B';
  button.style.color = '#FFE4F8';
});
