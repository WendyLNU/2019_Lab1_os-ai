package a_star_search;


public class Node {
	  private int x; //x坐标 
	  private int y; //y坐标 
	  private String value;  //表示节点的值 
	  private double FValue = 0; //F值 
	  private double GValue = 0; //G值 
	  private double HValue = 0; //H值 
	  private boolean Reachable; //是否可到达（因为要在地图类设置边界与障碍物） 
	  private Node PNode;   //父节点 
	   
	  public Node(int x, int y, String value, boolean reachable) { 
	    super(); 
	    this.x = x; 
	    this.y = y; 
	    this.value = value; 
	    Reachable = reachable; 
	  } 
	   
		  public Node() {
			super(); 
			this.value="x";

		  }
	 
	  public int getX() { 
	    return x; 
	  } 
	  public void setX(int x) { 
	    this.x = x; 
	  } 
	  public int getY() { 
	    return y; 
	  } 
	  public void setY(int y) { 
	    this.y = y; 
	  } 
	  public String getValue() { 
	    return value; 
	  } 
	  public void setValue(String value) { 
	    this.value = value; 
	  } 
	  public double getFValue() { 
	    return FValue; 
	  } 
	  public void setFValue(double fValue) { 
	    FValue = fValue; 
	  } 
	  public double getGValue() { 
	    return GValue; 
	  } 
	  public void setGValue(double gValue) { 
	    GValue = gValue; 
	  } 
	  public double getHValue() { 
	    return HValue; 
	  } 
	  public void setHValue(double hValue) { 
	    HValue = hValue; 
	  } 
	  public boolean isReachable() { 
	    return Reachable; 
	  } 
	  public void setReachable(boolean reachable) { 
	    Reachable = reachable; 
	  } 
	  public Node getPNode() { 
	    return PNode; 
	  } 
	  public void setPNode(Node pNode) { 
	    PNode = pNode; 
	  }   
}
