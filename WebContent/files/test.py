from org.json.simple import *

a='{"a1":"b1","a2":"b2","a3":"b3","a4":"b4"}'
o={"a1":"b1","a2":"b2","a3":"b3","a4":"b4"}
b = JSONObject()
jsonObj = JSONObject()
jsonObj = JSONValue.parse(a)
s = JSONValue.toJSONString(o)
print s
print jsonObj.get("a1")
b.put("c1","d1")
print b

