<?xml version="1.0" encoding="UTF-8"?>

<!-- 
Transformación 5 – Uso de plantillas XSLT
Objetivo
Repetir la transformación del listado simple, pero utilizando plantillas XSLT en lugar de bucles directos.

Requisitos
  Archivo: bebidas_5.xsl
  Debe incluir:
    una plantilla con match="/"
    una plantilla con match="bebida"
  Usar xsl:apply-templates
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
            <xsl:apply-templates/>
        </table>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="menu/bebida">
    <tr>
        <td><xsl:value-of select="nombre"/></td>
        <td><xsl:value-of select="precio"/>$</td>
    </tr>
  </xsl:template>

</xsl:stylesheet>