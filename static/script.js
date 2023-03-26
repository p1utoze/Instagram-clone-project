async function getLogin_redirect() {
    const loginForm = document.getElementById("login-form")

    // Add an event listener to the form submit event
    loginForm.addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent the form from submitting normally

  // Get the username and password values
  const email = document.getElementById('login_mail').value;
  const password = document.getElementById('password').value;

  // Make the GET request to the API endpoint
  if (verifyForm == true) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/users?email=${email}`, {
        method:'GET',
    })
    // console.log(response.json())
    const data = await response.json()
    console.log(data)
    if (data.user == true) {
        // Redirect to home.html if key is true
        window.location.href = 'index.html';
      } 
      else {
        // Display an error message if key is false
        const errorMsg = document.getElementById('error_message');
        errorMsg.innerHTML = 'Incorrect email or password';
      }
  } catch (error) {
    console.log(error)
  }
  }});
}
function changeImage() {
  var images = document
    .getElementById("slide-content")
    .getElementsByTagName("img");

  var i = 0;

  for (i = 0; i < images.length; i++) {
    var image = images[i];

    if (image.classList.contains("active")) {
      //remove active class from this image
      image.classList.remove("active");

      //if we are at the last image, then go back to the first image
      if (i == images.length - 1) {
        var nextImage = images[0];
        nextImage.classList.add("active");
        break;
      }

      var nextImage = images[i + 1];
      nextImage.classList.add("active");
      break;
    }
  }
}

function changeMode() {
  var body = document.getElementsByTagName("body")[0];
  var footerLinks = document
    .getElementById("links")
    .getElementsByTagName("a");

  //if we are currently using dark mode
  if (body.classList.contains("dark")) {
    body.classList.remove("dark");

    for (let i = 0; i < footerLinks.length; i++) {
      footerLinks[i].classList.remove("dark-mode-link");
    }
  } else {
    //we are currently using the light
    body.classList.add("dark");

    for (let i = 0; i < footerLinks.length; i++) {
      footerLinks[i].classList.add("dark-mode-link");
    }
  }
}

function verifyForm() {
  var password = document.getElementById("password").value;
  var error_message = document.getElementById("error_message");

  if (password.length < 6) {
    error_message.innerHTML = "Password is to short";
    return false;
  }

  return true;
}

document.getElementById("dark-btn").addEventListener("click", (e) => {
  e.preventDefault();
  changeMode();
});

document.getElementById("login-form").addEventListener("submit", (e) => {
  e.preventDefault();

  verifyForm();
});

async function follower_stories(user_id) {
  const imageContainer = document.getElementById('status-wrapper');

  fetch(`https://api.example.com/followers/${user_id}`)
  .then(response => response.json())
  .then(data => {
    // Get the list of img elements from the division container
    const imgElements = imageContainer.querySelectorAll('img');
    
    // Loop through the img elements and set their src value based on the corresponding item in the response data list
    imgElements.forEach((imgElement, index) => {
      imgElement.src = data[index].imageUrl;
    });
  })
  .catch(error => console.log(error));
}