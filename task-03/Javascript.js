const prompt=require("prompt-sync")({sigint:true});
const a = prompt("Enter the number : ");

if ((a==1)||(a==0)){
	console.log(a," is neither a prime nor a composite number.");
} else if (a==2) {
	console.log(a);
} else {
	for (let i = 2; i<=a; i++){
		let c = 0;
		for(let j = 2; j<=i; j++){
			if ((i%j==0)&&(i!=j)){
				c = 1;
				break;
			}
			else{
				c = 2;
			}
		}
		if (c==2){
			console.log(i);
		}
	}
}