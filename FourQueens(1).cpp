#include<iostream>
using namespace std;
#define ATTACK 0
#define OK 1
#define N 4

int count=0;      //��¼����Ҫ���ĸ���
int space[N][N];       //����4��4���̿�����
/*int isAttacked(int row,int column,int (*space)[N])
{
	int i,j;
	
	for(i=0;i<column;i++)
		//�ж�ͬһ���Ƿ��лʺ��Ѿ�����
		if(space[row][i]==1)
			return ATTACK;


	for(i=1;row-i>=0,column-i>=0;i++)
		//�ж��Ƿ���ͬһб��
		if(space[row-i][column-j]==1||space[row+i][column-j]==1)
			return ATTACK;
	return OK;
}*/

int isAttacked(int i, int j, int (*Q)[N]) {
    
    int s,t;
    // �ж��� 
    for(s=i,t=0; t<N; t++)
        if(Q[s][t]==1 && t!=j)
            return 0;
            
    // �ж��� 
    for(s=0,t=j; s<N; s++)
        if(Q[s][t]==1 && s!=i)
            return 0;
    
    // �ж����Ͻ�    
    for(s=i-1,t=j-1; s>=0&&t>=0; s--,t--)
        if(Q[s][t]==1)
            return 0;
    
    // ���½� 
    for(s=i+1,t=j+1; s<N&&t<N; s++,t++)
        if(Q[s][t]==1)
            return 0;
    
    // ���Ͻ� 
    for(s=i-1,t=j+1; s>=0&&t<N; s--,t++)
        if(Q[s][t]==1)
            return 0;
            
    // ���½� 
    for(s=i+1,t=j-1; s<N&&t>=0; s++,t--)
        if(Q[s][t]==1)
            return 0;
            
    return 1;
}
void backTrack(int column,int (*space)[N]){
	int i,j;
	if(column==N){
		count++;
		for(i=0;i<N;i++){
			for(j=0;j<N;j++)
				cout<<space[i][j]<<"  ";
			cout<<endl;
		}
		cout<<endl;
	}
	else{
		for(int row=0;row<N;row++){
			if(isAttacked(row,column,space)){
				space[row][column]=1;
				backTrack(column+1,space);
				space[row][column]=0;
			}
		}
	}
}

int main(){

	
	for(int m=0;m<N;m++){
		for(int n=0;n<N;n++){
			space[m][n]=0;
		}
	}

	backTrack(0,space);

	cout<<"����"<<count<<"�ֽ�"<<endl;
	return 0;
}
