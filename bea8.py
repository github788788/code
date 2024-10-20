from beasy.beasy import Bea
API_KEY = '3BC954F2-774A-45BB-A5C3-05F5A0482C38'
client = Bea(API_KEY)

#data = client.getDatasetList()

#client.[table_name].getParameterValues(parameter)

#data = client.'T10101'.getParameterValues(parameter)

#data = client.Regional.getData(TableName='T10101', LineCode='3', GeoFIPS='DE', Year='2014')
data = client.Regional.getData(TableName='T10101')


"""
<Request>
<RequestParam ParameterValue="Your- 36Char act er-K ey" ParameterName="USERID"/>
<RequestParam ParameterValue="REGIONAL" ParameterName="DATASETNAME"/>
<RequestParam ParameterValue="GETDATA" ParameterName="METHOD"/>
<RequestParam ParameterValue="DE" ParameterName="GEOFIPS"/>
<RequestParam ParameterValue="CAINC1" ParameterName="TABLENAME"/>
<RequestParam ParameterValue="3" ParameterName="LINECODE"/>
<RequestParam ParameterValue="2014" ParameterName="YEAR"/>
<RequestPara
"""

#data = client.Regional.getParameterList()
#data = client.Regional.getParameterValues('NIPA')




#data = client.getData(dataset='NIPA', table='T10101', frequency='A', year='2020')


print(data)