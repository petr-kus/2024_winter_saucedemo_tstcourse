*** Settings ***
Library    SeleniumLibrary
Library    CSVLibrary

*** Variables ***
${LOGIN_URL}     https://www.saucedemo.com
${BROWSER}       Chrome
${LOGIN_DATA}    login_data.csv

*** Test Cases ***
Valid Login
    Set Selenium Implicit Wait    10
    @{list}=    Read Csv File To List    ${LOGIN_DATA}
    FOR    ${row}    IN    @{list[1:]}
        ${username}    ${password}    ${expected}    Set Variable    ${row}
        Open Browser    ${LOGIN_URL}    ${BROWSER}
        Login With Credentials    ${username}    ${password}    ${expected}
    END

*** Keywords ***
Login With Credentials
    [Arguments]    ${username}    ${password}    ${expected}
    Input Text    user-name    ${username}
    Input Password    password     ${password}
    Click Element    login-button
    Run Keyword And Continue On Failure    Location Should Be    ${expected}
    