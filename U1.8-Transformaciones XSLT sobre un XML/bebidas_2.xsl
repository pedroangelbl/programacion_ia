<?xml version="1.0" encoding="UTF-8"?>

<!-- 
Transformación 2 – Tabla completa
Objetivo
Crear una hoja XSL que muestre las bebidas en una tabla HTML con las columnas:
  Nombre
  Precio
  Tipo

Requisitos
  Archivo: bebidas_2.xsl
  Usar una tabla (<table>)
  Mostrar todas las bebidas
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
                <td>Tipo</td>
            </tr>
            <xsl:for-each select="menu/bebida">
                <tr>
                    <td><xsl:value-of select="nombre"/></td>
                    <td><xsl:value-of select="precio"/>$</td>
                    <td><xsl:value-of select="tipo"/></td>
                </tr>
            </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>