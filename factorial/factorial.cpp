#include <iostream>
using namespace std;

int main()
{
    int factonial(int);
    int n;
    cout << "Enter the nnumber to factorial";
    cin >> n;

    int fact = factorial(n);
    return 0;
}

int factonial(int n)
{
    if (n >= 1)
    {
        return (n * factorial(n - 1));
    }
    else
    {
        return 1;
    }
}