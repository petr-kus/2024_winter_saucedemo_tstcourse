
#Vylepšení lektora
*** Variables ***
${user_name_field}    id:user-name 
${password_field}     id:password


*** Keywords ***
Login ${user} with password ${password}
        Wait Until Element Is Visible    ${user_name_field}    timeout=10s
        Input Text    ${user_name_field}    ${user}
        Wait Until Element Is Visible    ${password_field}   timeout=10s
        Input Text    ${password_field}    ${password}