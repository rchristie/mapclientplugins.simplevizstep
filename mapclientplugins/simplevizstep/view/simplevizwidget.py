'''
Created on Aug 12, 2015

@author: Richard Christie
'''
from PySide import QtGui, QtCore

import json
from mapclientplugins.simplevizstep.view.ui_simplevizwidget import Ui_SimpleVizWidget

class SimpleVizWidget(QtGui.QWidget):
    '''
    classdocs
    '''

    def __init__(self, model, parent=None):
        '''
        Constructor
        '''
        super(SimpleVizWidget, self).__init__(parent)
        self._ui = Ui_SimpleVizWidget()
        self._ui.setupUi(self)
        self._model = model
        self._ui.sceneviewer_widget.setContext(model.getContext())
        self._ui.sceneviewer_widget.graphicsInitialized.connect(self._graphicsInitialized)
        self._doneCallback = None
        self._makeConnections()

    def _graphicsInitialized(self):
        '''
        Callback for when SceneviewerWidget is initialised
        Set custom scene from model
        '''
        sceneviewer = self._ui.sceneviewer_widget.getSceneviewer()
        if sceneviewer is not None:
            scene = self._model.getRootRegion().getScene()
            sceneviewer.setScene(scene)
            self._ui.sceneviewer_widget.setSelectModeAll()
            self._ui.sceneviewer_editor_widget.setSceneviewer(sceneviewer)
            self.viewAll()

    def _makeConnections(self):
        self._ui.done_button.clicked.connect(self._doneButtonClicked)
        self._ui.view_all_button.clicked.connect(self.viewAll)
        self._ui.toolBox.currentChanged.connect(self._toolBoxPageChanged)
        self._ui.region_chooser.currentIndexChanged.connect(self._regionChanged)
        self._makeConnectionsTime()
        self._makeConnectionsRendering()
        self._makeConnectionsDataColouring()
        self._makeConnectionsOutput()

    def initialise(self):
        '''
        Clear the model and view, reset display of widgets
        '''
        self._model.initialise()
        self._graphicsInitialized()
        self._ui.dockWidget.setFloating(False)
        self._ui.toolBox.setCurrentIndex(0)
        self._allSettingsDisplay()

    def getModel(self):
        return self._model

    def registerDoneExecution(self, doneCallback):
        self._doneCallback = doneCallback

    def _doneButtonClicked(self):
        self.initialise() # to free model resources
        self._doneCallback()

    def loadScript(self, inputScriptFileName):
        success = self._model.loadScript(inputScriptFileName)
        rootRegion = self._model.getRootRegion()
        # rebuild region chooser tree
        self._ui.region_chooser.setRootRegion(rootRegion)
        scene = rootRegion.getScene()
        self._ui.scene_editor.setScene(scene)
        self.viewAll()
        self._allSettingsDisplay()
        return success

    def _toolBoxPageChanged(self, page):
        # enable view widget updates only when looking at them
        self._ui.sceneviewer_editor_widget.setEnableUpdates(page == 1)

    def _displayReal(self, widget, value):
        '''
        Display real value in a widget
        '''
        newText = unicode('{:.5g}'.format(value))
        widget.setText(newText)

    def _displayScaleInteger(self, widget, values, numberFormat = '{:d}'):
        '''
        Display vector of integer values in a widget, separated by '*'
        '''
        newText = "*".join(numberFormat.format(value) for value in values)
        widget.setText(newText)

    def _parseScaleInteger(self, widget):
        '''
        Return integer vector from comma separated text in line edit widget
        '''
        text = widget.text()
        values = [int(value) for value in text.split('*')]
        if len(values) < 1:
            raise
        return values

    def _allSettingsDisplay(self):
        '''
        Show initial values on widgets
        '''
        self._timeSettingsDisplay()
        self._renderingSettingsDisplay()
        self._dataColouringSettingsDisplay()

# ----- Graphics Settings -----

    def _regionChanged(self):
        region = self._ui.region_chooser.getRegion()
        self._ui.scene_editor.setScene(region.getScene())

# ----- View Settings -----

    def viewAll(self):
        '''
        Ask sceneviewer to show all of scene.
        '''
        if self._ui.sceneviewer_editor_widget.getSceneviewer() is not None:
            self._ui.sceneviewer_editor_widget.viewAll()

