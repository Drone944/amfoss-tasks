use std::io;

fn tocheckprime(num: u32) -> bool {
    if num <= 1 {
        return false;
    }
    for i in 2..(num / 2 + 1) {
        if num % i == 0 {
            return false;
        }
    }
    true
}

fn main() {
    let mut input = String::new();

    println!("Enter an integer:");
    io::stdin()
    	.read_line(&mut input)
    	.expect("Failed to read line");

    let num: u32 = input.trim().parse().expect("Invalid input");

    if num == 0||num == 1 {
    	println!("{} is neither a prime nor a composite number.",num)
    } else {
    	println!("--------");
    	for num in 2..=num {
        	if tocheckprime(num) {
            	println!("{}", num);
    		}
        }
    }
}