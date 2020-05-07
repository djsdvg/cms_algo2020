#include <iostream>
#include <climits>

using namespace std;

const int NMAX=1000;

int m[NMAX][NMAX];
int col[NMAX];

int main()
{
  int i,j,k,min,a,n;
  cin>>n;
  for(i=0;i<n;i++)
    {
      cin>>col[i];
      m[0][i]=1;
    }
  for(i=1;i<n;i++)
      for(j=0;j<n-i;j++)
	{
	  min=INT_MAX;

	  for(k=1;k<=i;k++)
	    if ((a=(m[k-1][j]+m[i-k][j+k]-((col[j]==col[j+i])?1:0)))<min)
	      min=a;
	  m[i][j]=min;
	}
  cout<<m[n-1][0]<<endl;
}
