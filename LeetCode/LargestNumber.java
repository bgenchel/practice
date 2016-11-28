/*LARGEST NUMBER (medium)

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases. */


/* 	my psuedo code:
	take each number in the list, split it into an array of its digits,
	sort(store in a priority_queue) by first digit, if match, by second digit, etc.
	if one number is longer than another, check its extra digits against the last digit
	of the first to see who goes first */
	
public class Solution{

	public static void main(String[] args){
		System.out.println("this is where the solution will be.");
		System.out.println(args[0] + " " + args[1]);
	}

	public LargestNumber(int[] list){


	}
}

/*note to self, I need to learn how to implement generics in java*/
public class priority_que{
	public class Node{
		public int[] data;
		public Node parent, left, right = null;

		public Node(int[] data){
			this.data = data;
		}
	}

	public Node root;

	public priority_que(){ 
	}

	protected int[] toArray(int data){
		stack<Integer> digits;
		while(data != 0){
			 digits.push(data%10);
			 data /= 10;
		}
		ArrayList<Integer> num_array;
		while(!digits.empty()){
			num_array.append(digits.pop());
		}
		return num_array;
	}

	public void push(int data){
		Node in  = new Node(toArray(data));
		if(root == null){
			root = new Node(dat);
			return;
		}

		Node prev = null;
		Node curr = root;
		while(curr != null){

		}

}

