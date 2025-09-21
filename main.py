from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value

    # Clear the output div first
    document.querySelector("#output").innerText = ""

    # Multiline message using input values
    message = f"""👤 Student Profile
    Name   : {name}
    Age    : {age}
    School : {school}

    ✏️ Notes:
    {name} is now {age} years old and goes to {school}.
    This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript.
    """

    display(message, target="output")

