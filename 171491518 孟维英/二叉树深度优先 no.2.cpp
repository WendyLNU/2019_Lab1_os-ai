#include "iostream"
#include <stdlib.h>
#include <malloc.h>
#include <stack>
#include <Queue>
using namespace std;
typedef struct Node{
	char data;
	struct Node* lchild;
	struct Node* rchild;
}*Tree;
int index=0;
void treeNodeConstructer (Tree &root,char data[])//建立一个二叉树
{
	char e=data[index++];
	if(e=='#') root=NULL; 
	//如果输入# 则没有孩子（如果没有左孩子，查看其右孩子，如果没有右孩子，则返回上一层（依靠栈来实现））
	else  
		{
			root=(Node *)malloc(sizeof(Node));
			root->data=e;
			treeNodeConstructer(root->lchild,data);
			treeNodeConstructer(root->rchild,data);
	}
}
void DFS (Tree root)//深度优先遍历，依靠栈来实现
{
	stack <Node *>nodeStack;
	nodeStack.push(root);
	Node *node;
	while(!nodeStack.empty()){
		node=nodeStack.top();
		cout<<node->data;
		nodeStack.pop();
		if(node->rchild) nodeStack.push(node->rchild);
		if(node->lchild) nodeStack.push(node->lchild);
	}
}
void BFS(Tree root)//广度优先遍历，依靠队列来实现
{

	queue<Node *> nodeQueue;
	nodeQueue.push(root);
	Node *node;
	while(!nodeQueue.empty())
	{
		node=nodeQueue.front();//返回最早的元素
		nodeQueue.pop();
		cout<<node->data;
		if(node->lchild) nodeQueue.push(node->lchild);
		if(node->rchild) nodeQueue.push(node->rchild);
	}
}
int main(){
	char data[15]={'A','B','D','#','#','E','#','#','C','F','#','#','G','#','#'};
	Tree tree;
	treeNodeConstructer(tree,data);
	cout<<"深度优先遍历的结果是：";
	DFS(tree);
	cout<<endl;
	cout<<"广度优先遍历的结果是：";
	BFS(tree);
	return 0;
}
