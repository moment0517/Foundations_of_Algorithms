#include <iostream>
#include <cassert>

using namespace std;

int arr[] = {3, 1, 10, 5, 7, 4};
int n = 6;

int find_kth_smallest(int low, int high, int k)
{
    assert(low <= k && k <= high);
    int pivot = low;
    int i = low, j = low + 1;
    int tmp;
    while (j <= high)
    {
        if (arr[j] < arr[pivot])
        {
            i++;
            if (i != j)
            {
                tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
        j++;
    }
    tmp = arr[pivot];
    arr[pivot] = arr[i];
    arr[i] = tmp;
    if (i == k)
    {
        return arr[i];
    }
    else if (i > k)
    {
        return find_kth_smallest(0, i - 1, k);
    }
    else
    {
        return find_kth_smallest(i + 1, n - 1, k);
    }
}

int main()
{
    int res = find_kth_smallest(0, n - 1, 3);
    cout << res << endl;
}
