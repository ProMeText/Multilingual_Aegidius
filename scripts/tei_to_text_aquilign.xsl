<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math" exclude-result-prefixes="xs math"
    version="3.0">

    <xsl:output method="text"/>

    <xsl:template match="/">
        <xsl:for-each select="descendant::tei:TEI[@type = 'corpus']">
            <xsl:for-each select="tei:TEI[@xml:id = 'rome_1556']">
                <xsl:for-each select="descendant::tei:div[@type = 'livre']">
                    <xsl:variable name="ident_livre" select="@n"/>
                    <xsl:for-each select="tei:div[@type = 'partie']">
                        <xsl:variable name="ident_partie" select="@n"/>
                        <xsl:for-each select="tei:div[@type = 'chapitre']">
                            <xsl:variable name="ident_chapitre" select="@n"/>
                            <xsl:for-each
                                select="//tei:TEI[@type = 'corpus']/tei:TEI/descendant::tei:div[@type = 'livre'][@n = $ident_livre]/tei:div[@type = 'partie'][@n = $ident_partie]/tei:div[@type = 'chapitre'][@n = $ident_chapitre]">
                                <xsl:variable name="ident" select="ancestor::tei:TEI[1]/@xml:id"/>
                                <xsl:variable name="lang" select="ancestor::tei:TEI[2]/@xml:lang"/>
                                <xsl:result-document
                                    href="../data/aegidius/txt/multilingual/livre_{$ident_livre}/partie_{$ident_partie}/chapitre_{$ident_chapitre}/{$lang}/{$ident}.txt">
                                    <xsl:apply-templates/>
                                </xsl:result-document>
                            </xsl:for-each>
                        </xsl:for-each>
                    </xsl:for-each>
                </xsl:for-each>
            </xsl:for-each>
        </xsl:for-each>
    </xsl:template>


    <xsl:template match="tei:lb[@break = 'yes']">
        <xsl:text> </xsl:text>
    </xsl:template>



</xsl:stylesheet>
