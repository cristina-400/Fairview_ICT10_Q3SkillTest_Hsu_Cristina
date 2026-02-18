from pyscript import document, display

def sign_up(e):
    # Clear previous output
    document.getElementById("output").innerHTML = ''
    # Get password value from input field
    username = document.getElementById('username').value.strip()
    password = document.getElementById('password').value

    password_length = len(password)
    username_length= len(username)

    # Username validation
    if password_length <4:
        document.getElementById('output').innerHTML = "❌ Username must be at least 7 characters."
    else:
         document.getElementById("output").innerHTML = "✅ Username length is valid."

        # Check password length
         if password<10:
            document.getElementById("output").innerHTML = "❌ Password must be at least 10 characters."
         else:
            document.getElementById("output").innerHTML = "✅ Password length is valid."

        
    