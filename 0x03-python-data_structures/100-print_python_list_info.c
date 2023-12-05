#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pyobject
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	PyObject *q;
	int allocation, size, i = 0;

	allocation = ((PyListObject *)p)->allocated;
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocation);
	for (i = 0; i < size; i++)
	{
		q = PyList_GetItem(p, i);
		printf("Element %d: ", i);
		printf("%s\n", Py_TYPE(q)->tp_name);
	}
}
