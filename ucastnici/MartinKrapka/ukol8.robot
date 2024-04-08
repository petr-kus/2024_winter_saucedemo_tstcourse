*** Settings ***
Documentation     Test cases for saucedemo.com
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://www.saucedemo.com/
${BROWSER}        Chrome

*** Test Cases ***
Valid Login
    [Documentation]    Test valid login functionality
    Open Browser To Login Page
    Input Username    problem_user
    Input Password    secret_sauce
    Submit Credentials
    Wait For Welcome Page
    [Teardown]    Close Browser

Login with incorrect Username and Password
    [Documentation]    Test the behavior of unsuccessful login with incorrect username and password
    Open Browser To Login Page
    Input Username    locked_out_user
    Input Password    secret_sauce
    Submit Credentials
    Error Message Should Be Displayed
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Wait Until Page Contains Element    user-name

Input Username
    [Arguments]    ${username}
    Input Text    user-name    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Click Button    Login

Wait For Welcome Page
    Wait Until Page Contains Element    //div[@id='inventory_filter_container']
    Title Should Be    Swag Labs

Error Message Should Be Displayed
    Wait Until Page Contains Element    class: error-button
    Element Should Contain    class: error-button 