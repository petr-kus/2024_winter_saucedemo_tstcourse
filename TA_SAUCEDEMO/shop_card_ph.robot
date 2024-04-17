*** Settings ***
Documentation    
...    Variables and Keywords for Shopping Cart section check
...    Contains proofs whether actions are working right
Library    SeleniumLibrary

*** Variables ***
${shopping_cart}    id:shopping_cart_link
${continue_shopping}    id:continue-shopping
${quantity_label}    class:cart_quantity_label
${description_label}    class:cart_desc_label
${inventory_name}    class:inventory_item_name
${checkout}    id:checkout
${URL_inventory}    https://www.saucedemo.com/inventory.html
${URL_shopping_cart}    https://www.saucedemo.com/cart.html
${URL_checkout}    https://www.saucedemo.com/checkout-step-one.html
${current_url}    Get Location

${add_backpack}    id:add-to-cart-sauce-labs-backpack
${add_bike_light}    id:add-to-cart-sauce-labs-bike-light
${add_bolt_tshirt}    id:add-to-cart-sauce-labs-bolt-t-shirt
${add_jacket}    id:add-to-cart-sauce-labs-fleece-jacket
${add_onesie}    id:add-to-cart-sauce-labs-onesie
${add_test_tshirt}    id:add-to-cart-test.allthethings()-t-shirt-(red)

*** Keywords ***
Add Items To Cart And Check Shopping Cart Section
    [Documentation]    This keyword adds items to the cart and afterwards click on shopping cart to check whether the right items were added to it.
    [Arguments]     ${description_label}    ${inventory_name}
    Click Button    ${add_backpack}
    Click Button    ${add_bike_light}
    Click Button    ${add_bolt_tshirt}
    Click Button    ${add_jacket}
    Click Button    ${add_onesie}
    Click Button    ${add_test_tshirt}
    Should Be Equal    ${description label}    ${inventory name}

Verify whether we are successfully back on the page with items.
    [Documentation]    This keyword clicks on "Continue Shopping" in Shopping cart section and verify whether we are on the page with items.
    [Arguments]     ${URL_inventory}    ${current_url}
    Click Button    ${continue_shopping}
    Should Be Equal    ${URL_inventory}    ${current_url}

Verify whether we are successfully back in Shopping Cart section.
    [Documentation]    This keyword clicks on "Shopping cart" and verify whether we are on the right page.
    [Arguments]     ${URL_shopping_cart}    ${current_url}
    Click Button    ${shopping_cart}
    Should Be Equal    ${URL_shopping_cart}    ${current_url}

Verify whether we are successfully in "Checkout" section.
    [Documentation]    This keyword clicks on "Checkout" button and verify whether we are on the right page.
    [Arguments]     ${URL_checkout}    ${current_url}
    Click Button    ${checkout}
    Should Be Equal    ${URL_checkout}    ${current_url}

