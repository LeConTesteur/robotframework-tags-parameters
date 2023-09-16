*** Setting ***
Library    robotframework_tags_parameters.TagsParameters
Library    OperatingSystem
Library    Collections

*** Variable ***
${SCHEMA_PATH}    ${CURDIR}/schema_file.json

*** Test Case ***
Test
    [Tags]    foo    bar    no-reset    name:FOO
    ${result}=    Convert Tags To Dict    ${SCHEMA_PATH}
    Log    ${result}
    Dictionary Should Contain Item    ${result}     foo    ${True}
    Dictionary Should Contain Item    ${result}     name    FOO
    Dictionary Should Contain Item    ${result}     reset    ${False}