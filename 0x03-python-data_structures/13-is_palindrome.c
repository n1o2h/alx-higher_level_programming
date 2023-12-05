#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - a function that checks if a linked list is a palindrome.
 * @head: the header
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *palindrome;
	int len = 0, i, j;

	if (head == NULL || *head == NULL)
		return (1);
	current = *head;
	while (current)
	{
		current = current->next;
		len++;
	}
	current = *head;
	palindrome = *head;
	for (i = 0; i < len / 2; i++)
	{
		for (j = 1; j < len - i; j++)
			palindrome = palindrome->next;
		if (current->n != palindrome->n)
			return (0);
		palindrome = *head;
		current = current->next;
	}
	return (1);
}
