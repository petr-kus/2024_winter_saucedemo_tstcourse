*** Settings ***
Documentation     basic test of saucedemo.com
Library           SeleniumLibrary

*** Variables ***
${URL}            https://www.saucedemo.com/
${BROWSER}        Chrome
${USERNAME}       standard_user
${PASSWORD}       secret_sauce
${FIRST_NAME}     Chandler
${LAST_NAME}      Bing
${POSTAL_CODE}    70030

*** Test Cases ***
Login Test
    [Documentation]    Test Case for logging in with valid credentials.
    Open Browser To Login Page
    Login credentials
    Click Button    login-button
    Page Should Contain Element    id:inventory_container
   

Add Item To Cart Test
    [Documentation]    Test Case for adding an item to the shopping cart.
    Slow Down
    Submit click for product
    Slow Down
    Click Button  add-to-cart
    Page Should Contain Element    id:shopping_cart_container

Checkout Test
    [Documentation]    Test Case for checkout process.
    Slow Down
    Checkout start
    Slow Down
    Checkout credentials
    Slow Down
    Click Button    continue
    Slow Down
    Checkout Final Part
    Page Should Contain    Swag Labs

Footer Link Test
    [Documentation]    Test Case for navigating to footer link.
    Click Footer Link

Logout Test
    [Documentation]    Test Case for logging out.
    Slow Down
    Click Element    react-burger-menu-btn
    Slow Down
    Click Element    logout_sidebar_link
    Page Should Contain Element    login-button
    [Teardown]    Close Browser


*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Swag Labs

Login credentials
    Wait Until Element Is Visible    id:user-name    timeout=10s
    Input Text    id:user-name    ${USERNAME}
    Wait Until Element Is Visible    id:password    timeout=10s
    Input Text    id:password    ${PASSWORD}


Submit click for product
    Click Link  Sauce Labs Backpack

Click Footer Link
    [Documentation]    Clicks on the footer link and switches to the new window.
    Execute JavaScript    window.scrollTo(0, document.body.scrollHeight);
    Slow Down
    Click Element    css:#page_wrapper footer ul li a
    Switch Window    NEW
    Sleep    4s
    Switch Window    MAIN
    ${window_handles}=    Get Window Handles
    Length Should Be    ${window_handles}    2    

Checkout start
    Click Element    shopping_cart_container
    Slow Down
    Click Element    checkout

Checkout credentials
    [Documentation]    Fills in checkout credentials.
    Wait Until Element Is Visible    id:first-name    timeout=10s
    Input Text    id:first-name    ${FIRST_NAME}
    ${first_name_value}=    Get Element Attribute    id:first-name    value
    Should Be Equal As Strings    ${first_name_value}    ${FIRST_NAME}
    Wait Until Element Is Visible    id:last-name    timeout=10s
    Input Text    id:last-name    ${LAST_NAME}
    ${last_name_value}=    Get Element Attribute    id:last-name    value
    Should Be Equal As Strings    ${last_name_value}    ${LAST_NAME}
    Wait Until Element Is Visible    id:postal-code    timeout=10s
    Input Text    id:postal-code    ${POSTAL_CODE}
    ${postal_code_value}=    Get Element Attribute    id:postal-code    value
    Should Be Equal As Strings    ${postal_code_value}    ${POSTAL_CODE}


Checkout Final Part
    Click Button    finish
    Click Button    back-to-products

Slow Down
    Sleep    3s


