#include <iostream>
// ----------------------------
using namespace std;
// ----------------------------
int** newMemFor2dArr(int rows, int columns)
{
    int **arr = new int *[rows];
    for (int i = 0; i < rows; i++)
        arr[i] = new int[columns];

    return arr;
}
// ----------------------------
void freeMemFrom2dArr(int **a, int rows)
{
    for (int i = 0; i < rows; i++)
        delete [] a[i];
    delete [] a;
}
// ----------------------------
void init2dArr(int **a, int rows, int columns)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            a[i][j] = i+1;
        }
    }
}
// ----------------------------
void printArr(int **a, int rows, int columns)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}
// ----------------------------
int main()
{
    int n;
    cin >> n;
    int rows = n;
    int columns = n;

    int **arr = newMemFor2dArr(rows, columns);

    init2dArr(arr, rows, columns);
    printArr(arr, rows, columns);

    freeMemFrom2dArr(arr, rows);

    return 0;
}
