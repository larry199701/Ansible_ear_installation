import java.lang.System as javasys
import time
import sys
import re

lineSeparator = javasys.getProperty('line.separator')
strAppPath = "/home/wasadmin/larrytest/"
strAppName = "Weblink2_EAR"
strAppEdition1 = ""
strEditionDesc = time.strftime("%Y%m%d")
clusterName = "wasAppCluster02"
valEndpoint = "10.100.2.101:2016"
valJNDI = "eis/NGCatalog"

print "================================================================="
print sys.argv[0]
print "================================================================="

#---------------------------------------------------------------------------
# Install App
#---------------------------------------------------------------------------

AdminApp.install('C:/fakepath/Weblink2_EAR_beta_2.11_2.11.0.5.ear', '[ -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb -appname Weblink20_47981_EAR -edition beta_2.11_2.11.0.5 -edition.desc 2020.12.02 -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn -noprocessEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -noallowDispatchRemoteInclude -noallowServiceRemoteInclude -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule -clientMode isolated -novalidateSchema -MapModulesToServers [[ "Weblink 2.0 RPC - 47981" Weblink2.war,WEB-INF/web.xml WebSphere:cell=qa-dmgr01Cell01,cluster=wasAppCluster06+WebSphere:cell=qa-dmgr01Cell01,node=qa-web02.gpi.com-node,server=ihsWebServer02+WebSphere:cell=qa-dmgr01Cell01,node=qa-web01.gpi.com-node,server=ihsWebServer01 ]]]' ) 




AdminApp.install('strAppPath + strAppName + '_' + sys.argv[0] + '.ear', '[ \
    -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb \
    -appname ' + strAppName + ' -edition ' + sys.argv[0] + strAppEdition1 + ' -edition.desc ' + strEditionDesc + ' \
    -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn \
    -noprocessEmbeddedConfig \
    -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 \
    -noallowDispatchRemoteInclude -noallowServiceRemoteInclude \
    -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule \
    -clientMode isolated -novalidateSchema \
    -MapModulesToServers [[ "Weblink 2.0 RPC" Weblink2.war,WEB-INF/web.xml WebSphere:cell=qa-dmgr01Cell01,cluster=' + clusterName + ' ] \
           WebSphere:cell=qa-dmgr01Cell01,node=qa-web02.gpi.com-node,server=ihsWebServer02+WebSphere:cell=qa-dmgr01Cell01,node=qa-web01.gpi.com-node,server=ihsWebServer01 ]]]' ) 










AdminApp.install(strAppPath + strAppName + '_' + sys.argv[0] + '.ear',  '[ \
   -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb \
    -appname ' + strAppName + ' -edition ' + sys.argv[0] + strAppEdition1 + ' -edition.desc ' + strEditionDesc + ' \
    -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn \
    -noprocessEmbeddedConfig \
    -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 \
    -noallowDispatchRemoteInclude -noallowServiceRemoteInclude \
    -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule \
    -clientMode isolated -novalidateSchema \
    -MapModulesToServers [[ PAOServiceProject PAOServiceProjectWAS85.jar,META-INF/ejb-jar.xml WebSphere:cell=qa-dmgr01Cell01,cluster=' + clusterName + ' ] \
        [ PAOServiceProjectWAS85_HTTPRouter PAOServiceProjectWAS85_HTTPRouter.war,WEB-INF/web.xml \
            WebSphere:cell=qa-dmgr01Cell01,cluster=' + clusterName + '+WebSphere:cell=qa-dmgr01Cell01,node=qa-web02.gpi.com-node,server=ihsWebServer02+WebSphere:cell=qa-dmgr01Cell01,node=qa-web01.gpi.com-node,server=ihsWebServer01 ] \
        [ "NextGen Catalog Adapter" NextGenAdapter.rar,META-INF/ra.xml WebSphere:cell=qa-dmgr01Cell01,cluster=' + clusterName + ' ]]]' )

AdminConfig.save()

