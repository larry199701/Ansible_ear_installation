import java.lang.System as javasys
import time
import sys

lineSeparator = javasys.getProperty('line.separator')
strAppPath = "/home/wasadmin/larrytest/"
strAppName = "PAOServiceWAS85EAR"
strAppEdition1 = ""
strEditionDesc = time.strftime("%Y%m%d")
clusterName = "wasAppCluster02"
valEndpoint = "10.100.2.101:2016"
valJNDI = "eis/NGCatalog"

print "================================================================="
print sys.argv[0]
print "================================================================="

#---------------------------------------------------------------------------
# Uninstall appNames
#---------------------------------------------------------------------------

cells = AdminConfig.list('Cell').split(lineSeparator)
cellName = AdminConfig.showAttribute(cells[0], 'name')
print ""
print time.strftime("%Y%m%d_%H:%M:%S")+' cellName: '+cellName

clusterIds = AdminConfig.list('ServerCluster').split(lineSeparator)
for clusterId in clusterIds:
    clusterName = AdminConfig.showAttribute(clusterId, 'name')
    appNames = AdminApp.list('WebSphere:cell=' + cellName + ',cluster=' + clusterName).split(lineSeparator)

    for appName in appNames:
        if appName == (strAppName + '-edition' + sys.argv[0] ):
            AdminApp.uninstall(appName)
            AdminConfig.save()
            print time.strftime("%Y%m%d_%H:%M:%S")+' '+appName + " has been uninstalled!"



























'''
# Uninstall App
AdminApp.uninstall('Weblink2Utility-edition1.5.2.4')
AdminApp.uninstall('Weblink2Utility-edition1.6.0.10')
AdminApp.uninstall('Weblink2Utility-edition1.6.0.5')
AdminApp.uninstall('Weblink2Utility-edition1.6.0.6')
AdminApp.uninstall('Weblink2Utility-edition1.6.0.7')
AdminApp.uninstall('Weblink2Utility-edition1.6.0.8')
AdminApp.uninstall('Weblink2Utility-edition1.6.0.9')
AdminConfig.save()
'''






'''
#--------------------------------------------------------------------------- 
# print Cell Name
#---------------------------------------------------------------------------
#print AdminControl.getCell()
cells = AdminConfig.list('Cell').split(lineSeparator)
cellName = AdminConfig.showAttribute(cells[0], 'name')
print "cellName _________"
print cellName

#---------------------------------------------------------------------------
# print Cluster Names
#---------------------------------------------------------------------------
clusterIds = AdminConfig.list('ServerCluster').split(lineSeparator)

for clusterId in clusterIds:
    clusterName = AdminConfig.showAttribute(clusterId, 'name')
    print clusterName
    print 
    appNames = AdminApp.list('WebSphere:cell=' + cellName + ',cluster=' + clusterName).split(lineSeparator)

    for appName in appNames:
        print ""
        print "------------"
        print appName
        deployment = AdminConfig.getid("/Deployment:"+appName+"/")
        if (len(deployment) == 0):
            print "debug--------: No deployment "+appName
            sys.exit()

        modules = AdminApp.listModules(appName).split(lineSeparator)

        for module in modules:
            print module

#            moduleName = AdminConfig.showAttribute(module, 'uri')





        print deployment
        depObjects = AdminConfig.showAttribute(deployment, 'deployedObject')
        print depObjects



#        modules = AdminConfig.showAttribute(depObjects, 'modules').split(lineSeparator)
#        modules = AdminConfig.showAttribute(depObjectRef, 'modules')

#        print modules



        opt = '-cluster ' + clusterName
        moduleIds = AdminApp.listModules(appName, opt).split(lineSeparator)
        print moduleIds


            print moduleName
#             print moduleId
#print AdminApp.listModules('ivtApp').split(lineSeparator)
'''











