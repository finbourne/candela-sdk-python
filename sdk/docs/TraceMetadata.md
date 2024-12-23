# TraceMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 
**trace_id** | **str** |  | 

## Example

```python
from finbourne_candela.models.trace_metadata import TraceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TraceMetadata from a JSON string
trace_metadata_instance = TraceMetadata.from_json(json)
# print the JSON string representation of the object
print TraceMetadata.to_json()

# convert the object into a dict
trace_metadata_dict = trace_metadata_instance.to_dict()
# create an instance of TraceMetadata from a dict
trace_metadata_form_dict = trace_metadata.from_dict(trace_metadata_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


