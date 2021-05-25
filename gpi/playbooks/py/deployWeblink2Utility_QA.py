import java.lang.System as javasys
import time
import sys
import re

lineSeparator = javasys.getProperty('line.separator')
strAppPath = "/home/wasadmin/larrytest/"
strAppName = "Weblink2Utility"
strAppEdition1 = ""
strEditionDesc = time.strftime("%Y%m%d")
clusterName = "wasAppCluster01"

print "================================================================="
print sys.argv[0]
print "================================================================="

#---------------------------------------------------------------------------
# Install App 
#---------------------------------------------------------------------------

AdminApp.install(strAppPath + strAppName + '.' + sys.argv[0] + '.ear',  '[ \
    -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb \
    -appname Weblink2Utility -edition ' + sys.argv[0] + ' -edition.desc ' + strEditionDesc + ' \
    -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn \
    -noprocessEmbeddedConfig \
    -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 \
    -noallowDispatchRemoteInclude -noallowServiceRemoteInclude \
    -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule \
    -clientMode isolated -novalidateSchema \
    -MapModulesToServers [[ Weblink2UtilityEJB Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml WebSphere:cell=qa-dmgr01Cell01,cluster=' + clusterName + ' ]]]' )

AdminConfig.save()


'''

AdminApp.edit(strAppName + '-edition' + strAppEdition, '[ \
    -MapResEnvRefToRes [[ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml Weblink2Utilities com.gpi.websphere.util.config.Configuration rep/weblink2Utility \
    ][ Weblink2UtilityEJB AAPMIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml Weblink2Utilities com.gpi.websphere.util.config.Configuration rep/weblink2Utility ]]]' )


AdminApp.edit(strAppName + '-edition' + strAppEdition, '[ -MapResRefToEJB [ \
    [ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogDb javax.sql.DataSource jdbc/catalogDb DefaultPrincipalMapping catalogDb_Alias "" ] \
    [ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogCanada javax.sql.DataSource jdbc/catalogCanada DefaultPrincipalMapping catalogCanada_Alias "" ] \
    [ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogBWP javax.sql.DataSource jdbc/catalogBWP DefaultPrincipalMapping catalogBWP_Alias "" ] \
    [ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogCAP javax.sql.DataSource jdbc/catalogCAP DefaultPrincipalMapping catalogCAP_Alias "" ] \
    [ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogAWI javax.sql.DataSource jdbc/catalogAWI DefaultPrincipalMapping catalogAWI_Alias "" ] \
    [ Weblink2UtilityEJB AAPMIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogAAP javax.sql.DataSource jdbc/catalogAAP DefaultPrincipalMapping catalogAAP_Alias "" ]]]' )




print "----" + strAppEdition0 + "   " + AdminTask.getEditionState ('[-appName Weblink2Utility -edition ' + strAppEdition0 + ']') 
print "----" + strAppEdition + "   " + AdminTask.getEditionState ('[-appName Weblink2Utility -edition ' + strAppEdition + ']') 











AdminTask.rolloutEdition('[-appName Weblink2Utility \
    -edition ' + strAppEdition + ' \
    -params "{rolloutStrategy [grouped]}{resetStrategy [soft]}{groupSize 1}{drainageInterval 30}"]')





print ""
print time.strftime("%Y%m%d_%H:%M:%S")+' '+ strAppName + " has been installed!"

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------








AdminTask.deactivateEdition('[-appName Weblink2Utility -edition ' + strAppEdition + ' ]') 
AdminTask.activateEdition('[-appName Weblink2Utility -edition ' + strAppEdition0 + ' ]') 


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











