*** Setting ***
Library           TagsParameters
Library           Collections
Documentation     Tags work into case setup and teardown.
...               THe walue must be returned

*** Variable ***
${SCHEMA_PATH}    ${CURDIR}/schema_file.json
${SCHEMA_TYPE_CHECKING_PATH}    ${CURDIR}/schema_file_with_type_checking.json
${SCHEMA_INT_PATH}    ${CURDIR}/schema_file_int.json

*** Test Case ***
Test
    [Setup]    Validation Tags
    [Teardown]    Validation Tags
    [Tags]    foo    bar    no-reset    name:FOO
    [Documentation]    Foo must be true, name must be FOO and reset muse be false
    Validation Tags

Name with Space
    [Tags]    name:FOO${SPACE}bar
    [Documentation]    Name must be "FOO BAR"
    ${result}=    Convert Tags To Dict    ${SCHEMA_PATH}
    Dictionary Should Contain Item    ${result}    name    FOO bar

Tag name with BAR value
    [Tags]    name:BAR
    [Documentation]    **name** to *BAR*
    ${result}=    Convert Tags To Dict    ${SCHEMA_PATH}
    Dictionary Should Contain Item    ${result}    name    BAR
    Log    ${result.foo}

Tag name with BAAR value
    [Tags]    name:BAAR
    [Documentation]    ValidationError is throw
    Run Keyword And Expect Error    ValidationError: 'BAAR' is too long*    Convert Tags To Dict    ${SCHEMA_TYPE_CHECKING_PATH}

Tag Foo
    [Tags]    foo:5
    [Documentation]    **foo** to *5*
    ${result}=    Convert Tags To Dict    ${SCHEMA_INT_PATH}
    Dictionary Should Contain Item    ${result}    foo    ${5}

Default Tags
    [Documentation]    **foo** to *0*
    ${result}=    Convert Tags To Dict    ${SCHEMA_INT_PATH}
    Dictionary Should Contain Item    ${result}    foo    ${0}

Can Use DotDict
    ${result}=    Convert Tags To Dict    ${SCHEMA_INT_PATH}
    Should Be Equal    ${result.foo}    ${0}

*** Keywords ***
Validation Tags
    ${result}=    Convert Tags To Dict    ${SCHEMA_PATH}
    Log    ${result}
    Dictionary Should Contain Item    ${result}    foo    ${True}
    Dictionary Should Contain Item    ${result}    name    FOO
    Dictionary Should Contain Item    ${result}    reset    ${False}
