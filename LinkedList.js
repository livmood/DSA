import {Node} from "./Node.js";

class LinkedList {
  constructor(value) {
    const newNode = new Node(value);
    this.head = newNode;
    this.tail = this.head;
    this.length = 1;
  }

  //DONE: push function (given a value, add a new node to end of list)
  push(value) {
    if(this.head === null) {
      this.constructor(value);
      return;
    }
    const newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
  }

  //DONE: pop function (removes and returns node at end of list) //remember to consider edge cases: what if there's only one node?
  pop() {
    if(this.length === 0) return console.error("Linked List is already empty");
    if(this.length === 1) {
      let result = this.head.value;
      this.tail = null;
      this.head = null;
      this.length--;
      return result;
    }
    let temp = this.head;
    while(temp.next !== this.tail) {
      temp = temp.next;
    }
    let returnValue = this.tail.value;
    this.tail = temp;
    this.tail.next = null;
    this.length--;
    return returnValue;
  }

  //DONE: unshift function (given a value, add a new node to begining of list)
  unshift(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
  }

  //TODO: shift function (removes and returns node at beginning of list)
  shift() {
    if(this.length === 0) return console.error("Linked List is already empty");
    let headVal = this.head.value;
    this.head = this.head.next;
    this.length--;
    return headVal;
  }

  //TODO: get function (given an index, return the node at that index)
  //TODO: set function (given an index and a value, set the node at that index to the value)
  //TODO: print function (prints the entire linked list)
  //TODO: insert function (given an index and a value, insert a new node at that index)
  //TODO: remove function (given an index, remove the node at that index)
  //TODO: reverse function (in place reversal)
}

function test() {
  const myLL = new LinkedList(4);
  console.log(myLL);
  myLL.push(5);
  console.log(myLL);

  console.log("Should return 5", myLL.pop());
  myLL.unshift(3);
  console.log(myLL);
  console.log("Should return 3", myLL.shift());
  console.log("Should return 4", myLL.shift());
  console.log("Should return error", myLL.shift());
}

test();
