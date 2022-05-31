from azure.identity import DefaultAzureCredential
import azure.analytics.loadtestexample as loadtest

client=loadtest.LoadTestClient(credential=DefaultAzureCredential(), endpoint="https://1bc65f40-8b4c-4cbe-bc38-263adde93b1c.eus2.cnt-canary.loadtesting.azure.com")
print(client.test.list_load_test_search())