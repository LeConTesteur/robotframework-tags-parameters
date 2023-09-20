# robotframework-tags-parameters
![build](https://github.com/LeConTesteur/robotframework-tags-parameters/actions/workflows/build.yml/badge.svg)


## Description

This project want simplify the complexity of initialisation and test by send
data with tag.

This project can convert robotframework tag to dictionary. For this, the project
use jsonschema for declare and annotate tag.

### Example

```robotframework
*** Setting ***
Library    TagsParameters
Test Setup    Generic Test Setup


*** Test Case ***
Test1
    [Tags]    foo    bar    no-reset    name:FOO
    No Operation

Test2
    [Tags]    reset    name:BAR
    No Operation

Test3
    [Tags]    foo    bar
    No Operation

*** Keyword ***
Generic Test Setup
    ${result}=    Convert Tags To Dict    ${CURDIR}/schema_file.json
    Run Keyword If    ${result.foo}    Keyword1
    Run Keyword If    "${result.name}" == "BAR"    Keyword2
    ...
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install robotframework-tags-parameters
```

## Usage

Import the library into you project

```robotframework
*** Setting ***
Library    TagsParameters
Library    Collections


*** Test Case ***
Test
    [Tags]    foo    bar    no-reset    name:FOO
    ${result}=    Convert Tags To Dict    ${CURDIR}/schema_file.json
    Log    ${result}
    Dictionary Should Contain Item    ${result}     foo    ${True}
    Dictionary Should Contain Item    ${result}     name    FOO
    Dictionary Should Contain Item    ${result}     reset    ${False}
```

Use the json schema for description tags structure:
```json
{
  "description": "My Tags",
  "type": "object",
  "properties": {
    "foo": {
      "type": "boolean"
    },
    "name": {
      "type": "string"
    },
    "reset": {
      "type": "boolean",
      "default": true,
      "false-prefix": "no"
    }
  }
}
```

## Tags schema

### Boolean

Simple boolean can be declared with the next jsonschema. By default **foo** is *false*:

```json
{
  "description": "My Tags",
  "type": "object",
  "properties": {
    "foo": {
      "type": "boolean"
    }
  }
}
```
For set **foo** :
```robotframework
*** Test Case ***
True Foo
    [Tags]    foo
    Should Be Equal   ${result.foo}     ${True}

Default Tags
    Should Be Equal   ${result.foo}     ${False}
```

If you want by default, *true* boolean,you can use **default** attribute.
For declare *false* with tag, you need use **false-prefix** attribute.
**false-prefix** can be take anybody value.
```json
{
  "description": "My Tags",
  "type": "object",
  "properties": {
    "foo": {
      "type": "boolean",
      "default": false,
      "false-prefix": "no"
    }
  }
}
```
For set **foo** :
```robotframework
*** Test Case ***
False Foo
    [Tags]    no-foo
    Should Be Equal   ${result.foo}     ${False}

True Foo
    [Tags]    foo
    Should Be Equal   ${result.foo}     ${True}

Default Tags
    Should Be Equal   ${result.foo}     ${True}
```

You can change too, the prefix for *true* value with **true-prefix** attribute.
**true-prefix** can be take anybody value.
```json
{
  "description": "My Tags",
  "type": "object",
  "properties": {
    "foo": {
      "type": "boolean",
      "true-prefix": "with",
      "false-prefix": "without"
    }
  }
}
```
For set **foo** :
```robotframework
*** Test Case ***
False Foo
    [Tags]    without-foo
    Should Be Equal   ${result.foo}     ${False}

True Foo
    [Tags]    with-foo
    Should Be Equal   ${result.foo}     ${True}

Default Tags
    Should Be Equal   ${result.foo}     ${False}
```

### String

Simple string can be declared with the next jsonschema. By default **foo** is *None*:

```json
{
  "description": "My Tags",
  "type": "object",
  "properties": {
    "foo": {
      "anyOf": [
        {"type": "string"},
        {"type": "null"},
      ]
    }
  }
}
```
For set **foo** :
```robotframework
*** Test Case ***
Tag Foo with BAR value
    [Tags]    foo:BAR
    Should Be Equal   ${result.foo}     BAR

Default Tags
    Should Be Equal   ${result.foo}     ${{None}}
```

You can use too a **type checking** as like:

```json
{
  "description": "My Tags",
  "type": "object",
  "properties": {
    "foo": {
      "type": "string",
      "maxLength": 3
    }
  }
}
```
For set **foo** :
```robotframework
*** Test Case ***
Tag Foo with BAR value
    [Tags]    foo:BAR
    Should Be Equal   ${result.foo}     ${BAR}

Tag Foo with BAAR value
    [Tags]    foo:BAAR
    [Documentation]  Validation Error is throw

```


### Integer

Simple string can be declared with the next jsonschema.:

```json
{
  "description": "My Tags",
  "type": "object",
  "properties": {
    "foo": {
      "type": "integer",
      "default": "0"
    }
  }
}
```
For set **foo** :
```robotframework
*** Test Case ***
Tag Foo
    [Tags]    foo:5
    Should Be Equal   ${result.foo}     ${5}

Default Tags
    Should Be Equal   ${result.foo}     ${0}
```

### Default Value

Default value can be declared with the next jsonschema. By default **foo** is *${EMPTY}*:

```json
{
  "description": "My Tags",
  "type": "object",
  "properties": {
    "foo": {
      "type": "string",
      "default": ""
    }
  }
}
```
For set **foo** :
```robotframework
*** Test Case ***
Tag Foo with BAR value
    [Tags]    foo:BAR
    Should Be Equal   ${result.foo}     BAR

Default Tags
    Should Be Equal   ${result.foo}     ${EMPTY}
```

## JsonSchema

For more explication into jsonschema, see [https://json-schema.org/](https://json-schema.org/)
You can too see [argparse-from-jsonschema](https://github.com/LeConTesteur/argparse-from-jsonschema)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Tests

Run tests with tox command :

```bash
tox
tox -e testsacc
```