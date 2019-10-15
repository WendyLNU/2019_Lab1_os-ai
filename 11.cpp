/*
#include <iostream>
#include <climits>

using namespace std;
int book[101] = {0}, sum, n, m, e[101][101] = {0};

void dfs(int cur) {
    cout << cur << " ";
    sum++;
    if (sum == n)return;
    for (int i = 1; i <= n; i++) {  //ѭ���ﵽ���ݵ�Ч��
        if (book[i] == 0 && e[cur][i] == 1) {
            book[i] = 1;
            dfs(i);
        }
    }
    return;
}

int main(int argc, const char *argv[]) {
    cin >> n >> m;  //n���ڵ㣬m����
    for (int i = 1; i <= n; i++)    //��ʼ��
        for (int j = 1; j <= n; j++) {
            if (i == j)
                e[i][j] = 0;
            else
                e[i][j] = INT_MAX;
        }
    int a, b;
    for (int k = 1; k <= m; k++) {  //�����ʾ
        cin >> a >> b;
        e[a][b] = 1;
        e[b][a] = 1;
    }
    book[1] = 1;
    dfs(1);

    return 0;
}
*/
#include <iostream>
#include <climits>

using namespace std;

int main() {
    int i,n, m, a, b, cur, book[101] = {0}, e[101][101] = {0};
    int que[101], head = 1, tail = 1;

    cin >> n >> m; //n���ڵ㣬m����
    for (  i = 1; i <= n; i++)   //��ʼ��
        for (int j = 1; j <= n; j++) {
            if (i == j)
                e[i][j] = 0;
            else
                e[i][j] = INT_MAX;
        }
    for (i = 1; i <= m; i++) {  //ͼ�ľ����ʾ
        cin >> a >> b;
        e[a][b] = 1;
        e[b][a] = 1;
    }

    que[1] = 1;
    tail++;
    book[1] = 1;  //�߹��ı��Ϊ1
    while (head < tail) {
        cur = que[head];
        for ( i = 1; i <= n; i++) { //��ǰ�������µ����п��ܶ��浽������ȥ
            if (book[i] == 0 && e[cur][i] == 1) {
                que[tail] = i;
                tail++;
            }
            if (tail > n)
                break;
        }
        head++; //��ʾ��ǰ������������¸���
    }

    for ( i = 1; i <= n; i++) {
        cout << que[i] << " ";
    }

    return 0;
}