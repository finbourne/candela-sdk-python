# Nodes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**node_type** | **str** |  | [optional] 
**as_block** | **bool** |  | [default to False]
**child_id** | **str** |  | [optional] 
**template** | **str** |  | 
**context** | **str** |  | 
**inserts** | **Dict[str, str]** |  | 
**spec** | [**Spec**](Spec.md) |  | 
**instruction** | **str** |  | [optional] 
**options** | **List[str]** |  | 
**intent_id** | **str** |  | 
**tool_obj** | [**ToolObj**](ToolObj.md) |  | 
**case_spec** | **Dict[str, str]** |  | 
**case_objs** | [**Dict[str, NoOp]**](NoOp.md) |  | [optional] 
**label** | **str** |  | 

## Example

```python
from finbourne_candela.models.nodes import Nodes

# TODO update the JSON string below
json = "{}"
# create an instance of Nodes from a JSON string
nodes_instance = Nodes.from_json(json)
# print the JSON string representation of the object
print Nodes.to_json()

# convert the object into a dict
nodes_dict = nodes_instance.to_dict()
# create an instance of Nodes from a dict
nodes_form_dict = nodes.from_dict(nodes_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


