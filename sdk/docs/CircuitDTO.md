# CircuitDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** |  | 
**nodes** | [**Dict[str, Nodes]**](Nodes.md) |  | 

## Example

```python
from finbourne_candela.models.circuit_dto import CircuitDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CircuitDTO from a JSON string
circuit_dto_instance = CircuitDTO.from_json(json)
# print the JSON string representation of the object
print CircuitDTO.to_json()

# convert the object into a dict
circuit_dto_dict = circuit_dto_instance.to_dict()
# create an instance of CircuitDTO from a dict
circuit_dto_form_dict = circuit_dto.from_dict(circuit_dto_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


