#include <iostream>
#include <list>
#include <iomanip>
//#include <cmath>

using namespace std;
// -----------------------------------
class Element
{
public:
    int weight = 0;
    int cost = 0;
    double costPerWeight = 0;

    Element(int c, int w)
    {
        weight = w;
        cost = c;
        costPerWeight = (double)c / w;
    }
};
// -----------------------------------
bool operator < (const Element &first, const Element &second)
{
    return (second.costPerWeight < first.costPerWeight);
}
// -----------------------------------
int main()
{
    double maxCost = 0;
    int n, maxWeight;
    cin >> n >> maxWeight;

    list<Element> myList;

    for (int i = 0; i < n; i++)
    {
        int cost, weight;
        cin >> weight >> cost;
        myList.push_back( Element(cost, weight) );
    }

    myList.sort();

    for (auto iter = myList.begin(); iter != myList.end(); iter++)
    {
        if (!maxWeight) break;

        if( iter->weight <= maxWeight )
        {
            maxCost += iter->cost;
            maxWeight -= iter->weight;
        }
        else
        {
            maxCost += iter->costPerWeight * maxWeight;
            maxWeight = 0;
        }
    }


    cout << fixed << setprecision(3) << maxCost << endl;

    return 0;
}
