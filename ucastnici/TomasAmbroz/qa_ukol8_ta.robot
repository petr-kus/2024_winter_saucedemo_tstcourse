*** Settings ***
Documentation     basic test of saucedemo.com
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://www.saucedemo.com/
${BROWSER}        Chrome

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username    problem_user
    Input Password    secret_sauce
    Submit Credentials
    Welcome Page Should Be Open
    Open Browser To Page Sauce Labs Backpack
    Add Backpack to cart
        [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Swag Labs

Input Username
    [Arguments]    ${username}
    Input Text    user-name    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Click Button    Login

Welcome Page Should Be Open
    Title Should Be    Swag Labs

Open Browser To Page Sauce Labs Backpack
    Title Should Be    Sauce Labs Backpack

Add Backpack to cart
    Click Button    Add to cart