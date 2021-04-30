# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simplevizwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from opencmiss.zincwidgets.sceneeditorwidget import SceneEditorWidget
from opencmiss.zincwidgets.regionchooserwidget import RegionChooserWidget
from opencmiss.zincwidgets.sceneviewereditorwidget import SceneviewerEditorWidget
from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget


class Ui_SimpleVizWidget(object):
    def setupUi(self, SimpleVizWidget):
        if not SimpleVizWidget.objectName():
            SimpleVizWidget.setObjectName(u"SimpleVizWidget")
        SimpleVizWidget.resize(580, 616)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SimpleVizWidget.sizePolicy().hasHeightForWidth())
        SimpleVizWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(SimpleVizWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dockWidget = QDockWidget(SimpleVizWidget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy1)
        self.dockWidget.setMinimumSize(QSize(230, 178))
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        sizePolicy1.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 250, 552))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.toolBox = QToolBox(self.scrollAreaWidgetContents_2)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy1.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy1)
        self.toolBox.setMinimumSize(QSize(0, 0))
        self.toolBox.setStyleSheet(u"QToolBox::tab {\n"
"         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                     stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"         border-radius: 5px;\n"
"         color: black;\n"
"     }\n"
"\n"
"     QToolBox::tab:selected { /* italicize selected tabs */\n"
"         font: bold;\n"
"         color: black;\n"
"     }\n"
"QToolBox {\n"
"    padding : 0\n"
"}")
        self.toolBox.setFrameShape(QFrame.NoFrame)
        self.toolBox.setFrameShadow(QFrame.Plain)
        self.graphics = QWidget()
        self.graphics.setObjectName(u"graphics")
        self.graphics.setGeometry(QRect(0, 0, 250, 396))
        sizePolicy1.setHeightForWidth(self.graphics.sizePolicy().hasHeightForWidth())
        self.graphics.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.graphics)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.region_widget = QWidget(self.graphics)
        self.region_widget.setObjectName(u"region_widget")
        self.formLayout_5 = QFormLayout(self.region_widget)
        self.formLayout_5.setContentsMargins(3, 3, 3, 3)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setHorizontalSpacing(3)
        self.formLayout_5.setVerticalSpacing(3)
        self.region_label = QLabel(self.region_widget)
        self.region_label.setObjectName(u"region_label")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.region_label)

        self.region_chooser = RegionChooserWidget(self.region_widget)
        self.region_chooser.setObjectName(u"region_chooser")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.region_chooser)


        self.verticalLayout_3.addWidget(self.region_widget)

        self.scene_editor = SceneEditorWidget(self.graphics)
        self.scene_editor.setObjectName(u"scene_editor")
        sizePolicy1.setHeightForWidth(self.scene_editor.sizePolicy().hasHeightForWidth())
        self.scene_editor.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.scene_editor)

        self.toolBox.addItem(self.graphics, u"Graphics")
        self.view = QWidget()
        self.view.setObjectName(u"view")
        self.view.setGeometry(QRect(0, 0, 250, 396))
        sizePolicy1.setHeightForWidth(self.view.sizePolicy().hasHeightForWidth())
        self.view.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.view)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sceneviewer_editor_widget = SceneviewerEditorWidget(self.view)
        self.sceneviewer_editor_widget.setObjectName(u"sceneviewer_editor_widget")

        self.verticalLayout_5.addWidget(self.sceneviewer_editor_widget)

        self.toolBox.addItem(self.view, u"View")
        self.time = QWidget()
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(0, 0, 250, 396))
        self.verticalLayout_8 = QVBoxLayout(self.time)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.time_autorange_button = QPushButton(self.time)
        self.time_autorange_button.setObjectName(u"time_autorange_button")

        self.verticalLayout_8.addWidget(self.time_autorange_button)

        self.frame_2 = QFrame(self.time)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.time_minimum_label = QLabel(self.frame_2)
        self.time_minimum_label.setObjectName(u"time_minimum_label")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.time_minimum_label)

        self.time_minimum_lineedit = QLineEdit(self.frame_2)
        self.time_minimum_lineedit.setObjectName(u"time_minimum_lineedit")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.time_minimum_lineedit)

        self.time_maximum_label = QLabel(self.frame_2)
        self.time_maximum_label.setObjectName(u"time_maximum_label")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.time_maximum_label)

        self.time_maximum_lineedit = QLineEdit(self.frame_2)
        self.time_maximum_lineedit.setObjectName(u"time_maximum_lineedit")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.time_maximum_lineedit)

        self.time_lineedit = QLineEdit(self.frame_2)
        self.time_lineedit.setObjectName(u"time_lineedit")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.time_lineedit)

        self.time_label = QLabel(self.frame_2)
        self.time_label.setObjectName(u"time_label")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.time_label)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.time_slider = QSlider(self.time)
        self.time_slider.setObjectName(u"time_slider")
        self.time_slider.setMaximum(10000)
        self.time_slider.setSingleStep(10)
        self.time_slider.setPageStep(100)
        self.time_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_8.addWidget(self.time_slider)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.toolBox.addItem(self.time, u"Time")
        self.rendering = QWidget()
        self.rendering.setObjectName(u"rendering")
        self.rendering.setGeometry(QRect(0, 0, 250, 396))
        self.verticalLayout_7 = QVBoxLayout(self.rendering)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tessellation_groupbox = QGroupBox(self.rendering)
        self.tessellation_groupbox.setObjectName(u"tessellation_groupbox")
        sizePolicy.setHeightForWidth(self.tessellation_groupbox.sizePolicy().hasHeightForWidth())
        self.tessellation_groupbox.setSizePolicy(sizePolicy)
        self.formLayout_2 = QFormLayout(self.tessellation_groupbox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.tessellation_minimum_divisions_label = QLabel(self.tessellation_groupbox)
        self.tessellation_minimum_divisions_label.setObjectName(u"tessellation_minimum_divisions_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.tessellation_minimum_divisions_label)

        self.tessellation_minimum_divisions_lineedit = QLineEdit(self.tessellation_groupbox)
        self.tessellation_minimum_divisions_lineedit.setObjectName(u"tessellation_minimum_divisions_lineedit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.tessellation_minimum_divisions_lineedit)

        self.tessellation_refinement_factors_label = QLabel(self.tessellation_groupbox)
        self.tessellation_refinement_factors_label.setObjectName(u"tessellation_refinement_factors_label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.tessellation_refinement_factors_label)

        self.tessellation_refinement_factors_lineedit = QLineEdit(self.tessellation_groupbox)
        self.tessellation_refinement_factors_lineedit.setObjectName(u"tessellation_refinement_factors_lineedit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.tessellation_refinement_factors_lineedit)

        self.tessellation_circle_divisions_label = QLabel(self.tessellation_groupbox)
        self.tessellation_circle_divisions_label.setObjectName(u"tessellation_circle_divisions_label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.tessellation_circle_divisions_label)

        self.tessellation_circle_divisions_lineedit = QLineEdit(self.tessellation_groupbox)
        self.tessellation_circle_divisions_lineedit.setObjectName(u"tessellation_circle_divisions_lineedit")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.tessellation_circle_divisions_lineedit)


        self.verticalLayout_7.addWidget(self.tessellation_groupbox)

        self.perturb_lines_checkbox = QCheckBox(self.rendering)
        self.perturb_lines_checkbox.setObjectName(u"perturb_lines_checkbox")

        self.verticalLayout_7.addWidget(self.perturb_lines_checkbox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.rendering, u"Rendering")
        self.data_colouring = QWidget()
        self.data_colouring.setObjectName(u"data_colouring")
        self.data_colouring.setGeometry(QRect(0, 0, 250, 396))
        self.verticalLayout_6 = QVBoxLayout(self.data_colouring)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.spectrum_autorange_button = QPushButton(self.data_colouring)
        self.spectrum_autorange_button.setObjectName(u"spectrum_autorange_button")

        self.verticalLayout_6.addWidget(self.spectrum_autorange_button)

        self.frame_3 = QFrame(self.data_colouring)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.spectrum_minimum_label = QLabel(self.frame_3)
        self.spectrum_minimum_label.setObjectName(u"spectrum_minimum_label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.spectrum_minimum_label)

        self.spectrum_minimum_lineedit = QLineEdit(self.frame_3)
        self.spectrum_minimum_lineedit.setObjectName(u"spectrum_minimum_lineedit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.spectrum_minimum_lineedit)

        self.spectrum_maximum_lineedit = QLineEdit(self.frame_3)
        self.spectrum_maximum_lineedit.setObjectName(u"spectrum_maximum_lineedit")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.spectrum_maximum_lineedit)

        self.spectrum_maximum_label = QLabel(self.frame_3)
        self.spectrum_maximum_label.setObjectName(u"spectrum_maximum_label")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.spectrum_maximum_label)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.spectrum_add_colour_bar_button = QPushButton(self.data_colouring)
        self.spectrum_add_colour_bar_button.setObjectName(u"spectrum_add_colour_bar_button")

        self.verticalLayout_6.addWidget(self.spectrum_add_colour_bar_button)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.toolBox.addItem(self.data_colouring, u"Data Colouring")
        self.output = QWidget()
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(0, 0, 250, 396))
        self.verticalLayout_9 = QVBoxLayout(self.output)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.save_image_button = QPushButton(self.output)
        self.save_image_button.setObjectName(u"save_image_button")

        self.verticalLayout_9.addWidget(self.save_image_button)

        self.save_webgl_button = QPushButton(self.output)
        self.save_webgl_button.setObjectName(u"save_webgl_button")

        self.verticalLayout_9.addWidget(self.save_webgl_button)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)

        self.toolBox.addItem(self.output, u"Output")

        self.verticalLayout_2.addWidget(self.toolBox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea)

        self.frame = QFrame(self.dockWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.view_all_button = QPushButton(self.frame)
        self.view_all_button.setObjectName(u"view_all_button")

        self.horizontalLayout_2.addWidget(self.view_all_button)

        self.done_button = QPushButton(self.frame)
        self.done_button.setObjectName(u"done_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.done_button.sizePolicy().hasHeightForWidth())
        self.done_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.done_button)


        self.verticalLayout.addWidget(self.frame)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.sceneviewer_widget = SceneviewerWidget(SimpleVizWidget)
        self.sceneviewer_widget.setObjectName(u"sceneviewer_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sceneviewer_widget.sizePolicy().hasHeightForWidth())
        self.sceneviewer_widget.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.sceneviewer_widget)


        self.retranslateUi(SimpleVizWidget)

        self.toolBox.setCurrentIndex(5)
        self.toolBox.layout().setSpacing(2)


        QMetaObject.connectSlotsByName(SimpleVizWidget)
    # setupUi

    def retranslateUi(self, SimpleVizWidget):
        SimpleVizWidget.setWindowTitle(QCoreApplication.translate("SimpleVizWidget", u"Form", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("SimpleVizWidget", u"SimpleViz Tools", None))
#if QT_CONFIG(accessibility)
        self.toolBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.region_label.setText(QCoreApplication.translate("SimpleVizWidget", u"Region:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.graphics), QCoreApplication.translate("SimpleVizWidget", u"Graphics", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.view), QCoreApplication.translate("SimpleVizWidget", u"View", None))
        self.time_autorange_button.setText(QCoreApplication.translate("SimpleVizWidget", u"Autorange time", None))
        self.time_minimum_label.setText(QCoreApplication.translate("SimpleVizWidget", u"Minimum:", None))
        self.time_maximum_label.setText(QCoreApplication.translate("SimpleVizWidget", u"Maximum:", None))
        self.time_label.setText(QCoreApplication.translate("SimpleVizWidget", u"Time:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.time), QCoreApplication.translate("SimpleVizWidget", u"Time", None))
        self.tessellation_groupbox.setTitle(QCoreApplication.translate("SimpleVizWidget", u"Tessellation divisions:", None))
        self.tessellation_minimum_divisions_label.setText(QCoreApplication.translate("SimpleVizWidget", u"Minimum:", None))
        self.tessellation_refinement_factors_label.setText(QCoreApplication.translate("SimpleVizWidget", u"Refinement:", None))
        self.tessellation_circle_divisions_label.setText(QCoreApplication.translate("SimpleVizWidget", u"Circle:", None))
        self.perturb_lines_checkbox.setText(QCoreApplication.translate("SimpleVizWidget", u"Perturb lines", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.rendering), QCoreApplication.translate("SimpleVizWidget", u"Rendering", None))
        self.spectrum_autorange_button.setText(QCoreApplication.translate("SimpleVizWidget", u"Autorange spectrum", None))
        self.spectrum_minimum_label.setText(QCoreApplication.translate("SimpleVizWidget", u"Minimum:", None))
        self.spectrum_maximum_label.setText(QCoreApplication.translate("SimpleVizWidget", u"Maximum:", None))
        self.spectrum_add_colour_bar_button.setText(QCoreApplication.translate("SimpleVizWidget", u"Add colour bar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.data_colouring), QCoreApplication.translate("SimpleVizWidget", u"Data Colouring", None))
        self.save_image_button.setText(QCoreApplication.translate("SimpleVizWidget", u"Save image...", None))
        self.save_webgl_button.setText(QCoreApplication.translate("SimpleVizWidget", u"Save WebGL...", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.output), QCoreApplication.translate("SimpleVizWidget", u"Output", None))
        self.view_all_button.setText(QCoreApplication.translate("SimpleVizWidget", u"View All", None))
        self.done_button.setText(QCoreApplication.translate("SimpleVizWidget", u"Done", None))
    # retranslateUi

