from azure.identity import DefaultAzureCredential
import azure.analytics.loadtestexample as loadtest
d = {}
with open("D:/Project/NGINX-10s.jmx","rb") as f:
    byte=f.read(1) 
    a=byte
    while byte:
        byte=f.read(1)
        a+=byte
print(type(a))   

d["NGINX-10s.jmx"]=a   
print(d)
# print(f)
f.close()
client=loadtest.LoadTestClient(credential=DefaultAzureCredential(), endpoint="https://1bc65f40-8b4c-4cbe-bc38-263adde93b1c.eus2.cnt-canary.loadtesting.azure.com")
print(client.test.upload_test_file("afb92a01-5860-4d31-ae39-ea9772801c4f","4c1a5970-aafe-49ed-b1cc-2073be28279c",{"D:/Project/NGINX-10s.jmx",a}))