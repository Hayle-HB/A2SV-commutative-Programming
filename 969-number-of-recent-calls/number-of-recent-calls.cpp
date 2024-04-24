class RecentCounter {
public:
    queue<int>q;
    
    int ping(int t) {
        int ti=t-3000;
        q.push(t);
        while(q.front()<ti)
            q.pop();
        return q.size();
    }
};

