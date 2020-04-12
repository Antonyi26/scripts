#include <iostream>
//#include <iomanip>
//#include <cmath>

using namespace std;

int main()
{
    const int SIZE = 50;
    int a[SIZE] = {};

    int n;
    cin >> n;

    // инициализация массива
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    bool ok = false; // флаг отсортированности массива
    int len = n;

    while (!ok)
    {
        ok = true;

        for (int i = 1; i < len; i++)
        {
            if (a[i-1] > a[i])
            {
                int tmp = a[i-1];
                a[i-1] = a[i];
                a[i] = tmp;

                ok = false;
            }
        }

        len--;
    }


    // результат
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }

    return 0;
}
