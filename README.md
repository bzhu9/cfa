# Chick-Fil-A OCR
A selenium web automation that submits Chick-Fil-A missed point transactions for you. It signs in and redeems points from your receipt.

## Installation
Requires Python 3.9 or above.

### Code and Dependencies
```console
$ git clone https://github.com/bzhu9/cfa.git
$ cd cfa
$ pip install -r requirements.txt
```

### Chrome Browser / Chrome Driver Version
Make sure to have the correct chromedriver version that matches your current Chrome Browser Version.

See https://chromedriver.chromium.org/downloads for more versions.

### Chrome Profile
When using selenium, it is often a good idea to create a separate Chrome profile to isolate your regular browser history from the script.

Your Chrome profiles can be found at:<br>
#### **`Windows`**
```
C:\Users\$USER\AppData\Local\Google\Chrome\User Data\<yourprofile>
```

#### **`Mac OSX`**
```
/Users/$USER/Library/Application Support/Google/Chrome/<yourprofile>
```

### Automated Login
Your Chick-Fil-A account credentials are required to execute the script. Create a new file as such:
#### **`password.py`**
```python
email = "<youremail@email.com>"
password = "<yourpassword>"
chrome_profile = "<pathtochromeprofile>"
```

## Usage
```console
$ python3 cfa.py
```
