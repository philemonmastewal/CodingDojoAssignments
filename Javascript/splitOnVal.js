function ListNode(){
  this.val = value;
  this.next = null;
}
function SLL(){
  this.head = null;
  this.addFront = function(val){
    if(!this.head){
      this.head = new Node(val);
      return this
    }
    var node = new Node(val);
    node.next = this.head;
    this.head = node;
    return this;

  }
  this.splitOnVal = function (List, num){
    var current = this.head;
    if(!this.head){
      return False;
    }
    if (this.head.val == num){
      console.log("num is at Begginning of List");
      return List;
    }
    while(current.next){
      current = current.next;
      if(current.next.val == num){
        List.head = current.next;
        current.next = null;
        break;
      }
      var list = new SLL();
      list.head = temp;
      return list.head;
    }
  }
}
var list = new SLL()

list.addFront(1)
list.addFront(2)
list.addFront(3)
list.addFront(4)
list.addFront(5)
