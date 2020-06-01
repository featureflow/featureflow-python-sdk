# featureflow.EnvironmentApi

All URIs are relative to *https://app.featureflow.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post3**](EnvironmentApi.md#create_using_post3) | **POST** /api/v2/environments | Create a new environment
[**delete_using_delete3**](EnvironmentApi.md#delete_using_delete3) | **DELETE** /api/v2/environments/{id} | Delete a environment
[**get_using_get3**](EnvironmentApi.md#get_using_get3) | **GET** /api/v2/environments/{id} | Get an environment.
[**list_using_get3**](EnvironmentApi.md#list_using_get3) | **GET** /api/v2/environments | Get all environments
[**update_using_put3**](EnvironmentApi.md#update_using_put3) | **PUT** /api/v2/environments | Update an environment

# **create_using_post3**
> Environment create_using_post3(body)

Create a new environment

Create a new environment with the given friendly name and unique key.

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
api_instance = featureflow.EnvironmentApi(featureflow.ApiClient(configuration))
body = featureflow.EnvironmentUpdate() # EnvironmentUpdate | environment

try:
    # Create a new environment
    api_response = api_instance.create_using_post3(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->create_using_post3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnvironmentUpdate**](EnvironmentUpdate.md)| environment | 

### Return type

[**Environment**](Environment.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete3**
> object delete_using_delete3(id)

Delete a environment

Delete a environment with the given id. Projects must have at least one environment.

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
api_instance = featureflow.EnvironmentApi(featureflow.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete a environment
    api_response = api_instance.delete_using_delete3(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->delete_using_delete3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get3**
> Environment get_using_get3(id)

Get an environment.

Returns a detail representation of a single environment for the given id

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
api_instance = featureflow.EnvironmentApi(featureflow.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Get an environment.
    api_response = api_instance.get_using_get3(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->get_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**Environment**](Environment.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_using_get3**
> Environments list_using_get3()

Get all environments

Returns a summary list of all environments within the organisation

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
api_instance = featureflow.EnvironmentApi(featureflow.ApiClient(configuration))

try:
    # Get all environments
    api_response = api_instance.list_using_get3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->list_using_get3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Environments**](Environments.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put3**
> Environment update_using_put3(body)

Update an environment

Update an environment.

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
api_instance = featureflow.EnvironmentApi(featureflow.ApiClient(configuration))
body = featureflow.EnvironmentUpdate() # EnvironmentUpdate | environment

try:
    # Update an environment
    api_response = api_instance.update_using_put3(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->update_using_put3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnvironmentUpdate**](EnvironmentUpdate.md)| environment | 

### Return type

[**Environment**](Environment.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

