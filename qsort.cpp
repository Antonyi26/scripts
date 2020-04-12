#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

// 3 4 7 8 11 [12] 19 16
// 3 4 [7] 8 11 [12] 16 [19]

void QSort(int *a, int l, int r) {
    int i = l, j = r;
    int x = a[(l+r)/2]; // опорный элемент
    while(i <= j) {
        while (a[i] < x) ++i;
        while (a[j] > x) --j;
        if (i <= j) {
            int tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
            ++i;
            --j;
        }
    }
    if (l < j) QSort(a, l, j); // рекурсивная часть
    if (i < r) QSort(a, i, r);
}

int main() {
    int n = 8;
    int data[] = { 3, 4, 7, 12, 19, 11, 8, 16};
    QSort(data, 0, n-1);
    for (int i = 0; i < n; ++i)
        cout << data[i] << " ";
    return 0;
}
