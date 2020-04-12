#include <iostream>
// -----------------------------------------------------
using namespace std;
// -----------------------------------------------------
void printDesk(bool **desk, int n)
{
    cout << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << desk[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}
// -----------------------------------------------------
void clearDesk(bool **desk, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            desk[i][j] = 0;
        }
    }
}
// -----------------------------------------------------
void clearRowDesk(bool **desk, int n, int row)
{
    for (int j = 0; j < n; j++)
    {
        desk[row][j] = 0;
    }
}
// -----------------------------------------------------
bool isNotAttacked(bool **desk, int n, int _i, int _j)
{
    if (desk[_i][_j] == 1)
        return false;
    // по вертикали
    for (int i = 0; i < n; i++)
    {
        if ( desk[i][_j] == 1)
            return false;
    }
    // по горизонтали
    for (int j = 0; j < n; j++)
    {
        if ( desk[_i][j] == 1)
            return false;
    }

    // по главной диагонали
    {
        int i = _i - 1;
        int j = _j - 1;

        while (i >= 0 && j >= 0)
        {
            if ( desk[i][j] == 1)
                return false;
            i -= 1;
            j -= 1;
        }

        i = _i + 1;
        j = _j + 1;

        while (i < n && j < n)
        {
            if (desk[i][j] == 1)
                return false;
            i += 1;
            j += 1;
        }
    }
    // по обратной диагонали
    {
        int i = _i + 1;
        int j = _j - 1;

        while (i < n && j >= 0)
        {
            if (desk[i][j] == 1)
                return false;
            i += 1;
            j -= 1;
        }

        i = _i - 1;
        j = _j + 1;

        while (i >= 0 && j < n)
        {
            if (desk[i][j] == 1)
                return false;
            i -= 1;
            j += 1;
        }
    }

    return true;
}
// -----------------------------------------------------
int placeQueenOnDesk(bool **desk, int n, int row, int startCol)
{
    int placeInCol = -1;

    for (int col = startCol+1; col < n; col++)
    {
        if ( isNotAttacked(desk, n, row, col) )
        {
            desk[row][col] = 1;
            placeInCol = col;
            break;
        }
    }

    return placeInCol;
}
// -----------------------------------------------------
int queensOnDesk(bool **desk, int n)
{
    int cnt = 0;
    int *cols = new int[n]{};
    for (int i = 0; i < n; i++)
        cols[i] = -1;

    for (int row = 0; row < n;)
    {
        cols[row] = placeQueenOnDesk(desk, n, row, cols[row]);

        if (cols[row] == -1)
        {
            if (row == 0) break;
            row--;
            clearRowDesk(desk, n, row);
            continue;
        }
        else
        {
            if (row == n-1)
            {
                cnt++;
                clearRowDesk(desk, n, row);
            }
            else
            {
                row++;
            }
        }
    }
    delete [] cols;

    return cnt;
}
// -----------------------------------------------------
int queensOnDeskRecursive(bool **desk, int n)
{

}
// -----------------------------------------------------
int main()
{
    int n;
    cin >> n;
    // --- выделяем память
    bool **desk = new bool *[n];
    for (int i = 0; i < n; i++)
        desk[i] = new bool[n]{};
    // -------------------------

    //int cnt = queensOnDesk(desk, n);
    int cnt = queensOnDeskRecursive(desk, n);
    //printDesk(desk, n);
    cout << "cnt = " << cnt << endl;

    // --- освобождаем память
    for (int i = 0; i < n; i++)
        delete [] desk[i];
    delete [] desk;
    // -------------------------
    return 0;
}
