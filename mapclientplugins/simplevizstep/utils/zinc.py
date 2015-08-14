'''
Created on Aug 12, 2015

@author: rchristie
'''

from opencmiss.zinc.field import Field

def getRegionTreeMeshSize(region, dimension):
    '''
    Get the number of elements of given dimension in the region and all its child regions.
    :return meshSize
    '''
    fieldmodule = region.getFieldmodule()
    mesh = fieldmodule.findMeshByDimension(dimension)
    meshSize = mesh.getSize()
    # recurse children
    child = region.getFirstChild()
    while child.isValid():
        meshSize = meshSize + getRegionTreeMeshSize(child, dimension)
        child = child.getNextSibling()
    return meshSize

def getRegionTreeTimeRange(region):
    '''
    Recursively get the time range of finite element field parameters in region, or any child regions
    :return minimum, maximum or None, None if no range
    '''
    minimum = None
    maximum = None
    # it's not easy to get the range of time; assume all nodes have same
    # time range, and use timesequence from first node field with one.
    # One problem is that often the last time represents the start of an
    # increment, so the new range should be higher, which matters if animating
    fieldmodule = region.getFieldmodule()
    for fieldDomainType in [Field.DOMAIN_TYPE_NODES, Field.DOMAIN_TYPE_DATAPOINTS]:
        nodeset = fieldmodule.findNodesetByFieldDomainType(fieldDomainType)
        nodeiter = nodeset.createNodeiterator()
        node = nodeiter.next()
        if node.isValid:
            fielditer = fieldmodule.createFielditerator()
            field = fielditer.next()
            while field.isValid():
                feField = field.castFiniteElement()
                if feField.isValid():
                    nodetemplate = nodeset.createNodetemplate()
                    nodetemplate.defineFieldFromNode(feField, node)
                    timesequence = nodetemplate.getTimesequence(feField)
                    if timesequence.isValid():
                        count = timesequence.getNumberOfTimes()
                        if count > 0:
                            thisMinimum = timesequence.getTime(1)
                            thisMaximum = timesequence.getTime(count)
                            if minimum is None:
                                minimum = thisMinimum
                                maximum = thisMaximum
                            elif thisMinimum < minimum:
                                minimum = thisMinimum
                            elif thisMaximum > maximum:
                                maximum = thisMaximum
                field = fielditer.next()
    # recurse children
    child = region.getFirstChild()
    while child.isValid():
        thisMinimum, thisMaximum = getRegionTreeTimeRange(child)
        if thisMinimum is not None:
            if minimum is None:
                minimum = thisMinimum
                maximum = thisMaximum
            elif thisMinimum < minimum:
                minimum = thisMinimum
            elif thisMaximum > maximum:
                maximum = thisMaximum
        child = child.getNextSibling()
    return minimum, maximum
