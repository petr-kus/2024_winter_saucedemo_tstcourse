*** Keywords ***
Login And Verify Dashboard
    [Arguments]    ${username}
    [Documentation]    Login and verify for user
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    0.5s
    Input Text    id=user-name    ${username}
    Input Text    xpath://*[@id="password"]    ${PASSWORD}
    Click Button    id=login-button


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