# ----- Time Settings -----

    def _makeConnectionsTime(self):
        self._ui.time_autorange_button.clicked.connect(self._timeAutorangeClicked)
        self._ui.time_minimum_lineedit.editingFinished.connect(self._timeMinimumEntered)
        self._ui.time_maximum_lineedit.editingFinished.connect(self._timeMaximumEntered)
        self._ui.time_lineedit.editingFinished.connect(self._timeEntered)
        QtCore.QObject.connect(self._ui.time_slider, QtCore.SIGNAL("valueChanged(int)"), self._timeSliderChanged)

    def _timeSettingsDisplay(self):
        self._timeMinimumDisplay()
        self._timeMaximumDisplay()
        self._timeDisplay()
        self._timeSliderDisplay()

    def _timeAutorangeClicked(self):
        '''
        Set time min/max to time range of finite element field parameters.
        '''
        self._model.autorangeTime()
        self._timeSettingsDisplay()

    def _timeMinimumDisplay(self):
        self._displayReal(self._ui.time_minimum_lineedit, self._model.getMinimumTime())

    def _timeMinimumEntered(self):
        try:
            minimumTime = float(self._ui.time_minimum_lineedit.text())
            self._model.setMinimumTime(minimumTime)
        except:
            pass
        self._timeMinimumDisplay()

    def _timeMaximumDisplay(self):
        self._displayReal(self._ui.time_maximum_lineedit, self._model.getMaximumTime())

    def _timeMaximumEntered(self):
        try:
            maximumTime = float(self._ui.time_maximum_lineedit.text())
            self._model.setMaximumTime(maximumTime)
        except:
            pass
        self._timeMaximumDisplay()

    def _timeDisplay(self):
        self._displayReal(self._ui.time_lineedit, self._model.getTime())

    def _timeEntered(self):
        try:
            time = float(self._ui.time_lineedit.text())
            self._model.setTime(time)
        except:
            pass
        self._timeDisplay()
        self._timeSliderDisplay()

    def _timeSliderDisplay(self):
        minimumTime = self._model.getMinimumTime()
        maximumTime = self._model.getMaximumTime()
        time = self._model.getTime()
        # don't want signal for my change
        self._ui.time_slider.blockSignals(True)
        if maximumTime != minimumTime:
            value = int(time*(10000.999/(maximumTime - minimumTime)))
        else:
            value = 0
        self._ui.time_slider.setValue(value)
        self._ui.time_slider.blockSignals(False)

    def _timeSliderChanged(self, value):
        minimumTime = self._model.getMinimumTime()
        maximumTime = self._model.getMaximumTime()
        if maximumTime != minimumTime:
            time = float(value)*((maximumTime - minimumTime)/10000.0)
        else:
            time = minimumTime
        self._model.setTime(time)
        self._timeDisplay()

