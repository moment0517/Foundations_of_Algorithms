#include <queue>
#include <iostream>

using namespace std;

struct Node
{
    Node() {}
    Node(int v) : next(NULL), value(v) {}
    int value;
    Node *next;
};

void find_second_largest(int *arr, int n, int &second_largest)
{
    queue<Node *> tour;
    for (int i = 0; i < n; i++)
        tour.push(new Node(arr[i]));

    while (tour.size() > 1)
    {
        Node *v1 = tour.front();
        tour.pop();
        Node *v2 = tour.front();
        tour.pop();
        Node *tmp = new Node;
        if (v1->value > v2->value)
        {
            tmp->value = v2->value;
            tmp->next = v1->next;
            v1->next = tmp;
            tour.push(v1);
        }
        else
        {
            tmp->value = v1->value;
            tmp->next = v2->next;
            v2->next = tmp;
            tour.push(v2);
        }
    }
    Node *largest_node = tour.front();
    cout << "largest: " << largest_node->value << endl;

    Node *next_node = largest_node->next;
    second_largest = next_node->value;
    while (next_node->next)
    {
        next_node = next_node->next;
        if (next_node->value > second_largest)
            second_largest = next_node->value;
    }
    cout << "second largest: " << second_largest << endl;
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    int second_largest{};
    find_second_largest(arr, 5, second_largest);
}
