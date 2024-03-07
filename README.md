# Password Generator

## Overview

This Python script generates random passwords of specified lengths. It utilizes the `random` module to randomly select characters from a predefined character set. The progress of password generation is visualized using the `tqdm` library, and the final password is displayed with a processing message.

## Features

- Generates random passwords of specified lengths.
- Progress visualization using the `tqdm` library.
- Supports customizing the length of the password.
- Provides a processing message upon completion.

## Dependencies

- Python 3.x
- tqdm

## Usage

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies using pip:
   ```
   pip install tqdm
   ```
4. Run the script:
   ```
   python password_generator.py
   ```
5. Follow the prompts to specify the length of the password.
6. Once the password is generated, it will be displayed with a processing message.

## Example

```
$ python password_generator.py
Enter the length of the password: 10
```
```
Processing..... Almost there
Processing complete.
Password is: q6!Gx#3tPz
```


