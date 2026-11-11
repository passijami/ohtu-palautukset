
*** Settings ***
Resource    resource.robot

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Application Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username    newuser
    Set Password    password123
    Set Password Confirmation    password123
    Click    role=button[name="Register"]
    Register Should Succeed

Register With Matching Password And Confirmation
    Set Username    matchingconfirmation
    Set Password    password123
    Set Password Confirmation    password123
    Click    role=button[name="Register"]
    Register Should Succeed

Register With Nonmatching Password And Confirmation
    Set Username    nonmatchingconfirmation
    Set Password    password123
    Set Password Confirmation    password456
    Click    role=button[name="Register"]
    Register Should Fail With Message    Passwords do not match

Register With Too Short Username And Valid Password
    Set Username    ab
    Set Password    password123
    Set Password Confirmation    password123
    Click    role=button[name="Register"]
    Register Should Fail With Message    Username

Register With Valid Username And Too Short Password
    Set Username    newuser
    Set Password    short
    Set Password Confirmation    short
    Click    role=button[name="Register"]
    Register Should Fail With Message    Password

Register With Username That Is Already In Use
    Set Username    existinguser
    Set Password    password123
    Set Password Confirmation    password123
    Click    role=button[name="Register"]
    Register Should Fail With Message    Username

Register With Password Containing Numbers
    Set Username    userwithnumbers
    Set Password    kalle123
    Set Password Confirmation    kalle123
    Click    role=button[name="Register"]
    Register Should Succeed

Register With Password Containing Special Characters
    Set Username    userwithspecialchars
    Set Password    kalle#abc
    Set Password Confirmation    kalle#abc
    Click    role=button[name="Register"]
    Register Should Succeed

Register With Password Containing Only Lowercase Letters
    Set Username    userlowercase
    Set Password    kallekalle
    Set Password Confirmation    kallekalle
    Click    role=button[name="Register"]
    Register Should Fail With Message    Password

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username    usermixedcase
    Set Password    KalleKalle
    Set Password Confirmation    KalleKalle
    Click    role=button[name="Register"]
    Register Should Fail With Message    Password


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User    existinguser    password123
    Go To Register Page

Register Should Succeed
    Get Title    ==    Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]    ${message}
    Get Title    ==    Register
    Get Text    body    *=    ${message}

