# Simple Banking App

A simple banking application that runs in the terminal, built using Python and SQLite3 for database management. This app allows users to create accounts, deposit money, withdraw funds, and check their account balance.

## Features

- User account creation
- Deposit and withdrawal functionalities
- Balance inquiries

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/hani-2020/Simple-banking.git
   ```

2. Navigate to the project directory:
   ```
   cd Simple-banking
   ```

3. Run the application:
   ```
   python main.py
   ```

## Code Explanation

- **Database Connection**: The application connects to an SQLite database (`database.db`) and creates a `user` table if it doesn't exist.
- **User Validation**: The `signinVerif` function checks for valid usernames and passwords, ensuring they do not consist solely of whitespace or quotation marks.
- **Account Management**: Users can sign in or create a new account via the `signin` function. The app supports deposits and withdrawals through the `deposit` and `withdraw` functions, respectively, which update the user's balance in the database.
- **Balance Display**: The `showBalance` function retrieves and displays the current balance of the user.
- **Login Functionality**: The `login` function verifies credentials and provides access to banking functionalities.

## Technologies Used

- Python
- SQLite3
