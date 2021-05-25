<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" version="1.0" encoding="UTF-8" omit-xml-declaration="no" indent="yes"/>
<xsl:strip-space elements="*"/>
<xsl:param name="VehicleHttpPort">http://ws.carquest.com:6510/2006/services/VehicleHttpPort</xsl:param>
<xsl:param name="InventoryServicePort">http://ws.gpi.com:80/was/InventoryServiceWeb/InventoryServiceService</xsl:param>
<xsl:param name="GpiPaoServiceSOAP">http://exapps.gpi.com/link/WebService/BrandedGpi/GpiPaoService.php</xsl:param>
<xsl:param name="TransactionLogServicePort">http://ws.gpi.com:80/TransactionLogServiceWeb/TransactionLogServiceService</xsl:param>
<xsl:param name="InventoryPort">https://commercial.advanceautoparts.com/b2bservices-WBL/CWSAdapter/Inventory</xsl:param>
<xsl:param name="AccountStatusPort">https://commercial.advanceautoparts.com/b2bservices-WBL/CWSAdapter/AccountStatus</xsl:param>
<xsl:param name="OrderFulfillmentPort">https://commercial.advanceautoparts.com/b2bservices-WBL/CWSAdapter/OrderFulfillment</xsl:param>
<xsl:param name="OrderQuotePort">https://commercial.advanceautoparts.com/b2bservices-WBL/CWSAdapter/OrderQuote</xsl:param>
<xsl:param name="IndependentsInterface">https://commercial.advanceautoparts.com/independents/IndependentsService</xsl:param>
<xsl:param name="PartsCrossReferenceSoap11">http://localhost:8380/CrossReferenceIntegration/partsXrefService</xsl:param>
<xsl:param name="CQProInventoryPort">https://localhost:15000/B2BAdapter/ws</xsl:param>
<xsl:param name="CQProOrderFulfillmentPort">https://localhost:15004/FulfillmentService/ws</xsl:param>
<xsl:param name="CQProOrderReviewPort">https://localhost:15004/FulfillmentService/ws</xsl:param>

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

