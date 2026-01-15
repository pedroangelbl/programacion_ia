<?xml version="1.0" encoding="UTF-8"?>

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
                <xsl:sort select="precio" order="ascending"></xsl:sort>
                <tr>
                    <td><xsl:value-of select="nombre"/></td>
                    <td><xsl:value-of select="precio"/>$</td>
                </tr>
            </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>