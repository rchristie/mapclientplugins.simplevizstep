'''
Created on Aug 12, 2015

@author: Richard Christie
'''
'''
MAP Client Plugin Step
'''
import os
import json

from PySide2 import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.simplevizstep.configuredialog import ConfigureDialog
from mapclientplugins.simplevizstep.model.simplevizmodel import SimpleVizModel
from mapclientplugins.simplevizstep.view.simplevizwidget import SimpleVizWidget


class simplevizStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    def __init__(self, location):
        super(simplevizStep, self).__init__('simpleviz', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Model Viewer'
        # Add any other initialisation code here:
        self._icon =  QtGui.QImage(':/simplevizstep/images/model-viewer.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        # Port data:
        self._inputScriptFileName = None # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        # Config:
        self._config = {}
        self._config['identifier'] = ''
        self._view = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        if self._view is None:
            simpleVizModel = SimpleVizModel()
            simpleVizModel.setLocation(os.path.join(self._location, self._config['identifier']))
            self._view = SimpleVizWidget(simpleVizModel)
            self._view.registerDoneExecution(self._doneExecution)
        else:
            pass
        self._view.initialise()
        if self._inputScriptFileName is not None:
            self._view.loadScript(self._inputScriptFileName)
        self._setCurrentWidget(self._view)

    def setPortData(self, index, dataIn):
        '''
        Set inputs, called by mapclient framework.
        '''
        self._inputScriptFileName = dataIn # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog()
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self):
        '''
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        '''
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.
        '''
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


