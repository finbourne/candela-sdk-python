# PostCircuit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**identifier** | **str** |  | 
**description** | **str** |  | [optional] 
**version_bump** | **str** |  | [optional] [default to 'patch']
**data** | [**CircuitDTO**](CircuitDTO.md) |  | 

## Example

```python
from finbourne_candela.models.post_circuit import PostCircuit

# TODO update the JSON string below
json = "{}"
# create an instance of PostCircuit from a JSON string
post_circuit_instance = PostCircuit.from_json(json)
# print the JSON string representation of the object
print PostCircuit.to_json()

# convert the object into a dict
post_circuit_dict = post_circuit_instance.to_dict()
# create an instance of PostCircuit from a dict
post_circuit_form_dict = post_circuit.from_dict(post_circuit_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


