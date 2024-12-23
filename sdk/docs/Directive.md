# Directive

Class that encapsulates directive (system prompt) content and its application to the llm dialogue.      

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | **str** |  | [optional] [default to ' * ']
**hide** | **bool** |  | [optional] [default to True]
**identity** | [**AnyOf**](AnyOf.md) |  | [optional] 
**purpose** | [**AnyOf**](AnyOf.md) |  | [optional] 
**style** | [**AnyOf**](AnyOf.md) |  | [optional] 
**restriction** | [**AnyOf**](AnyOf.md) |  | [optional] 
**context_vals** | **Dict[str, str]** |  | [optional] 

## Example

```python
from finbourne_candela.models.directive import Directive

# TODO update the JSON string below
json = "{}"
# create an instance of Directive from a JSON string
directive_instance = Directive.from_json(json)
# print the JSON string representation of the object
print Directive.to_json()

# convert the object into a dict
directive_dict = directive_instance.to_dict()
# create an instance of Directive from a dict
directive_form_dict = directive.from_dict(directive_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


