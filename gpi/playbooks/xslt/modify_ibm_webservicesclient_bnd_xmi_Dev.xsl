<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" version="1.0" encoding="UTF-8" omit-xml-declaration="no" indent="yes"/>
<xsl:strip-space elements="*"/>

<xsl:param name="VehicleHttpPort">http://dpdev01i.gpi.com:6510/2006/services/VehicleHttpPort</xsl:param>
<xsl:param name="InventoryServicePort">http://dev-web01.gpi.com:80/InventoryServiceWeb/InventoryServiceService</xsl:param>
<xsl:param name="GpiPaoServiceSOAP">http://qa-exapps02.gpi.com/link/WebService/BrandedGpi/GpiPaoService.php</xsl:param>
<xsl:param name="TransactionLogServicePort">http://dev-web01.gpi.com:80/TransactionLogServiceWeb/TransactionLogServiceService</xsl:param>
<xsl:param name="InventoryPort">http://cwsappqa01.corp.advancestores.com:9680/CWSAdapter/Inventory</xsl:param>
<xsl:param name="AccountStatusPort">http://cwsappqa01.corp.advancestores.com:9680/CWSAdapter/AccountStatus</xsl:param>
<xsl:param name="OrderFulfillmentPort">http://cwsappqa01.corp.advancestores.com:9680/CWSAdapter/OrderFulfillment</xsl:param>
<xsl:param name="OrderQuotePort">http://cwsappqa01.corp.advancestores.com:9680/CWSAdapter/OrderQuote</xsl:param>
<xsl:param name="IndependentsInterface">http://cwsappqa01.corp.advancestores.com:8980/independents/IndependentsService</xsl:param>
<xsl:param name="PartsCrossReferenceSoap11">http://gcsappqa01.corp.advancestores.com:8380/CrossReferenceIntegration/partsXrefService</xsl:param>
<xsl:param name="CQProInventoryPort">https://cwsappqa01.corp.advancestores.com:15000/B2BAdapter/ws</xsl:param>
<xsl:param name="CQProOrderFulfillmentPort">https://cwsappqa01.corp.advancestores.com:15004/FulfillmentService/ws</xsl:param>
<xsl:param name="CQProOrderReviewPort">https://cwsappqa01.corp.advancestores.com:15004/FulfillmentService/ws</xsl:param>

  <xsl:template match="node()|@*">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='VehicleHttpPort']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$VehicleHttpPort"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='InventoryServicePort']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$InventoryServicePort"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='GpiPaoServiceSOAP']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$GpiPaoServiceSOAP"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='TransactionLogServicePort']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$TransactionLogServicePort"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='InventoryPort']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$InventoryPort"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='AccountStatusPort']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$AccountStatusPort"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='OrderFulfillmentPort']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$OrderFulfillmentPort"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='OrderQuotePort']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$OrderQuotePort"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='IndependentsInterface']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$IndependentsInterface"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='PartsCrossReferenceSoap11']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$PartsCrossReferenceSoap11"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='CQProInventoryPort']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$CQProInventoryPort"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='CQProOrderFulfillmentPort']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$CQProOrderFulfillmentPort"/></xsl:attribute>
  </xsl:template>

  <xsl:template match="*/componentScopedRefs/serviceRefs/portQnameBindings[@portQnameLocalNameLink='CQProOrderReviewPort']/@overriddenEndpointURI">
    <xsl:attribute name="overriddenEndpointURI"><xsl:value-of select="$CQProOrderReviewPort"/></xsl:attribute>
  </xsl:template>

</xsl:stylesheet>

<!--
-->

