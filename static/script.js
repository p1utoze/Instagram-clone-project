async function getLogin_redirect() {
    const loginForm = document.getElementById("login-form")

    // Add an event listener to the form submit event
    loginForm.addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent the form from submitting normally

  // Get the username and password values
  const email = document.getElementById('login_mail').value;
  const password = document.getElementById('password').value;

  // Make the GET request to the API endpoint
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
      } else {
        // Display an error message if key is false
        const errorMsg = document.getElementById('error-msg');
        errorMsg.textContent = 'Incorrect email or password';
        errorMsg.style.display = 'block';
      }

  } catch (error) {
    console.log(error)
  }
  });
}