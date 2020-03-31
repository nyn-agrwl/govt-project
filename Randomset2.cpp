#include <iostream>
#include <vector>
#include <time.h>
using namespace std;

int RandomSet1(int stringLength,vector<int>& V,int sum=0){
    int temp;
    int randomNumber= rand()%4+1;
    if((randomNumber+sum)==stringLength){
        return randomNumber;
    }else if((randomNumber+sum)>stringLength){
        for(int i=1;i<randomNumber;i++){
            if(i+sum==stringLength){
                return i;
            }
        }
    }else{
        sum=sum+randomNumber;
        V.push_back(randomNumber);
        temp=RandomSet1(stringLength,V,sum);
        return temp;
    }
    V.push_back(temp);
}

int main(){
    srand (time(NULL));
    vector<int> V;
    for(int i=0;i<20;i++){
        RandomSet1(11,V);
        for(int a:V){
            cout<<a<<" ";
        }
        cout<<endl;
        V.clear();
    }


}
