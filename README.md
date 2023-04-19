# Nepali G2P Conversion Library
This is a simple Nepali grapheme-to-phoneme (G2P) conversion library that converts Nepali text to its phonetic representation using a predefined mapping of Nepali characters to their corresponding phonemes.

## Installation
To install the **nepali-g2p** package using **pip**, follow these steps:

- Open the command prompt (Windows) or terminal (macOS/Linux)
- Run the command **pip install nepali-g2p**
- Wait for the package and its dependencies to download and install
- Once the installation is complete, you can start using the package by importing it in your Python code using the statement **from nepali_g2p import NepaliG2P**

That's it! You have successfully installed the nepali-g2p package and can now use it in your Python projects.

## Usage
You can use the NepaliG2P class in nepali_g2p.py to convert Nepali text to phonemes. Here's an example:

```
from nepali_g2p import NepaliG2P

nepali_g2p = NepaliG2P()
nepali_text = "नमस्ते"
phonemes = nepali_g2p.convert(nepali_text)
print(phonemes)
```

This will output:

```
namastē
```

Note that this library is not perfect and may not accurately represent the pronunciation of all Nepali words.

## Dependencies
This library has no external dependencies.

## License
This library is licensed under the MIT License.
