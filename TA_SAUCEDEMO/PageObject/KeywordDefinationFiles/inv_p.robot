*** Settings ***
Documentation    
...    Variables and Keywords for Inventory Page
...    Contains all possible actions on Inventory page
Library    SeleniumLibrary


*** Variables ***
${menu_button}    id:react-burger-menu-btn
${all_items_button}    id:inventory_sidebar_link
${about_button}    id:about_sidebar_link
${logout_button}    id:logout_sidebar_link
${reset_button}    id:reset_sidebar_link

${item_backpack_link}    id:item_4_title_link
${add_backpack}    id:add-to-cart-sauce-labs-backpack
${remove_backpack}    id:remove-sauce-labs-backpack

${item_bike_light_link}    id:item_0_title_link
${add_bike_light}    id:add-to-cart-sauce-labs-bike-light
${remove_bike_light}    id:remove-sauce-labs-bike-light

${item_bolt_tshirt_link}    id:item_1_title_link
${add_bolt_tshirt}    id:add-to-cart-sauce-labs-bolt-t-shirt
${remove_bolt_shirt}    id:remove-sauce-labs-bolt-t-shirt

${item_jacket_link}    id:item_5_title_link
${add_jacket}    id:add-to-cart-sauce-labs-fleece-jacket
${remove_jacket}    id:remove-sauce-labs-fleece-jacket

${item_onesie_link}    id:item_2_title_link
${add_onesie}    id:add-to-cart-sauce-labs-onesie
${remove_onesie}    id:remove-sauce-labs-onesie

${item_test_tshirt_link}    id:item_3_title_link
${add_test_tshirt}    id:add-to-cart-test.allthethings()-t-shirt-(red)
${remove_test_tshirt}    id:remove-test.allthethings()-t-shirt-(red)

${sort_menu}    class:product_sort_container
${sort_a_z}    value:az
${sort_z_a}    value:za
${sort_low_high}    value:lohi
${sort_high_low}    value:hilo

${cart_button}    id:shopping_cart_container
${cart_badge}    class:shopping_cart_badge
${card_badge_number}    data-test:shopping-cart-badge

${twitter_button}    class:social_twitter
${facebook_button}    class:social_facebook
${linkedin_button}    class:social_linkedin



*** Keywords ***

Open Menu
    [Documentation]    This keyword opens Menu.
    Wait Until Element Is Visible     ${menu_button}    timeout=5s
    Click Button                      ${menu_button}
    Page Should Contain    About

Click On All Items
    [Documentation]    This keyword opens Inventory page if the "Open Menu" keyword has been used right before.
     Wait Until Element Is Visible    ${all_items_button}    timeout=5s
     Click Button                     ${all_items_button}
     Page Should Contain    Swag Labs
Click On About
    [Documentation]    This keyword opens About page if the "Open Menu" keyword has been used right before.
    Wait Until Element Is Visible     ${about_button}    timeout=5s
    Click Button                      ${about_button}
    Page Should Contain    Solutions  

Click On Logout
    [Documentation]    This keyword logs out the user if the "Open Menu" keyword has been used right before.
    Wait Until Element Is Visible     ${logout_button}    timeout=5s
    Click Button                      ${logout_button}
    Page Should Contain Element    id:login-button

Click On Reset 
    [Documentation]    This keyword resets the app state.
    Wait Until Element Is Visible     ${reset_button}    timeout=5s
    Click Button                      ${reset_button}



Add Items To Cart And Verify
    [Documentation]    This keyword adds items to the cart and verifies the number of items in the cart. Accepts multiple arguments
    ...    Example:
    ...    Add Items To Cart And Verify    3    ${item1}
    ...    ...    ${item2}
    ...    ...    ${item3}
    [Arguments]     ${item_amount}    ${add_item_button}
    Click Button    ${add_item_button}
    Should Be Equal    ${item_amount}    ${card_badge_number}


Remove Item From Cart And Verify
    [Documentation]    This keyword removes items from the cart and verifies that coressponding button disappered. Accepts multiple arguments
    ...    Example:
    ...    Remove Item From Cart And Verify    ${item1}
    ...    ...    ${item2}
    ...    ...    ${item3}   
    [Arguments]     ${remove_item_button}
    Click Button    ${remove_item_button}
    Element Should Not Be Visible    ${remove_item_button}

Open Product Page And Verify
    [Documentation]    This keyword opens provided link and verifies that the "Back to Products" button is present on the page.
    [Arguments]     ${product_page_link}
    Click Button    ${product_page_link}
    Page Should Contain Element    id="back-to-products"

Sort Products
    [Documentation]    This keyword changes the sorting of items on the page based on the provided sorting type.
    [Arguments]     ${sort_type}
    Click Button    ${sort_menu}
    Wait Until Element Is Visible    ${sort_type}    timeout=10s
    Click Button    ${sort_type}

Go To Cart And Verify
    [Documentation]    This keyword navigates to the shopping cart page and verifies that the cart page contains the text "Your Cart". 
    Click Button    ${cart_button}
    Page Should Contain    Your Cart

Go To SocNet
    [Documentation]    This keyword navigates to the provided social network link.
    [Arguments]     ${SocNet_type}
    Click Button    ${SocNet_type}

