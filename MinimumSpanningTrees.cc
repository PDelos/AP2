#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> iPair;

int find(int x, vector<int>&link) {
	while (x != link[x]) x = link[x];
	return x;
}

bool same(int a, int b, vector<int>&link) {
	return find(a, link) == find(b, link);
}

void unite(int a, int b, vector<int>&link, vector<int>&size) {
	a = find(a, link);
	b = find(b, link);
	if (size[a] < size[b]) swap(a,b);
	size[a] += size[b];
	link[b] = a;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	int n, m;
	while(cin >> n >> m){
		vector<pair<int, iPair>>edges(m);

		for (int i = 0; i < m; i++){
			int x, y, w;
			cin >> x >> y >> w;
			edges[i] = {w, {x, y}};
		}

		sort(begin(edges), end(edges));

		vector<int>link(n+1);
		vector<int>size(n+1);
		for (int i = 1; i <= n; i++) link[i] = i;
		for (int i = 1; i <= n; i++) size[i] = 1;

		int sol = 0;
		for (int i = 0; i < m; ++i) {
			int a = edges[i].second.first, b = edges[i].second.second;
			int w = edges[i].first;
			if (!same(a,b, link)) unite(a,b, link, size), sol+=w;
		}
		cout << sol << endl;

	}
	
}
