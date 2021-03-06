# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VectorTileBulder
                                 A QGIS plugin
 Build vector tiles using Tippecanoe
                             -------------------
        begin                : 2017-04-27
        copyright            : (C) 2017 by Dave Barter - Nautoguide Ltd.
        email                : dave@nautoguide.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load VectorTileBulder class from file VectorTileBulder.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .vt_builder import VectorTileBulder
    return VectorTileBulder(iface)
