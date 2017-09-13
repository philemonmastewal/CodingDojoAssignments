function Node(val){
  this.val = val;
  this.next = null;
}
function SLL(){
  this.head = null;
  this.addFront = function(val){
    var node = new Node(val);
    if(!this.head){    //also if (this.head==null)
      this.head = node;
      return this;
    }
    else{
      node.next = this.head;
      this.head = node;
      return this;    //with this you can chain methods
    }
  }
}

function swapPairs(SLL){
  if(!SLL.head){
    return False;
  }
  var a = SLL.head;
  if(!SLL.head.next){
    return SLL;
  }
  var b = SLL.head.next;
  var c = a;
  while (a && b){
    a.next = b.next;
    b.next = a;
    if(SLL.head == a){
      SLL.head = b;
    }
    if(!a.next){
      break;
    }
    else if (!a.next.next){
      break;
    }
    c = a;
    b = a.next.next;
    a = a.next;
    c.next = b;
  }
  return SLL;
}


var myList = new SLL()
myList.addFront(5).addFront(4).addFront(3).addFront(2).addFront(1)
console.log(swapPairs(myList))
console.log()
