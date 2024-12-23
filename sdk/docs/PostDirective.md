# PostDirective


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**identifier** | **str** |  | 
**description** | **str** |  | [optional] 
**version_bump** | **str** |  | [optional] [default to 'patch']
**data** | [**Directive**](Directive.md) |  | 

## Example

```python
from finbourne_candela.models.post_directive import PostDirective

# TODO update the JSON string below
json = "{}"
# create an instance of PostDirective from a JSON string
post_directive_instance = PostDirective.from_json(json)
# print the JSON string representation of the object
print PostDirective.to_json()

# convert the object into a dict
post_directive_dict = post_directive_instance.to_dict()
# create an instance of PostDirective from a dict
post_directive_form_dict = post_directive.from_dict(post_directive_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


