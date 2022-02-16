# Appium Allure pytest Example

This is an example project that uses Appium, pytest and allure to implement UI tests for a Plant Manager application. 

The application is built already for iOS simulator and Android and available under the `apps/` folder. 

## Setup

To create a virtual environment and install all dependencies:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Running the tests

To run the tests, run the following commands:

```
#start the appium server
appium 

#choose the platform you want to run on, ios or android
export running_platform=android 

#start the tests
pytest
```
