#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
    listint_t *this_node, *that_node;

    this_node = list;
    that_node = list;

    while (this_node && that_node)
    {
        if(that_node->next == NULL)
            return (0);

        this_node = this_node->next;
        that_node = that_node->next->next;

        if(this_node == that_node)
            return (1);
    }
    return (0);
}