cppCode="""
#include<iostream>
using namespace std;
int main()
{
    cout<<"Hello World!";
    return 0;
}
    
"""
print(cppCode)
print(type(cppCode))
file = open("G:\TV Series\Friends\Season 01\MyApp.txt","w")
file.write(cppCode)
print("Write done")