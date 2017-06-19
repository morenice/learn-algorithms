#include <stdio.h>
#include <stdlib.h>

 // 오름차순
int compare (const void *first, const void *second)
{
	if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}


void qsort_sample()
{
    int arr[] = {4,3,1,7,5,9,8,2,6};
    int arr_size = sizeof(arr) / sizeof(int);
    int i;

    // before sort
    for (i = 0; i < arr_size; i++)
        printf("%d ", arr[i]); printf("\n");

    // apply quick sort
    qsort(arr, arr_size, sizeof(int), compare);

    // after sort
    for (i = 0; i < arr_size; i++)
        printf("%d ", arr[i]); printf("\n");
}


int main(int argc, char** argv)
{
    int *arr = NULL;
    int arr_size = -1;
    int i = 0;

    scanf("%d", &arr_size);
    if (arr_size <= 0)
    {
        return 0;
    }

    arr = (int*) malloc(sizeof(int)*arr_size);
    for (i=0; i < arr_size; i++)
    {
        scanf("%d", &arr[i]);
    }

    // apply quick sort
    qsort(arr, arr_size, sizeof(int), compare);

    // after sort
    for (i = 0; i < arr_size; i++)
        printf("%d\n", arr[i]);

    free(arr);
    return 0;
}
