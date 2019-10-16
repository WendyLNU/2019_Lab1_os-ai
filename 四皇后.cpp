#include<cstdio>
#include<iostream>
using namespace std;
int ans;//ans是可行的方案数 
int lie[10];
int le[10];
int ri[10];
int aaa[5][5];
void dfs(int t)
{
	if(t==5){
		ans++;
		printf("第%d种:\n",ans); 
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++)
				printf("%d ",aaa[i][j]);
			printf("\n\n");
		}

		return;
	}	
	for(int i=1;i<=4;i++){
		if(lie[i]==0&&le[t+i]==0&&ri[t-i+5]==0){
			lie[i]=1;
			le[t+i]=1;
			ri[t-i+5]=1;
			aaa[t][i]=1;
			dfs(t+1);
			aaa[t][i]=0;
			lie[i]=0;
			le[t+i]=0;
			ri[t-i+5]=0;
		}	
	}
}
int main()
{
	dfs(1);
	printf("方案数 ：%d\n",ans); 
	return 0;
}
