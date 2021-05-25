import java.lang.System as javasys
import time
import sys
import re

lineSeparator = javasys.getProperty('line.separator')
strAppPath = "/home/wasadmin/larrytest/"
strAppName = "Weblink2Utility"
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
    -MapModulesToServers [[ Weblink2UtilityEJB Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml WebSphere:cell=dev-dmgr01Cell01,cluster=' + clusterName + ' ]]]' )

AdminApp.edit(strAppName + '-edition' + sys.argv[0], '[ -MapResEnvRefToRes [ \
    [ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml Weblink2Utilities com.gpi.websphere.util.config.Configuration rep/weblink2Utility] \
    [ Weblink2UtilityEJB AAPMIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml Weblink2Utilities com.gpi.websphere.util.config.Configuration rep/weblink2Utility ]]]' )


AdminApp.edit(strAppName + '-edition' + sys.argv[0], '[ -MapResRefToEJB [ \
    [ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogDb javax.sql.DataSource jdbc/catalogDb DefaultPrincipalMapping catalogDb_Alias "" ] \
    [ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogCanada javax.sql.DataSource jdbc/catalogCanada DefaultPrincipalMapping catalogCanada_Alias "" ] \
    [ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogBWP javax.sql.DataSource jdbc/catalogBWP DefaultPrincipalMapping catalogBWP_Alias "" ] \
    [ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogCAP javax.sql.DataSource jdbc/catalogCAP DefaultPrincipalMapping catalogCAP_Alias "" ] \
    [ Weblink2UtilityEJB MIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogAWI javax.sql.DataSource jdbc/catalogAWI DefaultPrincipalMapping catalogAWI_Alias "" ] \
    [ Weblink2UtilityEJB AAPMIFJobBean Weblink2UtilityEJB.jar,META-INF/ejb-jar.xml jdbc/catalogAAP javax.sql.DataSource jdbc/catalogAAP DefaultPrincipalMapping catalogAAP_Alias "" ]]]' )

AdminConfig.save()





'''
AdminTask.rolloutEdition('[-appName Weblink2Utility \
    -edition ' + strAppEdition + ' \
    -params "{rolloutStrategy [grouped]}{resetStrategy [soft]}{groupSize 1}{drainageInterval 30}"]')

print time.strftime("%Y%m%d_%H:%M:%S")+' '+ strAppName + " has been installed!"

AdminTask.deactivateEdition('[-appName Weblink2Utility -edition ' + strAppEdition + ' ]') 
AdminTask.activateEdition('[-appName Weblink2Utility -edition ' + strAppEdition0 + ' ]') 

'''
