// Local headers
#include "program.hpp"
#include "gloom/gloom.hpp"
#include "gloom/shader.hpp"

#include <stdio.h>
int set_vao(float* coord, int* indices){
	// Create and bind VAO
	uint array = 0;
	glGenVertexArrays(1, &array);
	glBindVertexArray(array);
	
	// Create and bind VBO
	uint buffer = 0;
	glGenBuffers(1, &buffer);
	glBindBuffer(GL_ARRAY_BUFFER, buffer);

	// Put data to VBO
	glBufferData(GL_ARRAY_BUFFER, 9 * sizeof(float), coord, GL_STATIC_DRAW);

	// Set vertex attributes
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, 0);

	// Enable VBO
	glEnableVertexAttribArray(1);

	// Create and bind index VBO
	uint index_buffer = 0;
	glGenBuffers(1, &index_buffer);
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, index_buffer);

	// Fill index buffer
	glBufferData(GL_ELEMENT_ARRAY_BUFFER, 3*sizeof(int), indices, GL_STATIC_DRAW);

	printGLError();

	return array;
}


void runProgram(GLFWwindow* window)
{
    // Set GLFW callback mechanism(s)
    glfwSetKeyCallback(window, keyboardCallback);

    // Enable depth (Z) buffer (accept "closest" fragment)
    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);

    // Configure miscellaneous OpenGL settings
    glEnable(GL_CULL_FACE);

    // Set default colour after clearing the colour buffer
    glClearColor(0.3f, 0.3f, 0.4f, 1.0f);

    // Set up your scene here (create Vertex Array Objects, etc.)
	
	Gloom::Shader shader;
	shader.makeBasicShader("/home/shomeb/a/andreanv/Documents/psychic-garbanzo/graphics/ass1/gloom/gloom/shaders/simple.vert", "/home/shomeb/a/andreanv/Documents/psychic-garbanzo/graphics/ass1/gloom/gloom/shaders/simple.frag");
	shader.link();

	float triangle_coord[] = {-0.6, -0.6, 0.0, 0.6, -0.6, 0.0, 0.0, 0.6, 0.0};
	int triangle_idx[] = {0, 1, 2};
	int triangleOne = 0;
	triangleOne = set_vao(triangle_coord, triangle_idx);


    // Rendering Loop
    while (!glfwWindowShouldClose(window))
    {
        // Clear colour and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        // Draw your scene here
		shader.activate();

		glBindVertexArray(triangleOne);
		glDrawElements(GL_TRIANGLE_STRIP, 3, GL_UNSIGNED_INT, 0);
		printGLError();

		//shader.deactivate();
        // Handle other events
        glfwPollEvents();

        // Flip buffers
        glfwSwapBuffers(window);
	}
}


void keyboardCallback(GLFWwindow* window, int key, int scancode,
                      int action, int mods)
{
    // Use escape key for terminating the GLFW window
    if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
    {
        glfwSetWindowShouldClose(window, GL_TRUE);
    }
}
