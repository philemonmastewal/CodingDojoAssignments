function Node(val){
  this.val = val
  this.next = null
}
function SLL(){
  this.head = null
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
  this.removeNegatives = function(){
    if(!this.head){
      return False;
    }
    var current = this.head;
    while(this.head){
      if (this.head.val<0){
        this.head=this.head.next;
      }
      else{
        break;
      }
    }
    while(current.next){
      if(current.next.val<0){
        current.next=current.next.next;
      }
      while(current.next.val<0){
        current.next=current.next.next;
        if(!current.next){
          return this;
        }
        current=current.next;
      }
    }
    return this;

  }
}
var myList = new SLL()  //this is how you create a new list by running the function new SLL
  //this will display an object- a new SLL
myList.addFront(5).addFront(-1).addFront(-3).addFront(-2) //chained methods because we used return this
console.log(myList)
myList.removeNegatives()
console.log(myList)

//
// function SLL(){
//   this.head = null
//   this.removeNegatives = function(){
//     if(!this.head){
//       return False;
//     }
//     var current = this.head;
//     if (this.head.val<0){
//       this.head=current.next;
//     }
//     while(current){
//       if(current.next.val<0){
//         current.next=current.next.next;
//       }
//       else{
//         current=current.next;
//       }
//     }
//     return this;
//   }
// }
//   var myList = new SLL()  //this is how you create a new list by running the function new SLL
//   console.log(myList)  //this will display an object- a new SLL
//   myList.addFront(4).addFront(5).addFront([10,11,12]) //chained methods because we used return this
//   console.log(myList)



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
