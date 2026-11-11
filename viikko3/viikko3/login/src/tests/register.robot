
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

