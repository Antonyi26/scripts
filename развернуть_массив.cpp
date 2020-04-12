#include <iostream>
//#include <iomanip>
//#include <cmath>

using namespace std;

int main()
{
    const int SIZE = 15;
    int a[SIZE] = {};

    int n = SIZE;
    //cin >> n;

    // заполняем массив
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    int k, s;
    cin >> k >> s;

    // перевод элементов в индексы
    k = k - 1;
    s = s - 1;

    // разворачисаем массив
    for (int i = k + 1, j = s - 1; i < j; i++, j--)
    {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }

    // выходные данные
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }


    return 0;
}
