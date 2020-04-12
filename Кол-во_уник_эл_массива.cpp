#include <iostream>
//#include <iomanip>
//#include <cmath>

using namespace std;

int main()
{
    const int SIZE = 100;
    int a[SIZE] = {};

    int n;
    cin >> n;

    // заполняем массив
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    // выполняем задание
    int cnt_uniq = 0;
    bool uniq = true;

    for (int i = 0; i < n-1; i++)
    {
        for (int j = i+1; j < n; j++)
        {
            if (a[i] == a[j])
                uniq = false;
        }

        if (uniq)
            cnt_uniq++;

        uniq = true;
    }

    cout << cnt_uniq + 1;

    return 0;
}
