#include <stdlib.h>
#include "lists.h"

/**
 * delete_dnodeint_at_index - deletes the node at index of a dlistint_t list
 * @head: pointer to pointer of the head
 * @index: index of the node to delete (starting at 0)
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *node;
	unsigned int i;

	if (head == NULL || *head == NULL)
		return (-1);
	node = *head;
	i = 0;
	while (i < index)
	{
		if (node->next == NULL)
			return (-1);
		node = node->next;
		i++;
	}
	if (node == *head)
	{
		*head = node->next;
		if (*head != NULL)
		{
			(*head)->prev->next = (*head)->next;
			(*head)->prev = node->prev;
		}
	}
	else
	{
		node->prev->next = node->next;
		if (node->next != NULL)
			node->next->prev = node->prev;
	}
	free(node);
	return (1);
}
