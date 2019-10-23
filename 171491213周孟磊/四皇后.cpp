#include<bits/stdc++.h>

using namespace std;
#define debug(x) cout<<#x<<" is "<<x<<endl;
typedef long long ll;

const int maxn=1e2+5;

int ans,ac[maxn];
bool vis[maxn],vis2[maxn],vis3[maxn];

void dfs(int x){
    if(x==5){
        ans++;
        for(int i=1;i<=4;i++)printf("%d ",ac[i]);
        printf("\n");
        return;
    }
    for(int i=1;i<=4;i++){
        if(vis[i]||vis2[x+i]||vis3[x-i+10])continue;
        vis[i]=vis2[x+i]=vis3[x-i+10]=1;
        ac[x]=i;
        dfs(x+1);
        vis[i]=vis2[x+i]=vis3[x-i+10]=0;
    }
}

int main(){
    dfs(1);
    printf("%d\n",ans);
    return 0;
}
