import re

class ProcessService:
    def __init__(self):
        pass

    def process(self,logs,policyData):
        # filename =logs['logFileName']
        obj = {
        'filename': logs['logFileName'],
        'productName':"xyz",
        'error':[]
        }   
        policySigniture =[]
        policyDict ={}
        for policy in policyData:
            policySigniture.append(policy['policySigniture'])
            signiture = policy['policySigniture']
            workaround = policy['workaround']
            policyDict[signiture] = workaround
            # policyDict[workaround] = policy['workaround']
                # policy['policySigniture']: policy['workaround']
            
        lines = logs['stacktrace'].split("\n")
        for line in lines:
            index = 0
            print(index)
            index+=1
            for signiture  in policySigniture:
                regexPattern = re.compile('{}'.format(signiture))
                
                res = regexPattern.findall(line)
                if(len(res) >0):
                    flag = False
                    for error in obj['error']:
                        if error['policySignitue'] == signiture:
                            error['count']+=1
                            flag = True

                    if (flag == False):    
                        obj['error'].append({
                            'errorMessage': line,
                            'policySignitue':signiture,
                            'workaround':policyDict[signiture],
                            'count': len(res)
                        })
        print(obj)
        return obj

