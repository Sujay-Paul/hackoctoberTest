#include<iostream>
using namespace std;

int main() {

    int i,j=1;

    cout<<"Enter the Number Table you want: ";
    cin>>i;

    cout<<"\n";

    do {
        cout<<i<<" X "<<j<<" = "<<i*j<<endl;
        j++;
    }while(j<=10);
    
    return 0;
}