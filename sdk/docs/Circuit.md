# Circuit

A class that represents a flow of states (circuits) that constitutes the control flow logic of an agent or pipeline.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** |  | [optional] 
**current** | **str** |  | [optional] 
**nodes** | [**Dict[str, Nodes]**](Nodes.md) |  | [optional] 

## Example

```python
from finbourne_candela.models.circuit import Circuit

# TODO update the JSON string below
json = "{}"
# create an instance of Circuit from a JSON string
circuit_instance = Circuit.from_json(json)
# print the JSON string representation of the object
print Circuit.to_json()

# convert the object into a dict
circuit_dict = circuit_instance.to_dict()
# create an instance of Circuit from a dict
circuit_form_dict = circuit.from_dict(circuit_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


