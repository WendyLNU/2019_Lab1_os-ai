package a_star_search;
import java.util.*;
public class AStar {
	/** 
	   * 使用ArrayList数组作为“开启列表”和“关闭列表” 
	   * 开启列表装载下一步将要走的结点，而关闭列表装载已经遍历过的结点
	   */
		ArrayList<Node> open = new ArrayList<Node>();
		ArrayList<Node> close = new ArrayList<Node>();
	
		
		
		public double getHValue(Node currentNode,Node endNode){
			return (Math.abs(currentNode.getX() - endNode.getX()) + 
					Math.abs(currentNode.getY() - endNode.getY()))*10;
		}

		public double getGValue(Node currentNode){
			if(currentNode.getPNode()!=null){//当当前节点有父节点是
				if(currentNode.getX()==currentNode.getPNode().getX()||
						currentNode.getY()==currentNode.getPNode().getY()){//水平位置
					//判断当前节点与其父节点之间的位置关系（水平？对角线） 
					return currentNode.getGValue()+10;//对角线位置
				}
				return currentNode.getGValue()+14;
			}
			return currentNode.getGValue();
		}

		public double getFValue(Node currentNode){
			return currentNode.getGValue()+currentNode.getHValue();
		}
		//将结点加入开启列表
		public void inOpen(Node node,Map map){
			int x = node.getX();
			int y = node.getY();
			for (int i = 0;i<3;i++){
				for (int j = 0;j<3;j++){
					//判断条件为：节点为可到达的（即不是障碍物，不在关闭列表中）
					//开启列表中不包含，不是选中节点 
					if(map.getMap()[x-1+i][y-1+j].isReachable()&&
							 !open.contains(map.getMap()[x-1+i][y-1+j])&&!(x==(x-1+i)&&y==(y-1+j))){
						map.getMap()[x-1+i][y-1+j].setPNode(map.getMap()[x][y]);
						//将选中节点作为父节点 
						map.getMap()[x-1+i][y-1+j].setGValue(getGValue(map.getMap()[x-1+i][y-1+j]));
						map.getMap()[x-1+i][y-1+j].
						setHValue(getHValue(map.getMap()[x-1+i][y-1+j],map.getEndNode()));
						map.getMap()[x-1+i][y-1+j].setFValue(getFValue(map.getMap()[x-1+i][y-1+j]));
						open.add(map.getMap()[x-1+i][y-1+j]);//求得合格点的fgh值并把点列入open列表
					}
				}
			}
		}
		//将对一个数列里的结点进行冒泡排序
		public void sort(ArrayList<Node> arr){
			for (int i = 0;i<arr.size()-1;i++){
				for (int j = i+1;j<arr.size();j++){
					if(arr.get(i).getFValue() > arr.get(j).getFValue()){
						Node tmp = new Node();
						tmp = arr.get(i);
						arr.set(i, arr.get(j));
						arr.set(j, tmp);
					}
				}
			}
		}
		//将结点放入关闭列表
		public void inClose(Node node,ArrayList<Node> open){
			if(open.contains(node)){//如果open表中含有该点
				node.setReachable(false);
				//设置为不可达 
				open.remove(node);
				close.add(node);
			}
		}
		public void search(Map map){
			//对起点及起点周围的节点进行操作 
			inOpen(map.getMap()[map.getStartNode().getX()][map.getStartNode().getY()],map);
			//那一长串是起点A
			close.add(map.getMap()[map.getStartNode().getX()][map.getStartNode().getY()]);
			//将起点A加入close表
			map.getMap()[map.getStartNode().getX()][map.getStartNode().getY()].setReachable(false);
			map.getMap()[map.getStartNode().getX()][map.getStartNode().getY()].
			setPNode(map.getMap()[map.getStartNode().getX()][map.getStartNode().getY()]);
			sort(open);
			//重复步骤 
			do{
				inOpen(open.get(0), map);
				inClose(open.get(0), open);
				sort(open);
			}
			while(!open.contains(map.getMap()[map.getEndNode().getX()][map.getEndNode().getY()]));
			//知道开启列表中包含终点B时，退出循环
			inClose(map.getMap()[map.getEndNode().getX()][map.getEndNode().getY()], open);
			//将结束点放入close表
			showPath(close,map);
		}
		//将路径表示出来的函数
		public void showPath(ArrayList<Node> arr,Map map) {
			if(arr.size()>0){
				for(int i=0;i<arr.size();i++) {
					arr.get(i).setValue("x");
				}
			}
		}
}