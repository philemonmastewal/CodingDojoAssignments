function SLStack(){

}

function top(stack){

}

function copyThat(stack){
  var temp = new Stack;
  var duplicateStack = new Stack;
   while(stack.top()){//we can also use stack.pop because .pop returns first val
    temp.push(stack.top());
    stack.pop();
  }
  while(temp.top()){
    duplicateStack.push(temp.top());
    stack.push(temp.top());
    temp.pop();
  }
  return duplicateStack;
}
