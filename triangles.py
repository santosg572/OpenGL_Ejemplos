from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def myInit():
    glGenVertexArrays(NumVAOs, VAOs)
    glBindVertexArray(VAOs[Triangles])
    vertices[NumVertices][2] = {
       { -0.90, -0.90 }, { 0.85, -0.90 }, 
       { -0.90, 0.85 }, { 0.90, -0.85 }, 
       { 0.90, 0.90 }, { -0.85, 0.90 }
    }
    glGenBuffers(NumBuffers, Buffers)
    glBindBuffer(GL_ARRAY_BUFFER, Buffers[ArrayBuffer])
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    shaders[] = {
     { GL_VERTEX_SHADER, "triangles.vert" }, { GL_FRAGMENT_SHADER, "triangles.frag" }, { GL_NONE, NULL }

     };

    program = LoadShaders(shaders); glUseProgram(program);

    glVertexAttribPointer(vPosition, 2, GL_FLOAT, GL_FALSE, 0, BUFFER_OFFSET(0)); glEnableVertexAttribArray(vPosition);


    glClearColor(1.0, 1.0, 0.0, 1.0) 
    glColor3f(0.2, 0.5, 0.4)
    glPointSize(10.0)
    gluOrtho2D(0, 500, 0, 500)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POINTS)
    glVertex2f(100, 100)
    glVertex2f(300, 200)
    glEnd()

    glBegin( GL_QUADS ) 
    glVertex2f( 100.0, 100.0 ) 
    glVertex2f( 300.0, 100.0 ) 
    glVertex2f( 300.0, 200.0 ) 
    glVertex2f( 100.0, 200.0 ) 
    glEnd()  

    glBegin(  GL_TRIANGLE_STRIP ) 
    glVertex2f( 100.0, 210.0 ) 
    glVertex2f( 300.0, 210.0 ) 
    glVertex2f( 300.0, 310.0 ) 
    glEnd() 

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(500, 500)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("My OpenGL Code")
myInit()
glutDisplayFunc(display) 
glutMainLoop()


