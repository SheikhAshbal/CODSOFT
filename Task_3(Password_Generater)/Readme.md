<h1>Password Generator</h1>
This is a simple password generator program that allows users to generate strong and random passwords.

<h2>Instructions:</h2>
Run the program by executing the main() function.
The program will generate a password based on the default or user-specified length.
Choose options to regenerate the password, change the password length, copy the generated password to the clipboard, or exit the program.
To regenerate the password, enter '1'.
To change the password length, enter '2' and follow the prompts.
To copy the generated password to the clipboard, enter '3'.
To exit the program, enter '4'.
<h2>Functions:</h2>
generate_password(length): Generates a random password with the specified length using letters (both upper and lower case) and digits.

Password_length(): Prompts the user to enter the desired length for the password. Validates that the length is a positive integer.

password_generator_menu(): Displays the generated password and provides a menu for users to choose various options.

main(): Calls the password_generator_menu() function to start the password generator.