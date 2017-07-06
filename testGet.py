#coding=utf-8
import checkapi_get

url="http://127.0.0.1"
data1=checkapi_get.data()
data1=checkapi_get.convert_data(data1)
checkapi_get.check_api_get(url, data1)
