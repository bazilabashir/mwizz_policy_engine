from db_connector import DBConnector
from process_service import ProcessService
from es_connector import ESConnector

db_obj = DBConnector()
service = ProcessService()
# es = ESConnector()

stacktrace = """Starting the development server...
Error: error:0308010C:digital envelope routines::unsupported
at Storage.finished (9)
throw err;
Error: error:0308010C:digital envelope routines::unsupported
code: 'ERR_OSSL_EVP_UNSUPPORTED'
Hello World, this is a file
Exception in thread "main" java.lang.NullPointerException: 	Cannot invoke "DummyClass.convert(String)" because "dummy" 	is null
at DummyClass.main(DummyClass.java:14)
"""

def main():
    print("Processing Started !!!")
    policy = db_obj.db_find("policy_db")
    logs = db_obj.db_find("bug_info","status")
    # service.process(logs[4],policy[1:])
    for log in logs:
        data = service.process(log,policy)
        print(data)

    # data = {
    #     'productName': 'Intune', 
    #     'logFileName': 'apache.log', 
    #     'severity': 'critcal', 
    #     'stacktrace': stacktrace, 
    #     'status': 'init'
    # }


    # policy_data ={
    #     "policyID":"abc123",
    #     "productName":"Intune",
    #     "policySigniture": "^Error:.*",
    #     "workaround": "Restart System",
    #     "severity":"Critcal"
    # }

    # policy_data ={
    #     "policyID":"xyz123",
    #     "productName":"Intune",
    #     "policySigniture": "NullPointerException:.*",
    #     "workaround": "Pointer issue workaround",
    #     "severity":"Critical"
    # }

    # db_obj.db_insert("bug_info",data)
    # db_obj.db_insert("policy_db",policy_data)
    # db_obj.db_find("bug_info")
    # db_obj.db_find("policy_db")

if __name__=="__main__":
    main()
    # data = {
    #     'productName': 'Intune', 
    #     'logFileName': 'apache.log', 
    #     'severity': 'critcal', 
    #     'stacktrace': stacktrace, 
    #     'status': 'init'
    # }
    # db_obj.db_insert("bug_info",data)
    # db_obj.db_find("bug_info","init")
    # db_obj.db_delete_all("bug_info")
    # main()