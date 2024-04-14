
*** Keywords ***  
Checkout start
    Click Element    shopping_cart_container
    Click Element    checkout
 
Click Continue Without Filling Requierd Fields
    Click Button     continue
    Page Should Contain    Error

Verify Character Limit for First and Last Name
    ${max_length_first} =    Get Element Attribute    id:first-name    maxlength
    ${max_length_last} =    Get Element Attribute    id:last-name    maxlength
    ${max_length_first} =    Set Variable If    '${max_length_first}' == 'None'    100    ${max_length_first}
    ${max_length_last} =    Set Variable If    '${max_length_last}' == 'None'    100    ${max_length_last}
    Log To Console     Maximum character limit for First Name is: ${max_length_first}
    Log To Console     Maximum character limit for Last Name is: ${max_length_last}
    ${first_length}    Get Length    ${FIRST_NAME}
    ${last_length}    Get Length    ${LAST_NAME}
    ${first_within_limit}    Evaluate    ${first_length} >= 0 and ${first_length} <= ${max_length_first}
    ${last_within_limit}    Evaluate    ${last_length} >= 0 and ${last_length} <= ${max_length_last}
    Should Be True    ${first_within_limit}    Length of '${FIRST_NAME}' should be within the limit of ${max_length_first}
    Should Be True    ${last_within_limit}    Length of '${LAST_NAME}' should be within the limit of ${max_length_last}
    Run Keyword If    ${first_within_limit}    Log To Console     Length of 'First Name' is within the range of maximum length.
    ...    ELSE    Log To Console     Length of 'First Name' is NOT within the range of maximum length.
    Run Keyword If    ${last_within_limit}    Log To Console     Length of 'Second Name' is within the range of maximum length.
    ...    ELSE    Log To Console     Length of 'Second Name' is NOT within the range of maximum length.

Continue button redirects to Order Overview with valid credentials
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
    Click Button     continue

Verify that Checkout Overview contains order summary data
    Page Should Contain    Payment
    Log To Console     The WebPage contains the information needed to make a payment.
    Page Should Contain    Shipping
    Log To Console    The WebPage contains the information needed for shipping.
    Page Should Contain    Total
    Log To Console     The WebPage contains the information needed to complete entire order.
    Click Button     Finish