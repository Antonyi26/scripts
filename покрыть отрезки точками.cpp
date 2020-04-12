#include <iostream>
#include <list>
//#include <iomanip>
//#include <cmath>

using namespace std;
// -----------------------------------
class Line
{
public:
    int begin = 0, end = 0;

    Line(int start, int fin)
    {
        begin = start;
        end = fin;
    }

    bool dotsOnLine(const int dot)
    {
        return (dot >= begin && dot <= end);
    }
};
// -----------------------------------
bool operator < (const Line &first, const Line &second)
{
    return (first.end < second.end);
}
// -----------------------------------
int main()
{
    int n;
    cin >> n;

    list<Line> myList;

    for (int i = 0; i < n; i++)
    {
        int x1, x2;
        cin >> x1 >> x2;
        Line newLine(x1, x2);
        myList.push_back(newLine);
    }

    myList.sort();

    list<int> dotsList;
    dotsList.push_back( myList.front().end );

    for (auto iter = myList.begin(); iter != myList.end(); iter++)
    {
        if ( iter->dotsOnLine(dotsList.back()) )
            continue;
        else
            dotsList.push_back( iter->end );
    }

    // вывод результата
    cout << dotsList.size() << endl;
    
    for (auto iter = dotsList.begin(); iter != dotsList.end(); iter++)
        cout << *iter << " ";

    return 0;
}
