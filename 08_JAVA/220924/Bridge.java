import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Bridge {
	static int n,result=10000,length;
	static int[][] graph;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	
	public static void make_land(int x, int y, int landnum) {
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] {x, y});
		graph[x][y] = landnum;
		while(!queue.isEmpty()) {
			int tempX = queue.peek()[0];
			int tempY = queue.peek()[1];
			queue.poll();
			for(int i=0; i < 4; i++) {
				int nX = tempX + dx[i];
				int nY = tempY + dy[i];
				if(nX>=0 & nX<n & nY>=0 & nY<n){
					if(graph[nX][nY]==1) {
						graph[nX][nY] = landnum;
						queue.add(new int[] {nX,nY});
					}
				}
			}
		}
	}
	
	public static int make_bridge(int x, int y, int landnum,int cnt) {
		int[] visited = new int[n*n];

		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] {x, y, cnt});
		visited[x*n+y] = 1;
		int find = 0;
		while(!queue.isEmpty()) {
			int tempX = queue.peek()[0];
			int tempY = queue.peek()[1];
			int ncnt = queue.peek()[2];
			queue.poll();
			if (ncnt>result){
				return 0;
			}
			for(int i=0; i<4; i++) {
				int nX = tempX + dx[i];
				int nY = tempY + dy[i];
				if(nX>=0 & nX<n & nY>=0 & nY<n) {
					if(graph[nX][nY]!=landnum) {
						if(visited[nX*n+nY]==0) {
						queue.add(new int[] {nX,nY,ncnt+1});
						visited[nX*n+nY] = 1;
						if(graph[nX][nY]!=0) {
							find = 1;
							}
						}
					}
				}
			if(find==1)
				return ncnt;
			}
		}
		return 0;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		graph = new int[n][n];
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				graph[i][j] = sc.nextInt();
			}
		}
		int land = 2;
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(graph[i][j] == 1) {
					make_land(i,j,land);
					land += 1;
				}
			}
		}
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(graph[i][j]!=0) 
					length = make_bridge(i,j,graph[i][j],0);
				if(length!=0) {
					if(length<result)
					result = length;
				}
			}
		}
		System.out.print(result);
	}
}
