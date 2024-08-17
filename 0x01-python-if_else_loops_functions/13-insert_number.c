#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list */
typedef struct x_s
{
    int n;
    struct x_s *next;
} x_t;

x_t *insert_node(x_t **head, int number)
{
    x_t *new_node, *current;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(x_t));
    if (new_node == NULL)
        return NULL;

    new_node->n = number;
    new_node->next = NULL;

    /* Special case: Insert at the head of the list */
    if (*head == NULL || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    /* Traverse the list to find the correct insertion point */
    current = *head;
    while (current->next != NULL && current->next->n < number)
    {
        current = current->next;
    }

    /* Insert the new node */
    new_node->next = current->next;
    current->next = new_node;

    return new_node;
}
