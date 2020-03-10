//debug code for the odd issue that I faced
package main

import (
	"fmt"
	"os"
	"io"
)

func sumsqrt(x int, y int) int {
	return x + (y * y)
}

func readIn() int {	
	var num int
	c := 0
	sum := 0
	n, err := fmt.Fscanln(os.Stdin, &num)
	if (err != nil || n == 0) {
		fmt.Fprintf(os.Stderr, "ReadIn: Fscanf: %v\n", err)
		return 0
	} else if (err != io.EOF) {
		sum := readNum(sum, num, c)
		return sum
	}
	return sum
}

func readNum(sum int, num int, c int) int {
	fmt.Printf("[%d] = [%d]\n", c, num)
	if c == num {
		fmt.Printf("start readNum\n")
		//fmt.Scanf("\n")
		fmt.Printf("end readNum\n")
	} else {
		var temp rune
		var temp2 int
		n2, err2 := fmt.Scanf("%d", &temp2)
		fmt.Printf("{%d}..", temp2)
		if (err2 != nil || n2 == 0) {
			fmt.Fprintf(os.Stderr, "ReadNum: Fscanf: %v\n", err2)
			return 0
		}
		if (c == num - 1){
			n, err := fmt.Scanf("%c", &temp)
			fmt.Printf("[%c],", temp)
			if (err != nil || n == 0) {
				fmt.Fprintf(os.Stderr, "ReadNum: Fscanf: %v\n", err)
				return 0
			} else if (err != io.EOF) {
				sum = 1
				//if temp > 0 {
				//	sum = sumsqrt(sum, temp)
				//}
			}
		}
		c++
		sum = readNum(sum, num, c)
	}
	return sum
}

func recur(count int, testcases int, sum int, testlist []int) []int {
	if count != testcases {
		sum = readIn()
		count++
		testlist = append(testlist, sum)
		testlist = recur(count, testcases, 0, testlist)
	}
	return testlist
}

func main() {
	var testcases int
	var testlist []int

	count := 0
	n, err := fmt.Fscanln(os.Stdin, &testcases)
	if (err != nil || n == 0) {
		fmt.Fprintf(os.Stderr, "Fscanf: %v\n", err)
	} else if (err != io.EOF){
		testlist = recur(count, testcases, 0, testlist)
		fmt.Fprintf(os.Stdout, "%v\n", testlist)

	}

}