'''
#---------------------------------------------------------------------------
# print Cell Name
#---------------------------------------------------------------------------
#print AdminControl.getCell()
cells = AdminConfig.list('Cell').split(lineSeparator)
cellName = AdminConfig.showAttribute(cells[0], 'name')

#---------------------------------------------------------------------------
# print Cluster Name: wasAppCluster02
#---------------------------------------------------------------------------
clusterIds = AdminConfig.list('ServerCluster').split(lineSeparator)

for clusterId in clusterIds:
    cn = AdminConfig.showAttribute(clusterId, 'name')

    if (cn == clusterName):
#        print "debug-------- Cluster Name: "+cn

#---------------------------------------------------------------------------
# print Apps Names in wasAppCluster02
#---------------------------------------------------------------------------
        appNames = AdminApp.list('WebSphere:cell=' + cellName + ',cluster=' + cn).split(lineSeparator)
        for appName in appNames:
            if (appName == strAppName + "-edition" + sys.argv[0] + strAppEdition1):
                print "debug-------- App Name: "+appName
                appDeployment = AdminConfig.getid("/Deployment:"+appName+"/")
                if (len(appDeployment) == 0):
                    print "debug-------- No deployment "+appName
                    javasys.exit()

                depObjects = AdminConfig.showAttribute(appDeployment, 'deployedObject')
                modules = AdminConfig.showAttribute(depObjects, 'modules')
                arrayModules = modules[1:len(modules)-1].split(" ")
                for module in arrayModules:
                    if (module.find('ConnectorModuleDeployment') != -1):

#---------------------------------------------------------------------------
# Modifying Endpoint
#---------------------------------------------------------------------------
                        resAdapter = AdminConfig.showAttribute(module, 'resourceAdapter')
                        propSet = AdminConfig.showAttribute(resAdapter, 'propertySet')
                        props = AdminConfig.showAttribute(propSet, 'resourceProperties')
                        arrayProps = props[1:len(props)-1].split(" ")
                        for prop in arrayProps:
                            if (prop.find('endpoint') != -1):
                                AdminConfig.modify(prop, [['value', valEndpoint]])
                                print AdminConfig.showAttribute(prop, 'value')

#---------------------------------------------------------------------------
# Modifying JNDI
#---------------------------------------------------------------------------
                        j2cFactory = AdminConfig.list('J2CConnectionFactory', module)
                        print AdminConfig.showAttribute(j2cFactory, 'jndiName')
                        AdminConfig.modify(j2cFactory, [['jndiName', valJNDI]])
                        print AdminConfig.showAttribute(j2cFactory, 'jndiName')


#---------------------------------------------------------------------------
# Modifying PAO Resource references
#---------------------------------------------------------------------------
                AdminApp.edit(appName, \
                    '[ -MapResRefToEJB [ \
                        [ PAOServiceProject PartHttpImpl  PAOServiceProjectWAS85.jar,META-INF/ejb-jar.xml wm/WAS_paoServicesWorkManager com.ibm.websphere.asynchbeans.WorkManager wm/pao "" "" "" ] \
                        [ PAOServiceProject OrderHttpImpl PAOServiceProjectWAS85.jar,META-INF/ejb-jar.xml wm/WAS_paoServicesWorkManager com.ibm.websphere.asynchbeans.WorkManager wm/pao "" "" "" ] \
                        [ PAOServiceProject OrderHttpImpl PAOServiceProjectWAS85.jar,META-INF/ejb-jar.xml jms/WeblinkPartOrderCF javax.jms.ConnectionFactory jms/WeblinkPartOrderCF "" "" "" ] \
                        [ PAOServiceProject PartHttpImpl  PAOServiceProjectWAS85.jar,META-INF/ejb-jar.xml jdbc/catalogUS javax.sql.DataSource jdbc/catalogDb DefaultPrincipalMapping catalogDb_Alias "" ] \
                        [ PAOServiceProject PartHttpImpl  PAOServiceProjectWAS85.jar,META-INF/ejb-jar.xml jdbc/acesDB javax.sql.DataSource jdbc/acesDb DefaultPrincipalMapping acesDb_Alias "" ] \
                        [ PAOServiceProject OrderHttpImpl PAOServiceProjectWAS85.jar,META-INF/ejb-jar.xml jdbc/acesDB javax.sql.DataSource jdbc/acesDb DefaultPrincipalMapping acesDb_Alias "" ] \
                        [ PAOServiceProject PartHttpImpl  PAOServiceProjectWAS85.jar,META-INF/ejb-jar.xml jdbc/nacDB javax.sql.DataSource jdbc/nacDb DefaultPrincipalMapping nacDb_Alias "" ] \
                        [ PAOServiceProject OrderHttpImpl PAOServiceProjectWAS85.jar,META-INF/ejb-jar.xml jdbc/catalogUS javax.sql.DataSource jdbc/catalogDb DefaultPrincipalMapping catalogDb_Alias "" ] \
                    ]]' )

                AdminApp.edit(appName, \
                    '[ -MapResEnvRefToRes [ \
                        [ PAOServiceProject PartHttpImpl  PAOServiceProjectWAS85.jar,META-INF/ejb-jar.xml rep/WAS_PAOResourceReference com.gpi.websphere.util.config.Configuration rep/pao ] \
                        [ PAOServiceProject OrderHttpImpl PAOServiceProjectWAS85.jar,META-INF/ejb-jar.xml rep/WAS_PAOResourceReference com.gpi.websphere.util.config.Configuration rep/pao ] \
                    ]]' )


#---------------------------------------------------------------------------
# Modifying Service client policy sets and bindings
#---------------------------------------------------------------------------

                arrExpandResources = [["{http://independents.services.advancestores.com/}IndependentsService", "HTTPNoChunked"], \
                    ["{http://inventory.service.cwsadapter.ecomm.advancestores.com/}CQProInventoryService", "HTTPS_10SecondTimeout"], \
                    ["{http://inventory.service.cwsadapter.ecomm.advancestores.com/}InventoryService", "HTTPNoChunked"], \
                    ["{http://orderfulfillment.service.cwsadapter.ecomm.advancestores.com/}CQProOrderFulfillmentService", "HTTPS_30SecondTimeout"], \
                    ["{http://orderreview.service.cwsadapter.ecomm.advancestores.com/}CQProOrderReviewService", "HTTPS_10SecondTimeout"], \
                    ["{http://ws.carquest.com/2006/services/vehicle}VehicleService", "HTTPBasicAuth"], \
                    ["{http://www.advancestores.com/parts/xref}PartsCrossReferenceService", "HTTP_10SecondTimeout"]] \

                for er in arrExpandResources:
                    atachs = AdminTask.getPolicySetAttachments('[-applicationName ' + appName + ' -attachmentType client -expandResources ' + er[0] + ' ]')
                    match = re.search(r'attachmentId (\d+)', atachs)
                    if match:
                        atachId = match.group(1)
                        AdminTask.deletePolicySetAttachment('[-applicationName ' + appName + ' -attachmentType client -attachmentId ' + atachId + ']')
                        print "debug-------- atachId ----"+ atachId +"============="

                    newAtachId = AdminTask.createPolicySetAttachment('[-applicationName ' + appName + ' -attachmentType client -policySet ' + er[1] + ' -resources [WebService:/PAOServiceProjectWAS85.jar:' + er[0] + ' ]]')
                    print "debug-------- newAtachId ----"+ newAtachId +"============="

                    if (er[0] == "{http://independents.services.advancestores.com/}IndependentsService"):
                        AdminTask.setBinding('[-bindingName IndependentsServiceBinding -attachmentType client -bindingLocation [ [application ' + appName + '] [attachmentId ' + newAtachId + '] ]]')

                    if (er[0] == "{http://ws.carquest.com/2006/services/vehicle}VehicleService"):
                        AdminTask.setBinding('[-bindingScope domain -bindingName "Internal Vehicle Client" -attachmentType client -bindingLocation [ [application ' + appName + '] [attachmentId ' + newAtachId + '] ]]')
AdminConfig.save()

'''


'''
AdminTask.deactivateEdition('[-appName Weblink2Utility -edition ' + sys.argv[0] + ' ]') 
AdminTask.activateEdition('[-appName Weblink2Utility -edition ' + sys.argv[0] + ' ]') 

'''











