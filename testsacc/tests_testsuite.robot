*** Setting ***
Library    TagsParameters
Library    Collections
Suite Setup    Validation Tags
Suite Teardown    Validation Tags
Force Tags    foo    bar    no-reset    name:FOO
Documentation    Tags doesn't work into suite setup and teardown.
...    Default must be return
*** Variable ***
${SCHEMA_PATH}    ${CURDIR}/schema_file.json

*** Test Case ***
Test
    [Tags]    foo    bar    no-reset    name:FOO
    No Operation

*** Keywords ***
Validation Tags
    ${result}=    Convert Tags To Dict    ${SCHEMA_PATH}
    Log    ${result}
    Dictionary Should Contain Item    ${result}     foo    ${False}
    Dictionary Should Contain Item    ${result}     name    ${{None}}
    Dictionary Should Contain Item    ${result}     reset    ${True}