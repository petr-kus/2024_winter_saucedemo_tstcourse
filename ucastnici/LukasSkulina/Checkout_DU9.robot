*** Settings ***
Documentation     basic test of saucedemo.com
Library           SeleniumLibrary
Resource          checkout_scenarios.robot
Test Setup        Set Selenium Speed    1

*** Variables ***
${FIRST_NAME}     Chandler
${LAST_NAME}      Bing
${POSTAL_CODE}    70030

*** Test Cases ***

Checkout Test
    [Documentation]    Testing of checkout process.
    Checkout start
    Verify Character Limit for First and Last Name
    Click Continue Without Filling Requierd Fields
    Continue button redirects to Order Overview with valid credentials
    Verify that Checkout Overview contains order summary data
    Close Browser