# ----- Rendering Settings -----

    def _makeConnectionsRendering(self):
        self._ui.tessellation_minimum_divisions_lineedit.returnPressed.connect(self._tessellationMinimumDivisionsEntered)
        self._ui.tessellation_refinement_factors_lineedit.returnPressed.connect(self._tessellationRefinementFactorsEntered)
        self._ui.tessellation_circle_divisions_lineedit.returnPressed.connect(self._tessellationCircleDivisionsEntered)
        self._ui.tessellation_minimum_divisions_lineedit.editingFinished.connect(self._tessellationMinimumDivisionsDisplay)
        self._ui.tessellation_refinement_factors_lineedit.editingFinished.connect(self._tessellationRefinementFactorsDisplay)
        self._ui.tessellation_circle_divisions_lineedit.editingFinished.connect(self._tessellationCircleDivisionsDisplay)
        QtCore.QObject.connect(self._ui.perturb_lines_checkbox, QtCore.SIGNAL("clicked(bool)"), self._perturbLinesStateChanged)

    def _renderingSettingsDisplay(self):
        self._tessellationMinimumDivisionsDisplay()
        self._tessellationRefinementFactorsDisplay()
        self._tessellationCircleDivisionsDisplay()

    def _checkTessellationDivisions(self, minimumDivisions, refinementFactors, widget):
        '''
        Check total divisions not too high or get user confirmation
        Call with both of the vectors set, each must have at least one component.
        Returns True if can apply.
        '''
        if self._model.checkTessellationDivisions(minimumDivisions, refinementFactors):
            return True
        # block signals otherwise editingFinished() is triggered
        widget.blockSignals(True)
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("SimpleViz")
        msgBox.setText("Warning! Fine tessellation divisions can take a long time to apply.")
        msgBox.setInformativeText("Please confirm action.")
        msgBox.setStandardButtons(QtGui.QMessageBox.Apply | QtGui.QMessageBox.Cancel)
        msgBox.setDefaultButton(QtGui.QMessageBox.Cancel)
        result = msgBox.exec_()
        widget.blockSignals(False)
        return result == QtGui.QMessageBox.Apply

    def _tessellationMinimumDivisionsDisplay(self):
        self._displayScaleInteger(self._ui.tessellation_minimum_divisions_lineedit,
                                  self._model.getTessellationMinimumDivisions())

    def _tessellationMinimumDivisionsEntered(self):
        try:
            minimumDivisions = self._parseScaleInteger(self._ui.tessellation_minimum_divisions_lineedit)
            # pack to len 3 to allow comparison with old values
            while len(minimumDivisions) < 3:
                minimumDivisions.append(minimumDivisions[-1])
            if minimumDivisions != self._model.getTessellationMinimumDivisions():
                if self._checkTessellationDivisions(minimumDivisions, self._model.getTessellationRefinementFactors(),
                                                    self._ui.tessellation_minimum_divisions_lineedit):
                    self._model.setTessellationMinimumDivisions(minimumDivisions)
        except:
            pass
        self._tessellationMinimumDivisionsDisplay()

    def _tessellationRefinementFactorsDisplay(self):
        self._displayScaleInteger(self._ui.tessellation_refinement_factors_lineedit,
                                  self._model.getTessellationRefinementFactors())

    def _tessellationRefinementFactorsEntered(self):
        try:
            refinementFactors = self._parseScaleInteger(self._ui.tessellation_refinement_factors_lineedit)
            # pack to len 3 to allow comparison with old values
            while len(refinementFactors) < 3:
                refinementFactors.append(refinementFactors[-1])
            if refinementFactors != self._model.getTessellationRefinementFactors():
                if self._checkTessellationDivisions(self._model.getTessellationMinimumDivisions(),refinementFactors,
                                                    self._ui.tessellation_refinement_factors_lineedit):
                    self._model.setTessellationRefinementFactors(refinementFactors)
        except:
            pass
        self._tessellationRefinementFactorsDisplay()

    def _tessellationCircleDivisionsDisplay(self):
        self._displayReal(self._ui.tessellation_circle_divisions_lineedit, self._model.getTessellationCircleDivisions())

    def _tessellationCircleDivisionsEntered(self):
        try:
            circleDivisions = int(self._ui.tessellation_circle_divisions_lineedit.text())
            self._model.setTessellationCircleDivisions(circleDivisions)
        except:
            pass
        self._tessellationCircleDivisionsDisplay()

    def _perturbLinesStateChanged(self, state):
        sceneviewer = self._ui.sceneviewer_widget.getSceneviewer()
        sceneviewer.setPerturbLinesFlag(state)

# ----- Data Colouring Settings -----

    def _makeConnectionsDataColouring(self):
        self._ui.spectrum_autorange_button.clicked.connect(self._spectrumAutorangeClicked)
        self._ui.spectrum_minimum_lineedit.editingFinished.connect(self._spectrumMinimumEntered)
        self._ui.spectrum_maximum_lineedit.editingFinished.connect(self._spectrumMaximumEntered)
        self._ui.spectrum_add_colour_bar_button.clicked.connect(self._spectrumAddColourBarClicked)

    def _dataColouringSettingsDisplay(self):
        self._spectrumMinimumDisplay()
        self._spectrumMaximumDisplay()

    def _spectrumAutorangeClicked(self):
        '''
        Set spectrum min/max to fit range of visible data in scene graphics.
        '''
        scenefilter = self._ui.sceneviewer_widget.getSceneviewer().getScenefilter()
        self._model.spectrumAutorange(scenefilter)
        self._dataColouringSettingsDisplay()

    def _spectrumMinimumDisplay(self):
        self._displayReal(self._ui.spectrum_minimum_lineedit, self._model.getSpectrumMinimum())

    def _spectrumMinimumEntered(self):
        try:
            minimum = float(self._ui.spectrum_minimum_lineedit.text())
            self._model.setSpectrumMinimum(minimum)
        except:
            pass
        self._spectrumMinimumDisplay()

    def _spectrumMaximumDisplay(self):
        self._displayReal(self._ui.spectrum_maximum_lineedit, self._model.getSpectrumMaximum())

    def _spectrumMaximumEntered(self):
        try:
            maximum = float(self._ui.spectrum_maximum_lineedit.text())
            self._model.setSpectrumMaximum(maximum)
        except:
            pass
        self._spectrumMaximumDisplay()

    def _spectrumAddColourBarClicked(self):
        self._model.addSpectrumColourBar()
        # ensure scene editor graphics list is redisplayed
        scene = self._model.getRootRegion().getScene()
        self._ui.scene_editor.setScene(scene)

