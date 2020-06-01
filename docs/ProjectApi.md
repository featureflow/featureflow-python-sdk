# featureflow.ProjectApi

All URIs are relative to *https://app.featureflow.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post5**](ProjectApi.md#create_using_post5) | **POST** /api/v2/projects | Create a new project
[**delete_using_delete5**](ProjectApi.md#delete_using_delete5) | **DELETE** /api/v2/projects/{key} | Delete a project
[**get_using_get5**](ProjectApi.md#get_using_get5) | **GET** /api/v2/projects/{key} | Get a project.
[**list_using_get5**](ProjectApi.md#list_using_get5) | **GET** /api/v2/projects | Get all projects
[**update_using_put5**](ProjectApi.md#update_using_put5) | **PUT** /api/v2/projects | Update a project

# **create_using_post5**
> Project create_using_post5(body)

Create a new project

Create a new project with the given friendly name and unique key.

### Example
```python
from __future__ import print_function
import time
import featureflow
from featureflow.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = featureflow.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = featureflow.ProjectApi(featureflow.ApiClient(configuration))
body = featureflow.ProjectUpdate() # ProjectUpdate | project

try:
    # Create a new project
    api_response = api_instance.create_using_post5(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_using_post5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectUpdate**](ProjectUpdate.md)| project | 

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete5**
> object delete_using_delete5(key)

Delete a project

Delete a project with the given key. Warning! All environments, features and history will be deleted.

### Example
```python
from __future__ import print_function
import time
import featureflow
from featureflow.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = featureflow.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = featureflow.ProjectApi(featureflow.ApiClient(configuration))
key = 'key_example' # str | key

try:
    # Delete a project
    api_response = api_instance.delete_using_delete5(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_using_delete5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| key | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get5**
> Project get_using_get5(key)

Get a project.

Returns a detail representation of a single project for the given key or id

### Example
```python
from __future__ import print_function
import time
import featureflow
from featureflow.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = featureflow.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = featureflow.ProjectApi(featureflow.ApiClient(configuration))
key = 'key_example' # str | key

try:
    # Get a project.
    api_response = api_instance.get_using_get5(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_using_get5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| key | 

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_using_get5**
> Projects list_using_get5()

Get all projects

Returns a summary list of all projects within the organisation

### Example
```python
from __future__ import print_function
import time
import featureflow
from featureflow.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = featureflow.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = featureflow.ProjectApi(featureflow.ApiClient(configuration))

try:
    # Get all projects
    api_response = api_instance.list_using_get5()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_using_get5: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Projects**](Projects.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put5**
> Project update_using_put5(body)

Update a project

Update a project with the given key.

### Example
```python
from __future__ import print_function
import time
import featureflow
from featureflow.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = featureflow.ProjectApi()
body = featureflow.ProjectUpdate() # ProjectUpdate | project

try:
    # Update a project
    api_response = api_instance.update_using_put5(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_using_put5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectUpdate**](ProjectUpdate.md)| project | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

