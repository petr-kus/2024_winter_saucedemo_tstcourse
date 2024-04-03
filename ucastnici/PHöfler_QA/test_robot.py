*** Settings ***
Documentation   check of unuccessfull login on saucedemo.com
Library         SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://www.saucedemo.com/
${BROWSER}        Chrome

*** Test Cases ***
Login with incorrect Username and Password
    Open Browser To Login Page
    Input Username    locked_out_user
    Input Password    secret_sauce
    Submit Credentials
    Welcome Page Should Not Be Open
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Element Should Contain    class: error-button    Epic sadface: Sorry, this user has been locked out.

Input Username
    [Arguments]    ${username}
    Input Text    user-name    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Click Button    Login

Element text should be
    Element Should Contain    class: error-button    Epic sadface: Sorry, this user has been locked out.