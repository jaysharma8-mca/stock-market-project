## Stock Market Project

## Description
This project is a Python-based stock market application that calculates key metrics for stocks such as:

- Dividend Yield
- P/E Ratio
- Volume Weighted Stock Price (VWSP)
- GBCE All Share Index

The application tracks trades and allows users to perform calculations for individual stocks based on recorded trades. It is designed with modularity in mind and can be easily extended for production use.

## Features
- Record trades for stocks with timestamps, prices, and quantities.
- Calculate the Dividend Yield and P/E Ratio based on stock data.
- Calculate the Volume Weighted Stock Price based on trades made in the last 15 minutes.
- Calculate the GBCE All Share Index using the geometric mean of all stocks' VWSPs.
- In-memory data storage (no external database needed).

## Technologies Used
- Python 3.7+
- unittest for testing
- logging for monitoring and debugging
- Thread safety via threading.Lock

## Project Structure
stock_market_project/
├── stock.py           # Main functionality for stock calculations
├── exceptions.py      # Custom exceptions for better error handling
├── test_stock.py      # Unit tests for the project
├── main.py            # User interaction and menu for the stock market system
└── README.md          # Project documentation

## Setup and Installation
 # Prerequisites
  - Python 3.7 or higher installed on your system.
  - Ensure pip is installed for installing required packages.

 # Step 1: Clone the repository
  - git clone <repository-url>
  - cd stock_market_project

 # Step 2: Create a virtual environment (optional)
  - python -m venv venv
  - source venv/bin/activate    # On macOS/Linux
  - venv\Scripts\activate       # On Windows

 # Step 3: Install dependencies
  - There are no external dependencies, as this project uses Python's standard libraries (unittest, logging, threading).

## Running the Application
 - You can run the stock market application using main.py. Follow the on-screen menu to select your desired option.
 - python main.py

## Menu Options:
 1. Calculate Dividend Yield
 2. Calculate P/E Ratio
 3. Record a Trade
 4. Calculate Volume Weighted Stock Price
 5. Calculate GBCE All Share Index
 6. Quit

## Running Unit Tests
 - The project includes unit tests for validating the core functionality (Dividend Yield, P/E Ratio, VWSP, GBCE Index). You can run the tests with the following command:
 - python -m unittest test_stock.py
 - If all tests pass, you should see an output similar to:
 - ----------------------------------------------------------------------
    Ran 5 tests in 0.003s

    OK

## Concurrency: Choosing Threading Over Async
 - In this project, we’ve opted to use threading.Lock for concurrency management when recording trades,  rather than switching to an async model. Here's why we made this decision:

 - Why Use Threading?
    # Simplicity:
       - The current functionality is CPU-bound and involves simple in-memory operations (like recording trades and performing stock calculations). These operations do not involve I/O-bound tasks such as network requests or database access.
       - Threading is easy to implement for this level of concurrency and effectively prevents race conditions with minimal complexity.
       - Sufficient for the Current Scale:
       - Threading with locks (via threading.Lock) is sufficient to handle the expected level of concurrency for this project, as it ensures thread-safe trade recording. This avoids potential issues like race conditions without introducing the overhead of managing an event loop or complex async patterns.
    # Why Not Use Async (Yet)?
       - While async would be more efficient for handling high-concurrency scenarios, particularly those involving I/O-bound tasks (e.g., network requests, database writes), we have decided against using it for now because:

        - Current Requirements: The project currently only handles in-memory operations with no external I/O dependencies (e.g., APIs or databases). Therefore, async’s advantages in handling concurrent I/O operations are not necessary.
        - Scalability Considerations: If the project evolves to handle real-time data feeds, multiple simultaneous trades, or integrates with external systems (like APIs or databases), async would offer better performance. At that point, refactoring to an async model with asyncio would make the application more scalable.
        - Future Consideration for Async
        - If the project grows to include:

        - Real-time trading platforms with high trade volumes
        API integrations for fetching live stock data or storing trades in a database
        Heavy I/O-bound operations (e.g., network calls, external services)
        Then transitioning to an async model would make the system more scalable and responsive, handling concurrent tasks more efficiently.

        - For now, threading offers the right balance between simplicity and concurrency, while leaving room for future scalability through async if required.





##### Constraints & Notes 
  1. Written in one of these languages - Java, C#, C++, Python 
  2. The source code should be suitable for forming part of the object model of a production application, and can be proven to meet the requirements. A shell script is not an appropriate submission for this assignment.  
  3. No database, GUI or I/O is required, all data need only be held in memory 
  4. No prior knowledge of stock markets or trading is required – all formulas are provided below. 
  5. The code should provide only the functionality requested, however it must be production quality. 

## Table1. Sample data from the Global Beverage Corporation Exchange

Stock Symbol  | Type      | Last Dividend | Fixed Dividend | Par Value
------------- | --------- | ------------: | :------------: | --------: 
TEA           | Common    |            0  |                | 100
POP           | Common    |            8  |                | 100
ALE           | Common    |            23 |                | 60
GIN           | Preferred |            8  |        2%      | 100
JOE           | Common    |            13 |                | 250


## Author

Jay Sharma


