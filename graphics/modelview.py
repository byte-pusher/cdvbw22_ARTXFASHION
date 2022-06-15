 #  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/       


import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc

#GL imports for pyqt
from PyQt6.QtOpenGL import QOpenGLWindow, QOpenGLVersionProfile, QOpenGLShaderProgram, QOpenGLVersionFunctionsFactory, QOpenGLShader
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

class GlWidget(QOpenGLWidget):
    """A widget to display the OpenGL drawing"""

    def initializeGL(self):
        super().initializeGL()

        # .get() of QOpenGLVersionFunctionsFactory() has been recommended to be used instead of 
        # .versionFunctions() of QOpenGLContext() when obtaining any functions of 
        # the Open GL library.
        # Fetch version-specific functions
        gl_fts = QOpenGLVersionFunctionsFactory()
        version = QOpenGLVersionProfile()
        version.setVersion(2, 1)
        self.gl = gl_fts.get(version)
        
        # Configure
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        self.gl.glDepthFunc(self.gl.GL_LESS)
        self.gl.glEnable(self.gl.GL_CULL_FACE)

        # Create the program
        self.program = QOpenGLShaderProgram()
        self.program.addShaderFromSourceFile(
            QOpenGLShader.ShaderTypeBit.Vertex, 'graphics/vertex_shader.glsl')
        self.program.addShaderFromSourceFile(
            QOpenGLShader.ShaderTypeBit.Fragment, 'graphics/fragment_shader.glsl')
        self.program.link()

        # Get variable locations
        self.vertex_location = self.program.attributeLocation('vertex')
        self.matrix_location = self.program.uniformLocation('matrix')
        self.color_location = self.program.attributeLocation('color_attr')

        # Create transformation matrix
        self.view_matrix = qtg.QMatrix4x4()
        self.view_matrix.perspective(
            45,  # Angle
            self.width() / self.height(),  # Aspect Ratio
            0.1,  # Near clipping plane
            100.0  # Far clipping plane
        )
        self.view_matrix.translate(0, 0, -5)
        self.rotation = [0, 0, 0, 0]

    def paintGL(self):
        # Fill the window with dark violet
        self.gl.glClearColor(0.1, 0, 0.2, 1)
        self.gl.glClear(
            self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.program.bind()

        # Drawing
        front_vertices = [
            qtg.QVector3D(0.0, 1.0, 0.0),  # Peak
            qtg.QVector3D(-1.0, 0.0, 0.0),  # Bottom left
            qtg.QVector3D(1.0, 0.0, 0.0)  # Bottom right
            ]

        face_colors = (
            qtg.QColor('red'),
            qtg.QColor('orange'),
            qtg.QColor('yellow'),
        )
        gl_colors = [
            self.qcolor_to_glvec(color)
            for color in face_colors
        ]
        self.program.setUniformValue(
            self.matrix_location, self.view_matrix)
        self.program.enableAttributeArray(self.vertex_location)
        self.program.setAttributeArray(self.vertex_location, front_vertices)
        self.program.enableAttributeArray(self.color_location)
        self.program.setAttributeArray(self.color_location, gl_colors)

        # Draw the front
        self.gl.glDrawArrays(self.gl.GL_TRIANGLES, 0, 3)
        # Draw the back
        back_vertices = [
            qtg.QVector3D(x.toVector2D(), -0.5)
            for x in front_vertices]
        self.program.setAttributeArray(
            self.vertex_location, reversed(back_vertices))
            # If you try the line below instead, the back side
            # will not show unless you disable face culling
            #self.vertex_location, back_vertices)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLES, 0, 3)

        # draw the sides
        sides = [(0, 1), (1, 2), (2, 0)]
        side_vertices = list()
        for index1, index2 in sides:
            side_vertices += [
                front_vertices[index1],
                back_vertices[index1],
                back_vertices[index2],
                front_vertices[index2]
            ]
        side_colors = [
            qtg.QColor('blue'),
            qtg.QColor('purple'),
            qtg.QColor('cyan'),
            qtg.QColor('magenta'),
        ]
        gl_colors = [
            self.qcolor_to_glvec(color)
            for color in side_colors
        ] * 3

        self.program.setAttributeArray(self.color_location, gl_colors)
        self.program.setAttributeArray(self.vertex_location, side_vertices)
        self.gl.glDrawArrays(self.gl.GL_QUADS, 0, len(side_vertices))
        self.program.disableAttributeArray(self.vertex_location)
        self.program.disableAttributeArray(self.color_location)
        self.program.release()

        # Animation
        # rotate
        self.view_matrix.rotate(*self.rotation)
        self.spin_right()
        self.update()

    
    def qcolor_to_glvec(self, qcolor):
        return qtg.QVector3D(
            qcolor.red() / 255,
            qcolor.green() / 255,
            qcolor.blue() / 255
        )

    #spin/rest functions
    def spin_none(self):
        self.rotation = [0, 0, 0, 0]

    def spin_left(self):
        self.rotation = [-1, 0, 1, 0]

    def spin_right(self):
        self.rotation = [1, 0, 1, 0]

    def spin_up(self):
        self.rotation = [1, 1, 0, 0]

    def spin_down(self):
        self.rotation = [-1, 1, 0, 0]

    def zoom_in(self):
        self.view_matrix.scale(1.1, 1.1, 1.1)

    def zoom_out(self):
        self.view_matrix.scale(.9, .9, .9)
    