async function getLogin_redirect() {
  const loginForm = document.getElementById("login-form")

  // Add an event listener to the form submit event
  loginForm.addEventListener('submit', async (event) => {
event.preventDefault(); // Prevent the form from submitting normally

// Get the username and password values
const name = document.getElementById('login_mail').value;
const password = document.getElementById('password').value;

// Make the GET request to the API endpoint
if (verifyForm() == true) {
try {
  const response = await fetch(`http://127.0.0.1:8000/users/${name}?user_bool=1`, {
      method:'GET', 
  })
  // console.log(response.json())
  const data = await response.json()
  // console.log(data.exists);

  if (data.exists) {
      // Redirect to home.html if key is true
      // await follower_stories(data.user_id); 
      // console.log(data);
      const encoded_data = encodeURIComponent(data.user_id);
      window.location.replace(`http://127.0.0.1:5500/static/index.html?user=${encoded_data}`);
      
      // console.log(userid); 
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


async function load_home() {
  const urlParams = new URLSearchParams(window.location.search);
  const encodeduser = urlParams.get('user');
  const userid = decodeURIComponent(encodeduser);
  // console.log(userid);
  try {
        const response = await fetch(`http://127.0.0.1:8000/followers/${userid}`, {
            method:'GET',
        });
        const user_data = await fetch(`http://127.0.0.1:8000/followers/${userid}?self=1`, {
            method:'GET',
        });
        const user = await user_data.json()
        console.log(user);
        const userinfo = document.querySelectorAll('#user-card p');
        userinfo[0].textContent = user.username;
        // const userbio = document.querySelector('#user-card .sub-text');
        userinfo[1].textContent = user.bio;
        await suggestions();
      // console.log(response.json())
      const followers = await response.json()
        // console.log(followers.profile_photo_url.length);
        const profileElements = document.querySelectorAll('#user-card img, .user .profile-pic img, .comment-wrapper img');
        for (let i=0; i<profileElements.length; i++){
          console.log(user.profile_photo_url);
          profileElements[i].src = user.profile_photo_url;
        }
        const imgElements = document.querySelectorAll('.status-card img');
        console.log(imgElements);
        // loop through img elements and set src attribute to corresponding image URL from response data
        for (let i=0; i<imgElements.length; i++){
          imgElements[i].src = followers.profile_photo_url[i];
        }
        const textElements = document.querySelectorAll('.status-card .username');
        for (let i=0; i<textElements.length; i++){
          textElements[i].textContent = followers.username[i];
        }
        await posts(user.username);
      // window.addEventListener('load', () => {
        // profileElement.src = user.profile_photo_url;
    }
      catch (error) {
        console.log(error) 
      }
}

async function suggestions() {
  const urlParams = new URLSearchParams(window.location.search);
  const encodeduser = urlParams.get('user');
  const userid = decodeURIComponent(encodeduser);
  // console.log(userid);
  try {
        const response = await fetch(`http://127.0.0.1:8000/followers/${userid}?suggestion=true`, {
            method:'GET',
        });
        const suggestion = await response.json()
        console.log(`SUGGG: ${suggestion.profile_photo_url}`);
        const sugg_text = document.querySelectorAll('.suggestion-card p');
        const sugg_pic = document.querySelector('.suggestion-pic img');
        sugg_text[0].textContent = suggestion.username;
        sugg_text[1].textContent = suggestion.bio;
        sugg_pic.src = suggestion.profile_photo_url;
  }
  catch (error) {
    console.log(error) 
  }
}

async function posts(name) {
  const urlParams = new URLSearchParams(window.location.search);
  const encodeduser = urlParams.get('user');
  const userid = decodeURIComponent(encodeduser);
  try {
    const response = await fetch(`http://127.0.0.1:8000/posts/${userid}?rand_post=true`, {
        method:'GET',
    });
    const post = await response.json()
    console.log(post);
    const user_post = document.querySelector('.user p');
    const user_post2 = document.querySelector('.description span');
    const user_cap = document.querySelector('.description');
    const likes = document.querySelector('.likes');
    const image = document.querySelector('.post-image');
    user_post.textContent = name;
    user_post2.textContent = name;
    user_cap.textContent = post.caption;
    likes.textContent = `${post.likes}${post.likes * 5} likes`;
    image.src = post.url;
//     sugg_text[0].textContent = suggestion.username;
//     sugg_text[1].textContent = suggestion.bio;
}
catch (error) {
console.log(error) 
}
}

function logout()
{
  window.location.replace('http://127.0.0.1:5500/static/login.html');
}
