*** Settings ***
Metadata    Author    Patrik Sova
Metadata    Purpose   Login for all users of saucedemo
Metadata    Created   14.04.2024
Resource    DU9_login_page_users.robot
Resource    DU9_login_page_keywords.robot
Library     SeleniumLibrary
#Teardown    Close Browser

*** Test Cases ***
Login And Verify For Standard User
    Login And Verify Dashboard    ${STANDARD_USER}
    Verify User Is Logged In
    #Logout And Verify User Is Logged Out

Login And Verify For Locked Out User
    Login And Verify Dashboard    ${LOCKED_OUT_USER}
    Verify User Is Logged In
    #Logout And Verify User Is Logged Out

Login And Verify For Problem User
    Login And Verify Dashboard    ${PROBLEM_USER}
    Verify User Is Logged In
    #Logout And Verify User Is Logged Out

Login And Verify For Performance Glitch User
    Login And Verify Dashboard    ${PERFORMANCE_GLITCH_USER}
    Verify User Is Logged In
    #Logout And Verify User Is Logged Out

Login And Verify For Error User
    Login And Verify Dashboard    ${ERROR_USER}
    Verify User Is Logged In
    #Logout And Verify User Is Logged Out

Login And Verify For Visual User
    Login And Verify Dashboard    ${VISUAL_USER}
    Verify User Is Logged In
    #Logout And Verify User Is Logged Out

