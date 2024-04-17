*** Settings ***
Documentation     basic test of saucedemo.com
Library           SeleniumLibrary
Resource          DU9_login_page_users.robot
Resource          DU9_login_page_keywords.robot
Resource          checkout_scenarios.robot
Resource          shop_card_ph.robot
Resource          inv_p.robot

Test Setup        Set Selenium Speed    1

*** Variables ***
${FIRST_NAME}     Chandler
${LAST_NAME}      Bing
${POSTAL_CODE}    70030

*** Test Cases ***

Login And Verify For Standard User
    Login And Verify Dashboard    ${STANDARD_USER}
    Verify User Is Logged In
    #Logout And Verify User Is Logged Out

#Checkout Test
#    [Documentation]    Testing of checkout process.
#    Checkout start
#    Verify Character Limit for First and Last Name
#    Click Continue Without Filling Requierd Fields
#    Continue button redirects to Order Overview with valid credentials
#    Verify that Checkout Overview contains order summary data
#    Close Browser

Test1
    Add Items To Cart And Check Shopping Cart Section
Test2
    Verify whether we are successfully back on the page with items.
Test3
    Verify whether we are successfully back in Shopping Cart section.
Test4
    Verify whether we are successfully in "Checkout" section.