# ----- Output Settings -----

    def _makeConnectionsOutput(self):
        self._ui.save_image_button.clicked.connect(self._saveImageClicked)
        self._ui.save_webgl_button.clicked.connect(self._saveWebGLClicked)

    def _saveImageClicked(self):
        '''
        Save the view in the window to an image file.
        '''
        fileNameTuple = QtGui.QFileDialog.getSaveFileName(self, "Save image", "", "Image files (*.jpg *.png *.tif *.*)")
        fileName = fileNameTuple[0]
        if not fileName:
            return
        image = self._ui.sceneviewer_widget.grabFrameBuffer()
        image.save(fileName)

    def exportSceneViewersettings(self, outputPrefix, numberOfResources):
        scene = self._ui.sceneviewer_widget.getSceneviewer().getScene()
        si = scene.createStreaminformationScene()
        si.setIOFormat(si.IO_FORMAT_THREEJS)
        si.setIODataType(si.IO_FORMAT_THREEJS)
        timekeepermodule = scene.getTimekeepermodule()
        timekeeper = timekeepermodule.getDefaultTimekeeper()
        minimum = timekeeper.getMinimumTime()
        maximum = timekeeper.getMaximumTime()
        time_enabled = 0
        if (maximum - minimum) > 0.001:
            time_enabled = 1
        sv = self._ui.sceneviewer_widget.getSceneviewer()
        sv.viewAll()
        nearPlane = sv.getNearClippingPlane()
        farPlane = sv.getFarClippingPlane()
        result, eyePos, lookat, upVector = sv.getLookatParameters()
        obj = { "nearPlane": nearPlane, "farPlane": farPlane, "eyePosition": eyePos, "targetPosition": lookat, "upVector": upVector, "numberOfResources": numberOfResources, "timeEnabled" : time_enabled}
        outputName = outputPrefix + "_view.json"
        export_f = open(outputName, "wb+")
        export_f.write(str(json.dumps(obj)))
        export_f.close()

    def exportScene(self, outputPrefix):
        scene = self._ui.sceneviewer_widget.getSceneviewer().getScene()
        si = scene.createStreaminformationScene()
        si.setIOFormat(si.IO_FORMAT_THREEJS)
        si.setIODataType(si.IO_FORMAT_THREEJS)
        timekeepermodule = scene.getTimekeepermodule()
        timekeeper = timekeepermodule.getDefaultTimekeeper()
        minimum = timekeeper.getMinimumTime()
        maximum = timekeeper.getMaximumTime()
        if (maximum - minimum) > 0.0:
            si.setInitialTime(minimum)
            si.setFinishTime(maximum)
            si.setNumberOfTimeSteps(51)
        number = si.getNumberOfResourcesRequired()
        i = 0
        srs = []
        while i < number:
            outputName = outputPrefix + "_" + str(i + 1) + ".json"
            srs.append(si.createStreamresourceFile(outputName))
            i = i + 1
        scene.exportScene(si)
        return number

    def _saveWebGLClicked(self):
        '''
        Save the view in the window to WebGL content.
        '''
        fileNameTuple = QtGui.QFileDialog.getSaveFileName(self, "Specify prefix", "")
        fileName = fileNameTuple[0]
        if not fileName:
            return
        numberOfResources = self.exportScene(str(fileName))
        self.exportSceneViewersettings(str(fileName), numberOfResources)
