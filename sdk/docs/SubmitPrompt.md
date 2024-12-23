# SubmitPrompt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** |  | 
**session_id** | **str** |  | 

## Example

```python
from finbourne_candela.models.submit_prompt import SubmitPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitPrompt from a JSON string
submit_prompt_instance = SubmitPrompt.from_json(json)
# print the JSON string representation of the object
print SubmitPrompt.to_json()

# convert the object into a dict
submit_prompt_dict = submit_prompt_instance.to_dict()
# create an instance of SubmitPrompt from a dict
submit_prompt_form_dict = submit_prompt.from_dict(submit_prompt_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


