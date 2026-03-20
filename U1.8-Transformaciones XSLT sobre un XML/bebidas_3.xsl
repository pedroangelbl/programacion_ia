<?xml version="1.0" encoding="UTF-8"?>

<!-- 
Transformación 3 – Filtrado por tipo
Objetivo
Crear una hoja XSL que muestre solo las bebidas frías.

Requisitos
  Archivo: bebidas_3.xsl
  Mostrar nombre y precio
  Usar una condición (xsl:if) o un filtro XPath
-->

<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html lang="es">
      <head>
        <meta charset="UTF-8" />
        <title>Bebidas</title>
      </head>
      <body>
        <h1>Bebidas</h1>
        <table>
            <tr>
                <td>Nombre</td>
                <td>Precio</td>
            </tr>
            <xsl:for-each select="menu/bebida">
                <xsl:if test="precio &lt; 2">
                    <tr>
                        <td><xsl:value-of select="nombre"/></td>
                        <td><xsl:value-of select="precio"/>$</td>
                    </tr>
                </xsl:if>
            </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>