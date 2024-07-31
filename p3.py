import numpy as np

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

listName = 1;

def  myinit():
 glNewList (listName, GL_COMPILE);
 glColor3f(1.0, 0.0, 0.0);
 glBegin (GL_TRIANGLES);
 glVertex2f (0.0, 0.0);
 glVertex2f (1.0, 0.0);
 glVertex2f (0.0, 1.0);
 glEnd ();
 glTranslatef (1.5, 0.0, 0.0);
 glEndList ();
 glShadeModel (GL_FLAT);

def drawLine():
 glBegin (GL_LINES);
 glVertex2f (0.0, 0.5);
 glVertex2f (15.0, 0.5);
 glEnd ();


def display():
 glClear (GL_COLOR_BUFFER_BIT);
 glColor3f(0.0, 1.0, 0.0);
 for i in np.range(10):
  glCallList (listName);
 drawLine ();
 glFlush ();

def  myReshape(w=0, h=0):
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if w <= h and w !=0 : 
        gluOrtho2D (0.0, 2.0, -0.5 * h/w, 1.5 *  h/ w);
    else: 
        gluOrtho2D (0.0, 2.0 *  w/ h, -0.5, 1.5); 
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(500, 500)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("My OpenGL Code")
myinit ();
#glutDisplayFunc(myReshape(100,100));
#glutMenuStateFunc(display);
glutMainLoop()


