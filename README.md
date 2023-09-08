
# Currency Converter Application

This is a PyQt5-based currency converter application. This application allows users to convert between different currencies and view current exchange rates.


## Features
- Conversion between different currencies
- Viewing current exchange rates.
- User friendly interface.

## How to use
1. When the application starts, select a currency from the left side and another currency from the right side.
2. You can perform the conversion by clicking the "Convert" button.
3. You can clear the selected currencies and start a new conversion by clicking the "Clear" button.
4. Click the "Current Rates" button to view the current exchange rates.


## Code Explanation 


- First, the required libraries and modules are imported. These libraries include `requests`, `time`, `BeautifulSoup`, and PyQt5.

- The `requests` library is used to fetch currency data from a specific URL, and this data is processed with `BeautifulSoup`.

- Currency units and their values are extracted from the data obtained from the website and stored in two separate lists (`liste_birim` and `liste_değer`). These lists contain the names of currency units and their respective values.

- Some special operations are performed, such as removing the dollar sign ($), converting commas (,) to periods (.), and adjusting some values by multiplying with units.

- A class named `Ui_Form` is created, which is used to build a user interface (UI) using PyQt5.

- UI design is defined within the `setupUi` method of this class. The design includes several buttons and radio buttons representing currency units.

- The `buttons` method is used to connect click functions to the buttons. For example, when the "Clear" button is clicked, the `temizle_func` method is called.

- The `temizle_func` method clears the text area and deselects the radio buttons.

- The `guncel_kur_print` method prints the current currency exchange rates to the text area.

- The `donustur_fuc` method performs the currency conversion process. First, it checks the amount entered by the user and the selected currency units. Then, it performs the conversion and writes the result to the text area.

- The `if __name__ == "__main__"` block initiates the execution of the program and creates a window with PyQt5.

## Compilation and Execution

To compile and run the code for the currency conversion application, follow these steps:

1. Save the code in a Python file with a .py extension (e.g., currency_converter.py).

2. Open a terminal or command prompt and navigate to the directory where the file is saved.

3. Ensure you have the required Python libraries installed. You can install them using pip:

   ```
   pip install requests beautifulsoup4 PyQt5
   ```

4. Run the Python script:

   ```
   python currency_converter.py
   ```

5. The application window will open, allowing you to interact with it.

**Note:** This code assumes you have Python and the necessary libraries installed on your system.

## OUTPUT


![doviz_interface](https://github.com/aksoyorcun/Currency-Converter/assets/136446246/e1b81d9b-3ad2-4654-acad-ac0635f40470)



