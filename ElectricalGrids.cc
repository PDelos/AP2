#include <bits/stdc++.h>
using namespace std;


int bfs(int s, int t, vector<int>& p,  vector<vector<int>>&adj, vector<vector<int>>&capacity) {
    fill(p.begin(), p.end(), -1);
    p[s] = -2;
    queue<pair<int, int>> q;
    q.push({s, 1e9});

    while (!q.empty()) {
        int cur = q.front().first;
        int flow = q.front().second;
        q.pop();

        for (int next : adj[cur]) {
            if (p[next] == -1 && capacity[cur][next]) {
                p[next] = cur;
                int new_flow = min(flow, capacity[cur][next]);
                if (next == t) return new_flow;
                q.push({next, new_flow});
            }
        }
    }

    return 0;
}

int maxflow(int s, int t, vector<vector<int>>&adj, vector<vector<int>>&capacity) {
    int flow = 0;
    vector<int> p(adj.size());
    int new_flow;

    while (new_flow = bfs(s, t, p, adj, capacity)) {
        flow += new_flow;
        int cur = t;
        while (cur != s) {
            int prev = p[cur];
            capacity[prev][cur] -= new_flow;
            capacity[cur][prev] += new_flow;
            cur = prev;
        }
    }

    return flow;
}

int main() {
	int n, m;
	while(cin >> n >> m){

		vector<vector<int>> capacity(n, vector<int>(n));
		vector<vector<int>> adj(n);
		for(int i = 0; i < m; ++i) {
			int a, b, c;
			cin >> a >> b >> c;
			adj[a].push_back(b);
			adj[b].push_back(a);
			capacity[a][b] += c;
		}
		cout << maxflow(0, n-1, adj, capacity) << endl;
	}
}
