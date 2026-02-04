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
        <ul>
            <xsl:for-each select="menu/bebida">
                <li><xsl:value-of select="nombre"></xsl:value-of></li>
            </xsl:for-each>
        </ul>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>