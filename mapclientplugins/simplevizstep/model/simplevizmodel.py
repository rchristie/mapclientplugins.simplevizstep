'''
Created on Aug 12, 2015

@author: Richard Christie
'''

import os
from opencmiss.zinc.context import Context
from opencmiss.zinc.scenecoordinatesystem import SCENECOORDINATESYSTEM_NORMALISED_WINDOW_FIT_LEFT
from opencmiss.zinc.status import OK as ZINC_OK
from mapclientplugins.simplevizstep.utils import zinc as zincutils

class SimpleVizModel(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._context = Context("SimpleViz")
        # set up standard materials and glyphs so we can use them elsewhere
        materialmodule = self._context.getMaterialmodule()
        materialmodule.defineStandardMaterials()
        glyphmodule = self._context.getGlyphmodule()
        glyphmodule.defineStandardGlyphs()
        self._location = None
        self.initialise()

    def initialise(self):
        '''
        Ensure scene for this region is not in use before calling!
        '''
        self._rootRegion = self._context.createRegion()

    def getContext(self):
        return self._context

    def setLocation(self, location):
        self._location = location

    def getRootRegion(self):
        return self._rootRegion

    def loadScript(self, inputScriptFileName):
        '''
        Load model via python script file implementing loadModel(region).
        '''
        # set current directory to path from file, to support scripts and fieldml with external resources
        path = os.path.dirname(inputScriptFileName)
        os.chdir(path)
        f = open(inputScriptFileName, 'r')
        myfunctions = {}
        exec f in myfunctions
        success = myfunctions['loadModel'](self._rootRegion)
        if not success:
            raise ValueError('Could not load ' + inputScriptFileName)

# ----- Graphics Settings -----

# ----- View Settings -----

# ----- Time Settings -----

    def autorangeTime(self):
        '''
        Set time min/max to time range of finite element field parameters.
        '''
        rootRegion = self.getRootRegion()
        minimum, maximum = zincutils.getRegionTreeTimeRange(rootRegion)
        if minimum is None:
            minimum = 0.0
            maximum = 0.0
        timekeepermodule = self._context.getTimekeepermodule()
        timekeeper = timekeepermodule.getDefaultTimekeeper()
        timekeeper.setMinimumTime(minimum)
        timekeeper.setMaximumTime(maximum)
        currentTime = timekeeper.getTime()
        if currentTime < minimum:
            timekeeper.setTime(minimum)
        elif currentTime > maximum:
            timekeeper.setTime(maximum)

    def getMinimumTime(self):
        timekeeper = self._context.getTimekeepermodule().getDefaultTimekeeper()
        return timekeeper.getMinimumTime()

    def setMinimumTime(self, minimumTime):
        timekeeper = self._context.getTimekeepermodule().getDefaultTimekeeper()
        timekeeper.setMinimumTime(minimumTime)

    def getMaximumTime(self):
        timekeeper = self._context.getTimekeepermodule().getDefaultTimekeeper()
        return timekeeper.getMaximumTime()

    def setMaximumTime(self, maximumTime):
        timekeeper = self._context.getTimekeepermodule().getDefaultTimekeeper()
        timekeeper.setMaximumTime(maximumTime)

    def getTime(self):
        timekeeper = self._context.getTimekeepermodule().getDefaultTimekeeper()
        return timekeeper.getTime()

    def setTime(self, time):
        timekeeper = self._context.getTimekeepermodule().getDefaultTimekeeper()
        timekeeper.setTime(time)

# ----- Rendering Settings -----

    def checkTessellationDivisions(self, minimumDivisions, refinementFactors):
        '''
        Check total divisions not too high or get user confirmation
        Call with both of the vectors set, each must have at least one component.
        Returns True if within limits, False if need user confirmation.
        '''
        limit = 100000 # max elements*totalsize for each dimension

        min = 1
        ref = 1
        totalDivisions = [1,1,1]
        totalSize3d = 1
        for i in range(3):
            if i < len(minimumDivisions):
                min = minimumDivisions[i]
            if i < len(refinementFactors):
                ref = refinementFactors[i]
            totalDivisions[i] = min*ref
            totalSize3d = totalSize3d*min*ref
        totalSize2d = totalDivisions[0]*totalDivisions[1]
        if totalDivisions[1]*totalDivisions[2] > totalSize2d:
            totalSize2d = totalDivisions[1]*totalDivisions[2]
        if totalDivisions[2]*totalDivisions[0] > totalSize2d:
            totalSize2d = totalDivisions[2]*totalDivisions[0]
        totalSize1d = totalDivisions[0]
        if totalDivisions[1] > totalSize1d:
            totalSize1d = totalDivisions[1]
        if totalDivisions[2] > totalSize1d:
            totalSize1d = totalDivisions[2]

        meshSize3d = zincutils.getRegionTreeMeshSize(self._rootRegion, 3)
        limit3d = limit
        if limit3d < meshSize3d:
            limit3d = meshSize3d
        overLimit3d = totalSize3d*meshSize3d > limit3d

        meshSize2d = zincutils.getRegionTreeMeshSize(self._rootRegion, 2)
        limit2d = limit
        if limit2d < meshSize2d:
            limit2d = meshSize2d
        overLimit2d = totalSize2d*meshSize2d > limit2d

        meshSize1d = zincutils.getRegionTreeMeshSize(self._rootRegion, 1)
        limit1d = limit
        if limit1d < meshSize1d:
            limit1d = meshSize1d
        overLimit1d = totalSize1d*meshSize1d > limit1d

        if not (overLimit1d or overLimit2d or overLimit3d):
            return True
        return False

    def getTessellationMinimumDivisions(self):
        tessellation = self._context.getTessellationmodule().getDefaultTessellation()
        result, minimumDivisions = tessellation.getMinimumDivisions(3)
        return minimumDivisions

    def setTessellationMinimumDivisions(self, minimumDivisions):
        tessellation = self._context.getTessellationmodule().getDefaultTessellation()
        return ZINC_OK == tessellation.setMinimumDivisions(minimumDivisions)

    def getTessellationRefinementFactors(self):
        tessellation = self._context.getTessellationmodule().getDefaultTessellation()
        result, refinementFactors = tessellation.getRefinementFactors(3)
        return refinementFactors

    def setTessellationRefinementFactors(self, refinementFactors):
        tessellation = self._context.getTessellationmodule().getDefaultTessellation()
        return ZINC_OK == tessellation.setRefinementFactors(refinementFactors)

    def getTessellationCircleDivisions(self):
        tessellation = self._context.getTessellationmodule().getDefaultTessellation()
        return tessellation.getCircleDivisions()

    def setTessellationCircleDivisions(self, circleDivisions):
        tessellationmodule = self._context.getTessellationmodule()
        # set circle divisions for all tessellations in tessellationmodule
        result = ZINC_OK
        tessellationmodule.beginChange()
        iter = tessellationmodule.createTessellationiterator()
        tessellation = iter.next()
        while tessellation.isValid():
            result = tessellation.setCircleDivisions(circleDivisions)
            if ZINC_OK != result:
                break # can't raise here otherwise no call to endChange()
            tessellation = iter.next()
        tessellationmodule.endChange()
        return result

# ----- Data Colouring Settings -----

    def spectrumAutorange(self, scenefilter):
        '''
        Set spectrum min/max to fit range of data in scene graphics filtered by scenefilter.
        '''
        spectrummodule = self._context.getSpectrummodule()
        spectrum = spectrummodule.getDefaultSpectrum()
        scene = self._rootRegion.getScene()
        result, minimum, maximum = scene.getSpectrumDataRange(scenefilter, spectrum, 1)
        if result >= 1: # result is number of components with range, can exceed 1
            spectrummodule.beginChange()
            spectrumcomponent = spectrum.getFirstSpectrumcomponent()
            spectrumcomponent.setRangeMinimum(minimum)
            spectrumcomponent.setRangeMaximum(maximum)
            spectrummodule.endChange()

    def getSpectrumMinimum(self):
        spectrum = self._context.getSpectrummodule().getDefaultSpectrum()
        spectrumcomponent = spectrum.getFirstSpectrumcomponent()
        return spectrumcomponent.getRangeMinimum()

    def setSpectrumMinimum(self, minimum):
        spectrum = self._context.getSpectrummodule().getDefaultSpectrum()
        spectrumcomponent = spectrum.getFirstSpectrumcomponent()
        return spectrumcomponent.setRangeMinimum(minimum)

    def getSpectrumMaximum(self):
        spectrum = self._context.getSpectrummodule().getDefaultSpectrum()
        spectrumcomponent = spectrum.getFirstSpectrumcomponent()
        return spectrumcomponent.getRangeMaximum()

    def setSpectrumMaximum(self, maximum):
        spectrum = self._context.getSpectrummodule().getDefaultSpectrum()
        spectrumcomponent = spectrum.getFirstSpectrumcomponent()
        return spectrumcomponent.setRangeMaximum(maximum)

    def addSpectrumColourBar(self):
        '''
        Add an overlay graphics showing the default spectrum colour bar.
        '''
        colourbarName = 'colourbar'
        scene = self._rootRegion.getScene()
        scene.beginChange()
        spectrummodule = scene.getSpectrummodule()
        spectrum = spectrummodule.getDefaultSpectrum()
        glyphmodule = scene.getGlyphmodule()
        glyphmodule.beginChange()
        colourbar = glyphmodule.findGlyphByName(colourbarName)
        if not colourbar.isValid():
            colourbar = glyphmodule.createGlyphColourBar(spectrum)
            colourbar.setName(colourbarName)
        glyphmodule.endChange()
        graphics = scene.findGraphicsByName(colourbarName)
        if graphics.isValid():
            scene.removeGraphics(graphics)
        graphics = scene.createGraphicsPoints()
        graphics.setName(colourbarName)
        graphics.setScenecoordinatesystem(SCENECOORDINATESYSTEM_NORMALISED_WINDOW_FIT_LEFT)
        pointattributes = graphics.getGraphicspointattributes()
        pointattributes.setGlyph(colourbar)
        pointattributes.setBaseSize([1.0,1.0,1.0])
        pointattributes.setGlyphOffset([-0.9,0.0,0.0])
        scene.endChange()

# ----- Output Settings -----
