#include <bits/stdc++.h>
#define pb push_back
using namespace std;



int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	int n, m;
	while(cin >> n >> m){
		vector<vector<pair<int , int>>>adj(n);
		vector<int>distance(n, 1e8+3);
		vector<bool>processed(n);
		vector<int>parent(n, -1);

		for(int i = 0; i < m; ++i){
			int x, y, c;
			cin >> x >> y >> c;
			adj[x].push_back({y, c});
		}

		priority_queue<pair<int, int>>q;
		int start, end;
		cin >> start >> end;

		distance[start] = 0;
		q.push({0, start});
		while(!q.empty() and !processed[end]){
			int a = q.top().second; q.pop();
			if(processed[a]) continue;
			processed[a] = true;
			for(auto u : adj[a]){
				int b = u.first, w = u.second;
				if(distance[a]+w < distance[b]){
					distance[b] = distance[a]+w;
					q.push({-distance[b], b});
					parent[b] = a;
				}
			}
		}


		if(distance[end] < 1e8+3){
			vector<int> res;
	    	res.push_back(end);
	   		int temp = end;
	    	while (temp != start){
	        	temp = parent[temp];
	      		res.push_back(temp);
	    	}
	    	cout << res[res.size()-1];
	    	for(int i = res.size()-2; i >= 0; --i) cout << " " << res[i];
	    	cout << endl;
		}
		else{
			cout << "no path from " << start << " to " << end << endl;
		}

	}
	
}
