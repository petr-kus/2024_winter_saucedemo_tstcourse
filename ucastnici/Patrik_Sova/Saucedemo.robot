*** Settings ***
Metadata    Author    Patrik Sova
Metadata    Purpose   RobotFramework test of saucedemo
Metadata    Created   03.24.2023

Library    SeleniumLibrary

*** Variables ***
${BROWSER}      Chrome
${URL}          https://www.saucedemo.com/
${LOGIN_NAME}   standard_user
${PASSWORD}     secret_sauce

*** Test Cases ***
Verify User Login and Logout Functionality
    Open Browser To Login Page
    Login With Credentials    ${LOGIN_NAME}    ${PASSWORD}
    Verify User Is Logged In
    Logout And Verify User Is Logged Out

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Swag Labs

Login With Credentials
    [Arguments]    ${username}    ${password}
    Input Text    id:user-name    ${username}
    Input Text    xpath://*[@id="password"]    ${password}
    Click Element    class:submit-button

Verify User Is Logged In
    Wait Until Page Contains Element    class:inventory_list    timeout=10s
    Page Should Contain     Products
    Log To Console    User is logged in.

Logout And Verify User Is Logged Out
    Click Element    id:react-burger-menu-btn
    Wait Until Page Contains Element    xpath://*[@id="logout_sidebar_link"]   timeout=5s
    Click Element    xpath://*[@id="logout_sidebar_link"]
    Wait Until Page Contains Element    id:login_credentials    timeout=10s
    Page Should Contain     Accepted usernames are
    Log To Console   User is logged out and is on the home page.

