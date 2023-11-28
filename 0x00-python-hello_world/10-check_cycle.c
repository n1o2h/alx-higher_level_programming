#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: the list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list, *ptr2 = list;

	while(ptr1 && ptr1->next)
	{
		ptr1 = ptr1->next->next;
		ptr2 = ptr2->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return(0);
}
