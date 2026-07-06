class LRUCache {

    class Node
    {
        Node prev;
        Node next;
        int key;
        int val;

        public Node(int key, int val)
        {
            this.key = key;
            this.val = val;
        }
    }

    int capacity;
    Node head = new Node(-1,-1);
    Node tail = new Node(-1,-1);
    HashMap<Integer, Node> map = new HashMap<>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.head.next = tail;
        this.tail.prev = head;
    }

    public void addFront(Node n)
    {
        //prev is now null
        n.prev = head;
        //next node should be current head
        n.next = head.next;
        //head prev should be new head
        n.next.prev = n;
        head.next = n;

    }
    public void remove(Node n)
    {

        n.prev.next = n.next;
        n.next.prev = n.prev;

        
    }
    public int get(int key) {
        Node n = map.get(key);
        if(n == null)
        {
            return -1;
        }
        else
        {
            this.remove(n);
            this.addFront(n);
            return n.val;
        }
    }
    
    public void put(int key, int value) {
        Node n = map.get(key);
        if (n == null)
        {
            n = new Node(key, value);
            if(map.size()<capacity)
            {
                map.put(key,n);
                this.addFront(n);
            }
            else
            {
                map.remove(tail.prev.key);
                this.remove(tail.prev);
                map.put(key,n);
                this.addFront(n);
            }
        }
        else
        {
            this.remove(n);
            n.val = value;
            this.addFront(n);
            

        }
    }
}
