
Strong Password Checker
This is a simple Java tool that checks if a password is strong.

Password must include:
At least 8 characters

At least one lowercase letter (a–z)

At least one uppercase letter (A–Z)

At least one digit (0–9)

At least one special character (like !@#$%^&*)

No more than 2 of the same character

No 3 characters in a row (like abc, 123)

Technologies:
Java 17
Docker



Dockerfile for running the app in a container

How to run with Docker:
Open terminal in the project folder

Build the image:
docker build -t strong-password .

Run the container:
docker run strong-password