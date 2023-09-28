ppackage main
import ("fmt")

func main(){
	var a int

	fmt.Print("Enter a number : ")
	fmt.Println()
	fmt.Scan(&a)
	
	if (a==0)||(a==1){
	  fmt.Println(a,"is neither a prime nor a composite number.")
	}else if a==2{
	  fmt.Println(a)
	}else{
	  for i := 2; i <= a; i++ {
	    var c int
	    for j := 2; j <a; j++ {
	      if (i%j==0)&&(i!=j){
	        c = 1
	        break
	      }else{
	        c = 2
	      }
	      }
	      if (c==2){
	        fmt.Println(i)
	      }
	    }
	  }
}